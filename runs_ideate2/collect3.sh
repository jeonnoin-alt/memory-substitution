#!/bin/bash
cd /home/work/neuro/memory-substitution; P=/home/work/neuro/alfworld-env/bin/python
for s in xfer credit static; do
  $P tools/ideate2/prescan.py collect --slug $s --out runs_ideate2/$s --axes runs_ideate2/$s/axes.json --rerank --top 50 --sections 0 > runs_ideate2/$s/collect.log 2>&1
  echo "$s: $(tail -2 runs_ideate2/$s/collect.log | head -1)"
done
echo ALLDONE
