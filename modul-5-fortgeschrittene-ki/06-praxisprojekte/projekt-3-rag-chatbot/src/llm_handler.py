"""LLM Handler für Claude API Integration.

Dieses Modul verwaltet die Kommunikation mit der Claude API.
"""

import logging
from typing import Any, Iterator

from anthropic import Anthropic

from .config import SYSTEM_PROMPT, Config, get_user_prompt

logger = logging.getLogger(__name__)


class LLMHandler:
    """Klasse für Claude API Integration."""

    def __init__(
        self,
        api_key: str = Config.ANTHROPIC_API_KEY,
        model: str = Config.LLM_MODEL,
        max_tokens: int = Config.LLM_MAX_TOKENS,
        temperature: float = Config.LLM_TEMPERATURE,
    ):
        """Initialisiert den LLM Handler.

        Args:
            api_key: Anthropic API Key
            model: Modell-Name
            max_tokens: Maximale Anzahl Tokens
            temperature: Temperatur für Antwort-Generierung

        Raises:
            ValueError: Wenn API-Key fehlt
        """
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY fehlt. Bitte in .env-Datei setzen.")

        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature

        logger.info(f"LLM Handler initialisiert mit Modell: {model}")

    def generate_response(
        self, user_question: str, retrieved_chunks: list[dict[str, Any]], stream: bool = False
    ) -> str | Iterator[str]:
        """Generiert eine Antwort basierend auf der Frage und den Chunks.

        Args:
            user_question: Frage des Benutzers
            retrieved_chunks: Liste von relevanten Chunks
            stream: Ob die Antwort gestreamt werden soll

        Returns:
            str | Iterator[str]: Antwort oder Stream von Antwort-Teilen

        Raises:
            Exception: Bei API-Fehlern
        """
        if not retrieved_chunks:
            return "Ich konnte keine relevanten Informationen in den Dokumenten finden."

        # Erstelle User-Prompt
        user_prompt = get_user_prompt(retrieved_chunks, user_question)

        logger.info(f"Generiere Antwort für: '{user_question[:50]}...'")

        try:
            if stream:
                return self._generate_streaming_response(user_prompt)
            else:
                return self._generate_standard_response(user_prompt)

        except Exception as e:
            logger.error(f"Fehler bei API-Aufruf: {e}")
            raise

    def _generate_standard_response(self, user_prompt: str) -> str:
        """Generiert eine Standard-Antwort (nicht gestreamt).

        Args:
            user_prompt: Formatierter User-Prompt

        Returns:
            str: Generierte Antwort
        """
        response = self.client.messages.create(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )

        answer = response.content[0].text
        logger.info(f"Antwort generiert ({len(answer)} Zeichen)")
        return answer

    def _generate_streaming_response(self, user_prompt: str) -> Iterator[str]:
        """Generiert eine gestreamte Antwort.

        Args:
            user_prompt: Formatierter User-Prompt

        Yields:
            str: Teile der Antwort
        """
        logger.info("Starte Streaming-Response")

        with self.client.messages.stream(
            model=self.model,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        ) as stream:
            for text in stream.text_stream:
                yield text

    def validate_api_key(self) -> bool:
        """Validiert den API-Key durch einen Test-Aufruf.

        Returns:
            bool: True wenn API-Key gültig, sonst False
        """
        try:
            self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{"role": "user", "content": "Test"}],
            )
            return True
        except Exception as e:
            logger.error(f"API-Key Validierung fehlgeschlagen: {e}")
            return False


def format_sources(retrieved_chunks: list[dict[str, Any]]) -> str:
    """Formatiert die Quellenangaben für die Anzeige.

    Args:
        retrieved_chunks: Liste von Chunks mit Metadaten

    Returns:
        str: Formatierte Quellenangaben
    """
    if not retrieved_chunks:
        return "Keine Quellen gefunden."

    sources = []
    for i, chunk in enumerate(retrieved_chunks, start=1):
        metadata = chunk["metadata"]
        score = chunk["score"]

        source = (
            f"**Quelle {i}:** {metadata['filename']} "
            f"(Seite {metadata['page']}, "
            f"Relevanz: {score:.2%})"
        )
        sources.append(source)

    return "\n".join(sources)

