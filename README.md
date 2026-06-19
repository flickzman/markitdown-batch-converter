A completely unefforted and Vive-coded project by Flickzman
https://www.instagram.com/12niicoo/

# MarkItDown Batch Converter

Drop-and-run script to batch convert PDF, Excel, Word, and image files to Markdown using Microsoft's MarkItDown library.

## Requirements

Python 3.10 or higher.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Drop `convert_all.py` into the folder with your files
2. Run:

```bash
py convert_all.py
```

3. Find your Markdown files in the `markdown_output` subfolder.

## Supported formats

### Documents
- PDF (.pdf)
- Excel (.xlsx, .xls)
- Word (.docx)

### Images (with OCR)
- JPG (.jpg, .jpeg)
- PNG (.png)
- GIF (.gif)
- WebP (.webp)
- BMP (.bmp)
- TIFF (.tiff)

**Note:** Image processing requires Tesseract OCR to be installed. The script supports Spanish and English languages. Images will be skipped if OCR dependencies are not available.

## Optional Dependencies

For full image OCR support, install additional dependencies:

```bash
pip install pytesseract pillow
```

And install Tesseract-OCR:
- **Windows:** Download from https://github.com/UB-Mannheim/tesseract/wiki
- **macOS:** `brew install tesseract`
- **Linux:** `apt-get install tesseract-ocr`

## Credits

Built on top of Microsoft MarkItDown:
https://github.com/microsoft/markitdown
