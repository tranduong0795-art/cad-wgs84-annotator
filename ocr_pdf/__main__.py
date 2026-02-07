import argparse
from pathlib import Path

from pdf2image import convert_from_path
import pytesseract


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="OCR quet PDF va trich xuat van ban.")
    parser.add_argument("pdf_path", type=Path, help="Duong dan toi file PDF")
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Duong dan file luu ket qua (neu bo qua se in ra man hinh)",
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="eng",
        help="Ma ngon ngu Tesseract (vi du: eng, vie, eng+vie)",
    )
    parser.add_argument(
        "--dpi",
        type=int,
        default=300,
        help="Do phan giai de chuyen PDF sang anh",
    )
    return parser.parse_args()


def ocr_pdf(pdf_path: Path, lang: str, dpi: int) -> str:
    if not pdf_path.exists():
        raise FileNotFoundError(f"Khong tim thay file: {pdf_path}")

    images = convert_from_path(str(pdf_path), dpi=dpi)
    extracted_pages = []

    for page_index, image in enumerate(images, start=1):
        text = pytesseract.image_to_string(image, lang=lang)
        header = f"\n===== Trang {page_index} =====\n"
        extracted_pages.append(header + text.strip())

    return "\n".join(extracted_pages).strip()


def main() -> None:
    args = parse_args()
    result = ocr_pdf(args.pdf_path, args.lang, args.dpi)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(result, encoding="utf-8")
    else:
        print(result)


if __name__ == "__main__":
    main()
