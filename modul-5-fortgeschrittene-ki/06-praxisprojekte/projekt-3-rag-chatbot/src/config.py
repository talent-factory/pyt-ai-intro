"""Konfigurationsmodul für den RAG-ChatBot.

Dieses Modul lädt Umgebungsvariablen und stellt Konfigurationswerte bereit.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# Lade .env-Datei
load_dotenv()


class Config:
    """Zentrale Konfigurationsklasse."""

    # API-Keys
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    # Pfade
    BASE_DIR: Path = Path(__file__).parent.parent
    DATA_DIR: Path = BASE_DIR / "data"
    CHROMA_PERSIST_DIR: Path = Path(
        os.getenv("CHROMA_PERSIST_DIRECTORY", str(DATA_DIR / "chroma_db"))
    )

    # Embedding-Einstellungen
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

    # LLM-Einstellungen
    LLM_MODEL: str = os.getenv("LLM_MODEL", "claude-3-5-sonnet-20241022")
    LLM_MAX_TOKENS: int = int(os.getenv("LLM_MAX_TOKENS", "4096"))
    LLM_TEMPERATURE: float = float(os.getenv("LLM_TEMPERATURE", "0.7"))

    # Chunking-Einstellungen
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "200"))

    # Retrieval-Einstellungen
    TOP_K_RESULTS: int = int(os.getenv("TOP_K_RESULTS", "5"))
    SIMILARITY_THRESHOLD: float = float(os.getenv("SIMILARITY_THRESHOLD", "0.7"))

    # Upload-Einstellungen
    MAX_FILE_SIZE_MB: int = int(os.getenv("MAX_FILE_SIZE_MB", "50"))
    MAX_FILE_SIZE_BYTES: int = MAX_FILE_SIZE_MB * 1024 * 1024

    @classmethod
    def validate(cls) -> bool:
        """Validiert die Konfiguration.

        Returns:
            bool: True wenn Konfiguration gültig, sonst False
        """
        if not cls.ANTHROPIC_API_KEY:
            return False

        # Erstelle notwendige Verzeichnisse
        cls.DATA_DIR.mkdir(parents=True, exist_ok=True)
        cls.CHROMA_PERSIST_DIR.mkdir(parents=True, exist_ok=True)

        return True


# System-Prompt für Claude
SYSTEM_PROMPT = """Du bist ein hilfreicher Assistent, der Fragen zu hochgeladenen 
PDF-Dokumenten beantwortet. Basiere deine Antworten ausschliesslich auf dem 
bereitgestellten Kontext aus den Dokumenten.

Wichtige Regeln:
- Beantworte Fragen nur basierend auf dem bereitgestellten Kontext
- Falls die Information nicht im Kontext enthalten ist, sage dies deutlich
- Gib wenn möglich Seitenzahlen und Quellenangaben an
- Sei präzise und konkret
- Verwende die Schweizer Schreibweise (ss statt ß)
"""


def get_user_prompt(retrieved_chunks: list[dict], user_question: str) -> str:
    """Erstellt den User-Prompt für Claude.

    Args:
        retrieved_chunks: Liste von Chunks mit Metadaten
        user_question: Frage des Benutzers

    Returns:
        str: Formatierter User-Prompt
    """
    context = "\n\n".join(
        [
            f"[Quelle: {chunk['metadata']['filename']}, "
            f"Seite {chunk['metadata']['page']}, "
            f"Relevanz: {chunk['score']:.2f}]\n{chunk['text']}"
            for chunk in retrieved_chunks
        ]
    )

    return f"""Kontext aus den Dokumenten:
{context}

Frage: {user_question}

Beantworte die Frage präzise basierend auf dem Kontext. Gib wenn möglich 
Seitenzahlen und Quellenangaben an."""

