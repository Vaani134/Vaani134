from pathlib import Path
import pdfplumber

pdf_path = Path(r'd:/Portfolio/Vaani134/Software Developer – Web Applications, Search & Security.pdf')
print('exists', pdf_path.exists())
with pdfplumber.open(pdf_path) as pdf:
    text = '\n'.join(page.extract_text() or '' for page in pdf.pages)
print(text[:50000])
