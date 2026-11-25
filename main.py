import os

MOTTO = "I replaced three meetings, two spreadsheets, and one tired intern \u2014 and the intern says thanks."

output_dir = os.environ.get("OUTPUT_DIR", "/output")
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(MOTTO)
os.chmod(os.path.join(output_dir, "entry.txt"), 0o644)
