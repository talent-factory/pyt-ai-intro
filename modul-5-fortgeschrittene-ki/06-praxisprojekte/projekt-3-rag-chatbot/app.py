"""RAG-ChatBot Streamlit Anwendung.

Eine Streamlit-App für Retrieval-Augmented Generation mit PDF-Dokumenten.
"""

import logging

import streamlit as st

from src.config import Config
from src.llm_handler import LLMHandler, format_sources
from src.pdf_processor import PDFProcessor, validate_pdf_file
from src.vector_store import VectorStore

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Seitenkonfiguration
st.set_page_config(
    page_title="RAG-ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)


def initialize_session_state() -> None:
    """Initialisiert den Session State."""
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None

    if "llm_handler" not in st.session_state:
        st.session_state.llm_handler = None

    if "pdf_processor" not in st.session_state:
        st.session_state.pdf_processor = PDFProcessor()

    if "uploaded_files" not in st.session_state:
        st.session_state.uploaded_files = []


def initialize_components() -> tuple[bool, str]:
    """Initialisiert Vector Store und LLM Handler.

    Returns:
        tuple[bool, str]: (erfolg, fehlermeldung)
    """
    # Validiere Konfiguration
    if not Config.validate():
        return False, "❌ ANTHROPIC_API_KEY fehlt. Bitte in .env-Datei setzen."

    try:
        # Initialisiere Vector Store
        if st.session_state.vector_store is None:
            st.session_state.vector_store = VectorStore()

        # Initialisiere LLM Handler
        if st.session_state.llm_handler is None:
            st.session_state.llm_handler = LLMHandler()

        return True, ""

    except Exception as e:
        return False, f"❌ Fehler bei Initialisierung: {str(e)}"


def process_uploaded_file(uploaded_file) -> tuple[bool, str]:
    """Verarbeitet eine hochgeladene PDF-Datei.

    Args:
        uploaded_file: Streamlit UploadedFile Objekt

    Returns:
        tuple[bool, str]: (erfolg, nachricht)
    """
    try:
        # Speichere temporär
        temp_path = Config.DATA_DIR / uploaded_file.name
        temp_path.write_bytes(uploaded_file.getvalue())

        # Validiere PDF
        is_valid, error_msg = validate_pdf_file(temp_path)
        if not is_valid:
            temp_path.unlink()
            return False, f"❌ {error_msg}"

        # Verarbeite PDF
        with st.spinner(f"Verarbeite {uploaded_file.name}..."):
            chunks = st.session_state.pdf_processor.process_pdf(temp_path)

            # Füge zu Vector Store hinzu
            num_chunks = st.session_state.vector_store.add_documents(chunks)

        # Lösche temporäre Datei
        temp_path.unlink()

        # Merke hochgeladene Datei
        if uploaded_file.name not in st.session_state.uploaded_files:
            st.session_state.uploaded_files.append(uploaded_file.name)

        return True, f"✅ {uploaded_file.name} erfolgreich verarbeitet ({num_chunks} Chunks)"

    except Exception as e:
        logger.error(f"Fehler bei Verarbeitung: {e}")
        return False, f"❌ Fehler: {str(e)}"


def display_chat_message(role: str, content: str, sources: str | None = None) -> None:
    """Zeigt eine Chat-Nachricht an.

    Args:
        role: "user" oder "assistant"
        content: Nachrichteninhalt
        sources: Optional Quellenangaben
    """
    with st.chat_message(role):
        st.markdown(content)
        if sources:
            with st.expander("📚 Quellen"):
                st.markdown(sources)


def handle_user_question(question: str) -> None:
    """Verarbeitet eine Benutzerfrage.

    Args:
        question: Frage des Benutzers
    """
    # Füge User-Nachricht hinzu
    st.session_state.messages.append({"role": "user", "content": question})

    # Zeige User-Nachricht
    display_chat_message("user", question)

    # Suche relevante Chunks
    with st.spinner("Suche relevante Informationen..."):
        retrieved_chunks = st.session_state.vector_store.search(question)

    if not retrieved_chunks:
        response = "Ich konnte keine relevanten Informationen in den Dokumenten finden."
        sources = None
    else:
        # Generiere Antwort mit Streaming
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            full_response = ""

            for chunk in st.session_state.llm_handler.generate_response(
                question, retrieved_chunks, stream=True
            ):
                full_response += chunk
                message_placeholder.markdown(full_response + "▌")

            message_placeholder.markdown(full_response)

            # Zeige Quellen
            sources = format_sources(retrieved_chunks)
            with st.expander("📚 Quellen"):
                st.markdown(sources)

        response = full_response

    # Speichere Assistant-Nachricht
    st.session_state.messages.append(
        {"role": "assistant", "content": response, "sources": sources}
    )


def main() -> None:
    """Hauptfunktion der Streamlit-App."""
    initialize_session_state()

    # Titel
    st.title("🤖 RAG-ChatBot")
    st.markdown("Stelle Fragen zu deinen PDF-Dokumenten")

    # Initialisiere Komponenten
    success, error_msg = initialize_components()
    if not success:
        st.error(error_msg)
        st.info("💡 Erstelle eine `.env`-Datei mit deinem ANTHROPIC_API_KEY")
        st.stop()

    # Sidebar
    with st.sidebar:
        st.header("📄 Dokumente")

        # File Upload
        uploaded_file = st.file_uploader(
            "PDF hochladen",
            type=["pdf"],
            help=f"Maximale Dateigrösse: {Config.MAX_FILE_SIZE_MB} MB",
        )

        if uploaded_file:
            if st.button("Verarbeiten", type="primary"):
                success, message = process_uploaded_file(uploaded_file)
                if success:
                    st.success(message)
                else:
                    st.error(message)

        # Zeige hochgeladene Dokumente
        st.subheader("Hochgeladene Dokumente")
        if st.session_state.uploaded_files:
            for filename in st.session_state.uploaded_files:
                col1, col2 = st.columns([3, 1])
                col1.write(f"📄 {filename}")
                if col2.button("🗑️", key=f"delete_{filename}"):
                    st.session_state.vector_store.delete_document(filename)
                    st.session_state.uploaded_files.remove(filename)
                    st.rerun()
        else:
            st.info("Noch keine Dokumente hochgeladen")

        # Statistiken
        st.divider()
        st.subheader("📊 Statistiken")
        chunk_count = st.session_state.vector_store.get_document_count()
        st.metric("Chunks in DB", chunk_count)

        # Neue Session
        if st.button("🔄 Neue Chat-Session"):
            st.session_state.messages = []
            st.rerun()

    # Chat-Interface
    st.divider()

    # Zeige Chat-Historie
    for message in st.session_state.messages:
        display_chat_message(
            message["role"],
            message["content"],
            message.get("sources"),
        )

    # Chat-Input
    if question := st.chat_input("Stelle eine Frage zu deinen Dokumenten..."):
        if not st.session_state.uploaded_files:
            st.warning("⚠️ Bitte lade zuerst ein PDF-Dokument hoch")
        else:
            handle_user_question(question)


if __name__ == "__main__":
    main()

