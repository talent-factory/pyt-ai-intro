"""Vector Store Modul für ChromaDB-Integration.

Dieses Modul verwaltet Embeddings und die Vektordatenbank.
"""

import logging
from typing import Any

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer

from .config import Config

logger = logging.getLogger(__name__)


class VectorStore:
    """Klasse für Vector Store Operationen mit ChromaDB."""

    def __init__(
        self,
        collection_name: str = "pdf_documents",
        embedding_model: str = Config.EMBEDDING_MODEL,
        persist_directory: str = str(Config.CHROMA_PERSIST_DIR),
    ):
        """Initialisiert den Vector Store.

        Args:
            collection_name: Name der ChromaDB Collection
            embedding_model: Name des Embedding-Modells
            persist_directory: Verzeichnis für persistente Speicherung
        """
        self.collection_name = collection_name
        self.embedding_model_name = embedding_model

        logger.info(f"Initialisiere Vector Store mit Modell: {embedding_model}")

        # Initialisiere Embedding-Modell
        self.embedding_model = SentenceTransformer(embedding_model)

        # Initialisiere ChromaDB Client
        self.client = chromadb.PersistentClient(
            path=persist_directory,
            settings=Settings(anonymized_telemetry=False),
        )

        # Hole oder erstelle Collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},
        )

        logger.info(f"Collection '{collection_name}' bereit")

    def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        """Generiert Embeddings für eine Liste von Texten.

        Args:
            texts: Liste von Texten

        Returns:
            list[list[float]]: Liste von Embedding-Vektoren
        """
        logger.info(f"Generiere Embeddings für {len(texts)} Texte...")
        embeddings = self.embedding_model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()

    def add_documents(self, chunks: list[dict[str, Any]]) -> int:
        """Fügt Dokument-Chunks zur Vector DB hinzu.

        Args:
            chunks: Liste von Chunks mit Text und Metadaten

        Returns:
            int: Anzahl hinzugefügter Chunks

        Raises:
            Exception: Bei Fehlern beim Hinzufügen
        """
        if not chunks:
            logger.warning("Keine Chunks zum Hinzufügen")
            return 0

        logger.info(f"Füge {len(chunks)} Chunks zur Vector DB hinzu...")

        try:
            # Extrahiere Texte und Metadaten
            texts = [chunk["text"] for chunk in chunks]
            metadatas = [chunk["metadata"] for chunk in chunks]

            # Generiere eindeutige IDs
            ids = [
                f"{chunk['metadata']['filename']}_"
                f"page{chunk['metadata']['page']}_"
                f"chunk{chunk['metadata']['chunk_index']}"
                for chunk in chunks
            ]

            # Generiere Embeddings
            embeddings = self.generate_embeddings(texts)

            # Füge zur Collection hinzu
            self.collection.add(
                embeddings=embeddings, documents=texts, metadatas=metadatas, ids=ids
            )

            logger.info(f"{len(chunks)} Chunks erfolgreich hinzugefügt")
            return len(chunks)

        except Exception as e:
            logger.error(f"Fehler beim Hinzufügen von Chunks: {e}")
            raise

    def search(
        self,
        query: str,
        top_k: int = Config.TOP_K_RESULTS,
        min_score: float = Config.SIMILARITY_THRESHOLD,
    ) -> list[dict[str, Any]]:
        """Sucht ähnliche Dokumente basierend auf einer Query.

        Args:
            query: Suchanfrage
            top_k: Anzahl der zurückzugebenden Ergebnisse
            min_score: Minimaler Similarity-Score (0-1)

        Returns:
            list[dict]: Liste von Ergebnissen mit Text, Metadaten und Score
        """
        logger.info(f"Suche nach: '{query[:50]}...'")

        try:
            # Generiere Query-Embedding
            query_embedding = self.embedding_model.encode([query])[0].tolist()

            # Suche in Collection
            results = self.collection.query(query_embeddings=[query_embedding], n_results=top_k)

            # Formatiere Ergebnisse
            formatted_results = []

            if results["documents"] and results["documents"][0]:
                for i, doc in enumerate(results["documents"][0]):
                    # ChromaDB gibt Distanzen zurück, konvertiere zu Similarity
                    distance = results["distances"][0][i]
                    similarity = 1 - distance  # Cosine similarity

                    if similarity >= min_score:
                        formatted_results.append(
                            {
                                "text": doc,
                                "metadata": results["metadatas"][0][i],
                                "score": similarity,
                                "id": results["ids"][0][i],
                            }
                        )

            logger.info(f"{len(formatted_results)} relevante Ergebnisse gefunden")
            return formatted_results

        except Exception as e:
            logger.error(f"Fehler bei der Suche: {e}")
            raise

    def delete_document(self, filename: str) -> int:
        """Löscht alle Chunks eines Dokuments.

        Args:
            filename: Name der zu löschenden Datei

        Returns:
            int: Anzahl gelöschter Chunks
        """
        logger.info(f"Lösche Dokument: {filename}")

        try:
            # Finde alle IDs für dieses Dokument
            results = self.collection.get(where={"filename": filename})

            if results["ids"]:
                self.collection.delete(ids=results["ids"])
                logger.info(f"{len(results['ids'])} Chunks gelöscht")
                return len(results["ids"])
            else:
                logger.warning(f"Keine Chunks für {filename} gefunden")
                return 0

        except Exception as e:
            logger.error(f"Fehler beim Löschen: {e}")
            raise

    def get_all_documents(self) -> list[str]:
        """Gibt eine Liste aller gespeicherten Dokumente zurück.

        Returns:
            list[str]: Liste von Dateinamen
        """
        try:
            results = self.collection.get()
            if results["metadatas"]:
                filenames = set(meta["filename"] for meta in results["metadatas"])
                return sorted(list(filenames))
            return []
        except Exception as e:
            logger.error(f"Fehler beim Abrufen der Dokumente: {e}")
            return []

    def get_document_count(self) -> int:
        """Gibt die Anzahl der Chunks in der Collection zurück.

        Returns:
            int: Anzahl der Chunks
        """
        try:
            return self.collection.count()
        except Exception as e:
            logger.error(f"Fehler beim Zählen: {e}")
            return 0

    def clear_collection(self) -> None:
        """Löscht alle Dokumente aus der Collection."""
        logger.warning("Lösche alle Dokumente aus der Collection")
        try:
            self.client.delete_collection(name=self.collection_name)
            self.collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"hnsw:space": "cosine"},
            )
            logger.info("Collection geleert")
        except Exception as e:
            logger.error(f"Fehler beim Leeren der Collection: {e}")
            raise

