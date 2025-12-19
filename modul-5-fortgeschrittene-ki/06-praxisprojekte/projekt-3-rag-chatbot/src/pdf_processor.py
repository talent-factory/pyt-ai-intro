"""PDF-Verarbeitungsmodul.

Dieses Modul extrahiert Text aus PDF-Dateien und teilt ihn in Chunks auf.
"""

import logging
from pathlib import Path
from typing import Any

import fitz  # PyMuPDF
from langchain_text_splitters import RecursiveCharacterTextSplitter

from .config import Config

logger = logging.getLogger(__name__)


class PDFProcessor:
    """Klasse für PDF-Verarbeitung und Text-Chunking."""

    def __init__(
        self, chunk_size: int = Config.CHUNK_SIZE, chunk_overlap: int = Config.CHUNK_OVERLAP
    ):
        """Initialisiert den PDF-Processor.

        Args:
            chunk_size: Grösse der Text-Chunks in Zeichen
            chunk_overlap: Überlappung zwischen Chunks in Zeichen
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", " ", ""],
        )

    def extract_text_from_pdf(self, pdf_path: Path | str) -> list[dict[str, Any]]:
        """Extrahiert Text aus einem PDF-Dokument.

        Args:
            pdf_path: Pfad zum PDF-Dokument

        Returns:
            list[dict]: Liste von Dictionaries mit Text und Metadaten pro Seite

        Raises:
            FileNotFoundError: Wenn PDF-Datei nicht existiert
            Exception: Bei Fehlern beim Lesen des PDFs
        """
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise FileNotFoundError(f"PDF-Datei nicht gefunden: {pdf_path}")

        logger.info(f"Extrahiere Text aus: {pdf_path.name}")

        pages_data = []

        try:
            with fitz.open(pdf_path) as doc:
                for page_num, page in enumerate(doc, start=1):
                    text = page.get_text()

                    if text.strip():  # Nur nicht-leere Seiten
                        pages_data.append(
                            {
                                "text": text,
                                "page": page_num,
                                "filename": pdf_path.name,
                                "total_pages": len(doc),
                            }
                        )

            logger.info(f"Text von {len(pages_data)} Seiten extrahiert")
            return pages_data

        except Exception as e:
            logger.error(f"Fehler beim Extrahieren von Text: {e}")
            raise

    def chunk_text(self, pages_data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Teilt Text in Chunks auf und behält Metadaten.

        Args:
            pages_data: Liste von Seiten-Daten mit Text und Metadaten

        Returns:
            list[dict]: Liste von Chunks mit Text und Metadaten
        """
        logger.info("Teile Text in Chunks auf...")

        all_chunks = []

        for page_data in pages_data:
            text = page_data["text"]
            chunks = self.text_splitter.split_text(text)

            for chunk_idx, chunk in enumerate(chunks):
                all_chunks.append(
                    {
                        "text": chunk,
                        "metadata": {
                            "page": page_data["page"],
                            "filename": page_data["filename"],
                            "total_pages": page_data["total_pages"],
                            "chunk_index": chunk_idx,
                        },
                    }
                )

        logger.info(f"{len(all_chunks)} Chunks erstellt")
        return all_chunks

    def process_pdf(self, pdf_path: Path | str) -> list[dict[str, Any]]:
        """Verarbeitet ein PDF: Extraktion und Chunking.

        Args:
            pdf_path: Pfad zum PDF-Dokument

        Returns:
            list[dict]: Liste von Chunks mit Text und Metadaten

        Raises:
            FileNotFoundError: Wenn PDF-Datei nicht existiert
            Exception: Bei Verarbeitungsfehlern
        """
        pages_data = self.extract_text_from_pdf(pdf_path)
        chunks = self.chunk_text(pages_data)
        return chunks


def validate_pdf_file(
    file_path: Path | str, max_size_bytes: int = Config.MAX_FILE_SIZE_BYTES
) -> tuple[bool, str]:
    """Validiert eine PDF-Datei.

    Args:
        file_path: Pfad zur Datei
        max_size_bytes: Maximale Dateigrösse in Bytes

    Returns:
        tuple[bool, str]: (ist_gültig, fehlermeldung)
    """
    file_path = Path(file_path)

    # Prüfe ob Datei existiert
    if not file_path.exists():
        return False, "Datei existiert nicht"

    # Prüfe Dateierweiterung
    if file_path.suffix.lower() != ".pdf":
        return False, "Datei ist kein PDF"

    # Prüfe Dateigrösse
    file_size = file_path.stat().st_size
    if file_size > max_size_bytes:
        max_mb = max_size_bytes / (1024 * 1024)
        return False, f"Datei ist zu gross (max. {max_mb:.0f} MB)"

    # Prüfe ob PDF lesbar ist
    try:
        with fitz.open(file_path) as doc:
            if len(doc) == 0:
                return False, "PDF enthält keine Seiten"
    except Exception as e:
        return False, f"PDF kann nicht geöffnet werden: {str(e)}"

    return True, ""
