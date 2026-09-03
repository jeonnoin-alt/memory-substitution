#!/usr/bin/env python3
"""Generate all arm config JSONs from the frozen DESIGN §4 table."""
import json, os
HERE=os.path.dirname(os.path.abspath(__file__)); A=os.path.join(HERE,"arms")
I=json.load(open(os.path.join(HERE,"..","prereg","instructions.json")))
IS,IB=I["I_star"],I["I_B"]
def w(name,**kw):
    cfg={"instruction_text":"","memory_arm":None,"floor":"none","max_calls":8}
    cfg.update(kw); json.dump(cfg,open(os.path.join(A,name+".json"),"w"),indent=1)
# bare memory conditions
for m in ["M1","M2","M2i","M3","M4","M5","M5r","M8","ANCHOR","ANCHOR_NH","M6"]:
    w(m, memory_arm=m, **({"max_calls":11} if m=="M6" else {}))
w("M0")
# Fs (instruction only)
for m,tag in [("","M0"),("M1","M1"),("M2","M2"),("ANCHOR","ANCHOR")]:
    w(f"{tag}_Fs", memory_arm=(m or None), instruction_text=IS, floor="none")
# Fh
for m,tag in [("","M0"),("M1","M1"),("M2","M2"),("ANCHOR","ANCHOR"),("M8","M8")]:
    w(f"{tag}_Fh", memory_arm=(m or None), instruction_text=IS, floor="hard")
# I_B
w("IB_M0", instruction_text=IB); w("IB_M1", memory_arm="M1", instruction_text=IB)
# closed book
w("M0_CB", max_calls=1, closed_book=True)
print("configs:", sorted(os.listdir(A)))
