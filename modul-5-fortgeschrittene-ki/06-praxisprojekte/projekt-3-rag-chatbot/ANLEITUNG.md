# 📚 Anleitung: RAG-ChatBot Projekt

## 🎯 Lernziele

In diesem Projekt lernst du:

- ✅ Wie man ein RAG-System (Retrieval-Augmented Generation) aufbaut
- ✅ PDF-Verarbeitung und Text-Extraktion
- ✅ Vector Databases und Embeddings
- ✅ Integration der Claude API
- ✅ Streaming-Responses in Streamlit
- ✅ Modulare Code-Architektur

## 📋 Voraussetzungen

### Technisch

- Python 3.11+
- UV Package Manager installiert
- Anthropic API Key ([hier erhalten](https://console.anthropic.com/))
- Grundkenntnisse in Python und Streamlit

### Zeitaufwand

- **Geführte Implementierung**: 2-3 Stunden
- **Selbstständige Umsetzung**: 4-6 Stunden

## 🚀 Schritt-für-Schritt Anleitung

### Phase 1: Setup (15 Min)

#### 1.1 Projektstruktur erstellen

```bash
cd modul-5-fortgeschrittene-ki/06-praxisprojekte/projekt-3-rag-chatbot
mkdir -p src data
```

#### 1.2 Dependencies installieren

```bash
uv sync
```

#### 1.3 Umgebungsvariablen konfigurieren

```bash
cp .env.example .env
# Bearbeite .env und füge deinen ANTHROPIC_API_KEY ein
```

### Phase 2: Config-Modul (20 Min)

**Datei**: `src/config.py`

**Aufgaben**:
1. Lade Umgebungsvariablen mit `python-dotenv`
2. Erstelle eine `Config`-Klasse mit allen Einstellungen
3. Definiere System-Prompt für Claude
4. Implementiere `get_user_prompt()` Funktion

**Wichtige Konzepte**:
- Umgebungsvariablen für sensible Daten
- Zentrale Konfiguration
- Type Hints für bessere Code-Qualität

### Phase 3: PDF-Processor (30 Min)

**Datei**: `src/pdf_processor.py`

**Aufgaben**:
1. Implementiere `extract_text_from_pdf()` mit PyMuPDF
2. Implementiere `chunk_text()` mit LangChain TextSplitter
3. Füge Metadaten hinzu (Seitenzahl, Dateiname, etc.)
4. Implementiere `validate_pdf_file()` für Input-Validierung

**Wichtige Konzepte**:
- PDF-Verarbeitung mit fitz (PyMuPDF)
- Text-Chunking für bessere Retrieval-Qualität
- Overlap zwischen Chunks für Kontext-Erhaltung
- Fehlerbehandlung und Validierung

**Tipp**: Teste mit einem kleinen PDF (5-10 Seiten)

### Phase 4: Vector Store (45 Min)

**Datei**: `src/vector_store.py`

**Aufgaben**:
1. Initialisiere ChromaDB Client
2. Implementiere `generate_embeddings()` mit sentence-transformers
3. Implementiere `add_documents()` zum Speichern
4. Implementiere `search()` für Similarity Search
5. Implementiere `delete_document()` und `get_all_documents()`

**Wichtige Konzepte**:
- Embeddings: Vektorrepräsentationen von Text
- Vector Database: Effiziente Ähnlichkeitssuche
- Cosine Similarity: Metrik für Textähnlichkeit
- Metadaten-Filterung

**Tipp**: Verwende `show_progress_bar=True` beim Embedding-Generieren

### Phase 5: LLM Handler (30 Min)

**Datei**: `src/llm_handler.py`

**Aufgaben**:
1. Initialisiere Anthropic Client
2. Implementiere `generate_response()` mit Standard- und Streaming-Modus
3. Implementiere `_generate_streaming_response()` für Echtzeit-Antworten
4. Implementiere `format_sources()` für Quellenangaben

**Wichtige Konzepte**:
- API-Integration mit Anthropic
- Streaming für bessere UX
- Prompt Engineering für RAG
- Fehlerbehandlung bei API-Aufrufen

**Tipp**: Teste zuerst ohne Streaming, dann mit Streaming

### Phase 6: Streamlit App (60 Min)

**Datei**: `app.py`

**Aufgaben**:
1. Implementiere `initialize_session_state()` für State-Management
2. Implementiere `process_uploaded_file()` für PDF-Upload
3. Implementiere `handle_user_question()` für Chat-Logik
4. Erstelle UI mit Sidebar und Chat-Interface
5. Füge Quellenangaben und Statistiken hinzu

**Wichtige Konzepte**:
- Streamlit Session State
- File Upload und Verarbeitung
- Chat-Interface mit `st.chat_message()`
- Streaming-Anzeige mit Placeholder
- Sidebar für Dokument-Verwaltung

**Tipp**: Teste jeden Teil einzeln, bevor du alles zusammenfügst

### Phase 7: Testing & Debugging (30 Min)

#### 7.1 Syntax-Check

```bash
uv run python -m py_compile app.py
uv run python -m py_compile src/*.py
```

#### 7.2 Linting

```bash
uv run ruff check .
uv run ruff check . --fix  # Automatische Fixes
```

#### 7.3 Funktionstest

```bash
uv run streamlit run app.py
```

**Test-Checkliste**:
- [ ] PDF-Upload funktioniert
- [ ] Dokument wird verarbeitet (Progress-Bar)
- [ ] Chunks werden in Vector DB gespeichert
- [ ] Fragen liefern relevante Antworten
- [ ] Quellenangaben sind korrekt
- [ ] Streaming funktioniert
- [ ] Dokumente können gelöscht werden
- [ ] Neue Session funktioniert

## 🎓 Erweiterte Übungen

### Übung 1: Multi-PDF Support

Erweitere die App, um mehrere PDFs gleichzeitig zu durchsuchen.

**Hinweise**:
- Füge Dateiname-Filter zur Suche hinzu
- Zeige in Quellenangaben, aus welchem Dokument die Info stammt

### Übung 2: Chat-Export

Implementiere einen Export-Button für Chat-Verläufe.

**Hinweise**:
- Verwende `st.download_button()`
- Format: Markdown oder JSON

### Übung 3: Conversation Memory

Füge Kontext über mehrere Fragen hinzu.

**Hinweise**:
- Speichere letzte N Fragen/Antworten
- Füge zum Prompt hinzu

### Übung 4: OCR-Support

Unterstütze gescannte PDFs mit OCR.

**Hinweise**:
- Verwende `pytesseract` oder `easyocr`
- Erkenne automatisch, ob OCR nötig ist

## 🐛 Häufige Fehler

### Import-Fehler

```python
ModuleNotFoundError: No module named 'src'
```

**Lösung**: Stelle sicher, dass du im richtigen Verzeichnis bist und `uv sync` ausgeführt hast.

### API-Key Fehler

```
ValueError: ANTHROPIC_API_KEY fehlt
```

**Lösung**: Prüfe, ob `.env`-Datei existiert und API-Key korrekt ist.

### ChromaDB Fehler

```
Error: Collection already exists
```

**Lösung**: Lösche `data/chroma_db/` Verzeichnis oder verwende `get_or_create_collection()`.

### Embedding-Fehler

```
RuntimeError: CUDA out of memory
```

**Lösung**: Verwende kleineres Embedding-Modell oder reduziere Batch-Size.

## 📚 Zusätzliche Ressourcen

- [Anthropic API Docs](https://docs.anthropic.com/)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [Streamlit Docs](https://docs.streamlit.io/)

## 💡 Best Practices

1. **Modularer Code**: Trenne Logik in separate Module
2. **Type Hints**: Verwende Type Annotations
3. **Logging**: Logge wichtige Ereignisse
4. **Fehlerbehandlung**: Fange Exceptions ab
5. **Dokumentation**: Schreibe Docstrings
6. **Testing**: Teste mit verschiedenen PDFs

## 🎉 Abschluss

Wenn du alle Schritte abgeschlossen hast, hast du ein vollständiges RAG-System gebaut! 

**Nächste Schritte**:
- Experimentiere mit verschiedenen PDFs
- Passe Chunk-Größe und Overlap an
- Teste verschiedene Embedding-Modelle
- Optimiere Prompts für bessere Antworten

Viel Erfolg! 🚀

