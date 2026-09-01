import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
path = Path(r"C:\Users\ajtab\Downloads\Шаблон отчета.docx")
root = ET.fromstring(zipfile.ZipFile(path).read("word/document.xml"))

for i, para in enumerate(root.findall(".//w:p", ns), 1):
    texts = [t.text or "" for t in para.findall(".//w:t", ns)]
    txt = "".join(texts).strip()
    if txt:
        print(f"{i}: {txt}")
