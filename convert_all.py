"""
MarkItDown Batch Converter
Converts PDF, Excel, Word, and image files to Markdown.
Images are processed with Tesseract OCR.
Usage: py convert_all.py
"""

from pathlib import Path
from markitdown import MarkItDown

IMAGE_FORMATS = (".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff")
OTHER_FORMATS = (".pdf", ".xlsx", ".xls", ".docx")
SUPPORTED = OTHER_FORMATS + IMAGE_FORMATS

INPUT_DIR = Path(__file__).parent
OUTPUT_DIR = INPUT_DIR / "markdown_output"

# Check for Tesseract + pytesseract
try:
    import pytesseract
    from PIL import Image
    import pytesseract

    # Common Tesseract install path on Windows
    TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if Path(TESSERACT_PATH).exists():
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    OCR_AVAILABLE = True
except ImportError:
    OCR_AVAILABLE = False


def ocr_to_markdown(file_path: Path) -> str:
    img = Image.open(file_path)
    text = pytesseract.image_to_string(img, lang="spa+eng")
    return f"# {file_path.stem}\n\n{text.strip()}"


def main():
    if not INPUT_DIR.exists():
        print(f"ERROR: Folder not found: {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md = MarkItDown()

    files = [f for f in INPUT_DIR.iterdir() if f.suffix.lower() in SUPPORTED]

    if not files:
        print(f"No supported files found in: {INPUT_DIR}")
        return

    print(f"Found {len(files)} file(s) to convert. Output -> {OUTPUT_DIR}\n")

    if not OCR_AVAILABLE:
        print("  [WARN] pytesseract or Pillow not installed. Images will be skipped.\n"
              "         Run: py -m pip install pytesseract pillow\n")

    ok, fail = 0, 0

    for file_path in sorted(files):
        is_image = file_path.suffix.lower() in IMAGE_FORMATS
        try:
            if is_image:
                if not OCR_AVAILABLE:
                    print(f"  [SKIP] {file_path.name}  ->  OCR not available")
                    fail += 1
                    continue
                markdown = ocr_to_markdown(file_path)
            else:
                result = md.convert(str(file_path))
                markdown = result.markdown

            out_file = OUTPUT_DIR / f"{file_path.stem}.md"
            out_file.write_text(markdown, encoding="utf-8")
            print(f"  [OK]   {file_path.name}")
            ok += 1
        except Exception as e:
            print(f"  [FAIL] {file_path.name}  ->  {e}")
            fail += 1

    print(f"\nDone. {ok} converted, {fail} failed.")
    print(f"Markdown files saved in: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()