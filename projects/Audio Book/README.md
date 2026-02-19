# Audio Book

Convert a PDF into an MP3 using Google Text-to-Speech (gTTS).

**Author:** https://github.com/master-coder1998

## Description
This small utility extracts text from a PDF and saves spoken audio as an MP3 file.

## Files
- `Audio-book.py` — main script (CLI)
- `introduction-aws-security.pdf` — example PDF included in this folder
- `requirements.txt` — Python dependencies

## Requirements
Install dependencies into your virtual environment:

```bash
python -m pip install -r "projects/Audio Book/requirements.txt"
```

## Usage
Run the script from the repository root (examples):

Basic (uses included PDF and default output):

```bash
python "projects/Audio Book/Audio-book.py"
```

Specify input and output paths:

```bash
python "projects/Audio Book/Audio-book.py" -i "projects/Audio Book/introduction-aws-security.pdf" -o "projects/Audio Book/Audio.mp3"
```

Options:
- `-i`, `--input`  : path to input PDF (default: `introduction-aws-security.pdf`)
- `-o`, `--output` : path to output MP3 (default: `Audio.mp3`)
- `-l`, `--lang`   : language code for gTTS (default: `en`)
- `--slow`         : speak more slowly

## Notes
- The script attempts to use modern `PyPDF2.PdfReader` and falls back to older API if needed.
- Ensure your virtual environment is active when installing/running.
- gTTS requires network access to generate speech.
