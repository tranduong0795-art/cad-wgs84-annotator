# PDF OCR App

Ung dung nay quet file PDF va trich xuat van ban bang OCR.

## Cai dat

1. Tao moi truong ao (khuyen nghi):
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
2. Cai dat thu vien:
   ```bash
   pip install -r requirements.txt
   ```
3. Cai dat cac cong cu he thong (tuy may):
   - `tesseract-ocr`
   - `poppler` (de chay `pdf2image`)

## Su dung

```bash
python -m ocr_pdf path/to/file.pdf --output output.txt --lang vie
```

Neu khong truyen `--output`, ung dung se in ket qua ra man hinh.

## Ghi chu

- `--lang` su dung ma ngon ngu cua Tesseract, vi du: `eng`, `vie`, hoac `eng+vie`.
- Da ho tro PDF nhieu trang.
