#!/bin/bash
# Auto-commit + push the experiment repo, and mirror Claude session data to NAS.
# Invoked by Claude Code hooks (PostToolUse async, Stop). Safe to run any time.
# Reads (and ignores) hook JSON on stdin. Serialized with flock; skips if another run is active.
R=/home/work/neuro/memory-substitution
NAS=/home/work/neuro/claude
cat >/dev/null 2>&1   # drain stdin
exec 9>/tmp/claude-autocommit.lock
flock -n 9 || exit 0
cd "$R" || exit 0
if [ -n "$(git status --porcelain 2>/dev/null)" ]; then
  git add -A
  # never commit a credential
  if git diff --cached | grep -qE 'github_pat_[A-Za-z0-9_]{20,}|ghp_[A-Za-z0-9]{30,}|sk-ant-(api|oat)[A-Za-z0-9_-]{20,}'; then
    git reset -q
    echo '{"systemMessage":"autocommit: credential-like string in staged diff — commit skipped, fix before pushing"}'
    exit 0
  fi
  git commit -q -m "auto: $(date -u +%Y-%m-%dT%H:%M:%SZ) (${1:-hook})" 2>/dev/null || true
fi
if [ -n "$(git log origin/main..HEAD --oneline 2>/dev/null)" ]; then
  timeout 90 git push -q origin HEAD:main 2>/dev/null || echo '{"systemMessage":"autocommit: push failed (network?) — commits are local, will retry on next hook"}'
fi
# mirror session transcripts + memory + settings to NAS (survives node recycle)
if [ -d /home/work/.claude/projects ] && [ ! -L /home/work/.claude/projects ]; then
  mkdir -p "$NAS/projects"
  rsync -a --exclude '*.lock' /home/work/.claude/projects/ "$NAS/projects/" 2>/dev/null || true
fi
[ -f /home/work/.claude/settings.json ] && [ ! -L /home/work/.claude/settings.json ] && cp /home/work/.claude/settings.json "$NAS/settings.json" 2>/dev/null
exit 0
