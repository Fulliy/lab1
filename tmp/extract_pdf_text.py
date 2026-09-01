import os
import re
import zlib
from pathlib import Path

downloads = Path(os.path.join(os.environ["USERPROFILE"], "Downloads"))
pdf = next(p for p in downloads.iterdir() if "React" in p.name and p.suffix.lower() == ".pdf")
data = pdf.read_bytes()
texts = []

for m in re.finditer(rb"stream\r?\n", data):
    start = m.end()
    end = data.find(b"endstream", start)
    if end == -1:
        continue
    stream = data[start:end].strip(b"\r\n")
    try:
        decoded = zlib.decompress(stream)
    except Exception:
        continue
    texts.extend(re.findall(rb"\((?:\\.|[^\\()])*\)\s*Tj", decoded))
    for arr in re.findall(rb"\[(.*?)\]\s*TJ", decoded, flags=re.S):
        texts.extend(re.findall(rb"\((?:\\.|[^\\()])*\)", arr))

seen = set()
for b in texts:
    t = b.decode("latin1", "ignore")
    if len(t) >= 2:
        t = t[1:-1]
        t = t.encode("latin1", "ignore").decode("utf-8", "ignore")
    if t.strip() and t not in seen:
        seen.add(t)
        print(t)
