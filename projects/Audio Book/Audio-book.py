import argparse
import os
import sys
from gtts import gTTS

__author__ = "https://github.com/master-coder1998"


def extract_text_from_pdf(path: str) -> str:
    if not os.path.isfile(path):
        raise FileNotFoundError(f"PDF not found: {path}")

    # Try modern PyPDF2 API first (PdfReader)
    try:
        from PyPDF2 import PdfReader

        with open(path, "rb") as f:
            reader = PdfReader(f)
            texts = []
            for page in reader.pages:
                try:
                    texts.append(page.extract_text() or "")
                except Exception:
                    continue
            return " ".join(texts)
    except Exception:
        # Fallback to older PyPDF2 API
        try:
            import PyPDF2

            with open(path, "rb") as f:
                reader = PyPDF2.PdfFileReader(f)
                texts = []
                for i in range(reader.numPages):
                    try:
                        page = reader.getPage(i)
                        texts.append(page.extractText() or "")
                    except Exception:
                        continue
                return " ".join(texts)
        except Exception as e:
            raise RuntimeError(f"Failed to read PDF: {e}")


def text_to_speech(text: str, out_path: str, lang: str = "en", slow: bool = False) -> None:
    if not text or not text.strip():
        raise ValueError("No text extracted from PDF to convert to audio.")
    tts = gTTS(text=text, lang=lang, slow=slow)
    tts.save(out_path)


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PDF text to speech (MP3) using gTTS")
    parser.add_argument("--input", "-i", default="introduction-aws-security.pdf", help="Path to input PDF file")
    parser.add_argument("--output", "-o", default="Audio.mp3", help="Output MP3 file path")
    parser.add_argument("--lang", "-l", default="en", help="Language code for gTTS (default: en)")
    parser.add_argument("--slow", action="store_true", help="Speak more slowly")
    args = parser.parse_args()

    try:
        text = extract_text_from_pdf(args.input)
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        sys.exit(2)
    except Exception as e:
        print(f"Error extracting text from PDF: {e}", file=sys.stderr)
        sys.exit(3)

    if not text.strip():
        print("No text was extracted from the PDF.", file=sys.stderr)
        sys.exit(4)

    try:
        text_to_speech(text, args.output, lang=args.lang, slow=args.slow)
        print(f"Saved audio to {args.output}")
    except Exception as e:
        print(f"Error generating audio: {e}", file=sys.stderr)
        sys.exit(5)


if __name__ == "__main__":
    main()
