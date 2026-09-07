#!/usr/bin/env python3
"""LoRA feasibility check for the parametric route on this node: fine-tune a local backbone (QLoRA 4-bit or bf16 LoRA)
on ALFWorld trajectories rendered as chat turns (the same prompt scaffold the agent uses), report tokens/s, peak memory,
loss curve. Usage (train-env):
  lora_sft.py --model /home/work/neuro/models/qwen3-32b --bank 'runs/bank/expert_shard*.jsonl' --out runs/lora/qwen3-32b_expert --steps 200 --qlora"""
import os, sys, json, glob, time, argparse, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from prompts import SYSTEM

ap = argparse.ArgumentParser()
ap.add_argument("--model", required=True); ap.add_argument("--bank", required=True); ap.add_argument("--out", required=True)
ap.add_argument("--steps", type=int, default=200); ap.add_argument("--qlora", action="store_true"); ap.add_argument("--rank", type=int, default=32)
ap.add_argument("--lr", type=float, default=1e-4); ap.add_argument("--max-len", type=int, default=2048); ap.add_argument("--grad-accum", type=int, default=8)
a = ap.parse_args(); os.makedirs(a.out, exist_ok=True)
tok = AutoTokenizer.from_pretrained(a.model)
items = [json.loads(l) for p in sorted(glob.glob(a.bank)) for l in open(p)]
items = [it for it in items if it.get("won") and it.get("steps")]
random.Random(0).shuffle(items)
print(f"{len(items)} won trajectories", flush=True)


def render(it):
    """One training example per step: (goal, history, obs, admissible? unknown offline -> omitted) -> 'Action: a'."""
    exs = []; hist = []
    obs = it["init_obs"]
    for s in it["steps"]:
        hist_txt = "\n".join(f"> {x}\n{o[:300]}" for x, o in hist[-30:]) or "(none yet)"
        user = f"Goal: {it['goal']}\n\nHistory:\n{hist_txt}\n\nLatest observation:\n{obs[:600]}\n\nReply with 'Action: <one admissible action>'."
        msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
        prompt = tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True, enable_thinking=False)
        exs.append((prompt, f"Action: {s['action']}" + tok.eos_token))
        hist.append((s["action"], s["obs"])); obs = s["obs"]
    return exs

examples = [e for it in items for e in render(it)]
print(f"{len(examples)} step examples", flush=True)
if a.qlora:
    bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)
    model = AutoModelForCausalLM.from_pretrained(a.model, quantization_config=bnb, device_map={"": 0}, torch_dtype=torch.bfloat16)
    model = prepare_model_for_kbit_training(model, use_gradient_checkpointing=True)
else:
    model = AutoModelForCausalLM.from_pretrained(a.model, device_map={"": 0}, torch_dtype=torch.bfloat16)
    model.gradient_checkpointing_enable(); model.enable_input_require_grads()
cfg = LoraConfig(r=a.rank, lora_alpha=2 * a.rank, lora_dropout=0.05, task_type="CAUSAL_LM",
                 target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"])
model = get_peft_model(model, cfg); model.print_trainable_parameters()
opt = torch.optim.AdamW([p for p in model.parameters() if p.requires_grad], lr=a.lr, weight_decay=0.0)
model.train(); t0 = time.time(); toks = 0; losses = []
for step in range(a.steps):
    opt.zero_grad(set_to_none=True); acc = 0.0
    for _ in range(a.grad_accum):
        prompt, target = examples[random.randrange(len(examples))]
        p_ids = tok(prompt, add_special_tokens=False)["input_ids"][-(a.max_len - 64):]
        t_ids = tok(target, add_special_tokens=False)["input_ids"][:64]
        ids = torch.tensor([p_ids + t_ids], device="cuda"); labels = ids.clone(); labels[0, :len(p_ids)] = -100
        out = model(input_ids=ids, labels=labels); (out.loss / a.grad_accum).backward(); acc += out.loss.item() / a.grad_accum; toks += ids.numel()
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0); opt.step(); losses.append(acc)
    if step % 10 == 0 or step == a.steps - 1:
        el = time.time() - t0
        print(f"step {step} loss {acc:.3f} tok/s {toks/el:.0f} peak_mem {torch.cuda.max_memory_allocated()/2**30:.1f}GB elapsed {el:.0f}s", flush=True)
model.save_pretrained(a.out)
json.dump({"losses": losses, "examples": len(examples), "trajectories": len(items), "seconds": time.time() - t0,
           "peak_mem_gb": torch.cuda.max_memory_allocated() / 2**30, "qlora": a.qlora, "rank": a.rank}, open(os.path.join(a.out, "train_log.json"), "w"), indent=1)
print("saved", a.out)
