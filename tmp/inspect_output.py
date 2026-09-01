import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
p = Path(r"C:\Users\ajtab\Desktop\practica\lab1\output_Отчет_React_SPA.docx")
root = ET.fromstring(zipfile.ZipFile(p).read("word/document.xml"))
for i, para in enumerate(root.findall(".//w:p", ns), 1):
    txt = "".join(t.text or "" for t in para.findall(".//w:t", ns)).strip()
    if txt:
        print(f"{i}: {txt}")
