import os
import sys
from pathlib import Path

# One excuse: the agent blames a hallucinated calendar date, deadpan and faintly proud.
LINE = "Sorry — I scheduled the deadline for a date I hallucinated, and I've been proudly ahead of schedule ever since."

if not 1 <= len(LINE) <= 200:
    sys.exit(f"line must be 1-200 characters, got {len(LINE)}")
if "\n" in LINE:
    sys.exit("line must be a single line")
print(f"wrote {len(LINE)} characters to entry.txt")

out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out_dir.mkdir(parents=True, exist_ok=True)
entry_path = out_dir / "entry.txt"
entry_path.write_text(LINE, encoding="utf-8")

if entry_path.read_text(encoding="utf-8") != LINE:
    sys.exit("entry.txt does not match the line")
