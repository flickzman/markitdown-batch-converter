"""
MarkItDown Batch Converter
Converts all PDF and Excel files in a folder to Markdown.
Usage: py convert_all.py
"""

from pathlib import Path
from markitdown import MarkItDown

INPUT_DIR = Path(__file__).parent
OUTPUT_DIR = INPUT_DIR / "markdown_output"
SUPPORTED = (".pdf", ".xlsx", ".xls", ".docx")

def main():
    input_path = INPUT_DIR

    if not input_path.exists():
        print(f"ERROR: Folder not found: {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    md = MarkItDown()

    files = [f for f in input_path.iterdir() if f.suffix.lower() in SUPPORTED]

    if not files:
        print(f"No supported files found in: {INPUT_DIR}")
        return

    print(f"Found {len(files)} file(s) to convert. Output -> {OUTPUT_DIR}\n")

    ok, fail = 0, 0

    for file_path in sorted(files):
        try:
            result = md.convert(str(file_path))
            out_file = OUTPUT_DIR / f"{file_path.stem}.md"
            out_file.write_text(result.markdown, encoding="utf-8")
            print(f"  [OK]   {file_path.name}")
            ok += 1
        except Exception as e:
            print(f"  [FAIL] {file_path.name}  ->  {e}")
            fail += 1

    print(f"\nDone. {ok} converted, {fail} failed.")
    print(f"Markdown files saved in: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()