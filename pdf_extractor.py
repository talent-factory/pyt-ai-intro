"""
Einfaches Script zur Extraktion von Text aus PDF-Dateien mit Docling.
"""

import sys
from pathlib import Path
from docling.document_converter import DocumentConverter


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extrahiert Text aus einer PDF-Datei.
    
    Args:
        pdf_path: Pfad zur PDF-Datei
        
    Returns:
        Extrahierter Text aus dem PDF
    """
    pdf_file = Path(pdf_path)
    
    if not pdf_file.exists():
        raise FileNotFoundError(f"PDF-Datei nicht gefunden: {pdf_path}")
    
    if not pdf_file.suffix.lower() == ".pdf":
        raise ValueError(f"Datei ist kein PDF: {pdf_path}")
    
    # Konvertiere PDF zu Docling Document
    converter = DocumentConverter()
    doc = converter.convert(pdf_file)
    
    # Extrahiere Text
    text = doc.document.export_to_markdown()
    
    return text


def main():
    """Hauptfunktion für Command-Line Verwendung."""
    if len(sys.argv) < 2:
        print("Verwendung: python pdf_extractor.py <pdf_datei>")
        print("\nBeispiel: python pdf_extractor.py mein_dokument.pdf")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    
    try:
        text = extract_text_from_pdf(pdf_path)
        print(text)
    except FileNotFoundError as e:
        print(f"Fehler: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Fehler: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Fehler bei der PDF-Verarbeitung: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
