# 🤖 RAG-ChatBot mit Streamlit

Ein produktionsreifer RAG (Retrieval-Augmented Generation) ChatBot, der es ermöglicht, PDF-Dokumente hochzuladen und mittels Claude API mit deren Inhalt zu interagieren.

## 🎯 Features

- **PDF-Upload**: Drag & Drop oder File-Browser für PDF-Dateien (max. 50 MB)
- **Intelligente Verarbeitung**: Automatische Text-Extraktion und Chunking
- **Vector Search**: ChromaDB für schnelle Ähnlichkeitssuche
- **Claude Integration**: Streaming-Antworten mit Claude 3.5 Sonnet
- **Quellenangaben**: Präzise Referenzen mit Seitenzahlen und Relevanz-Scores
- **Session-Management**: Chat-Historie und Dokument-Verwaltung
- **Intuitive UI**: Übersichtliches Streamlit-Interface

## 🏗️ Architektur

```
rag-chatbot/
├── app.py                    # Streamlit Hauptanwendung
├── src/
│   ├── __init__.py
│   ├── config.py             # Konfigurationen & Konstanten
│   ├── pdf_processor.py      # PDF-Extraktion & Chunking
│   ├── vector_store.py       # ChromaDB Integration
│   └── llm_handler.py        # Claude API Integration
├── data/
│   └── chroma_db/            # Vector Database (wird erstellt)
├── .env                      # Umgebungsvariablen (nicht im Repo)
├── .env.example              # Beispiel für .env
├── .gitignore
├── pyproject.toml            # Dependencies
└── README.md
```

## 🚀 Setup

### 1. Voraussetzungen

- Python 3.11 oder höher
- UV Package Manager
- Anthropic API Key ([hier erhalten](https://console.anthropic.com/))

### 2. Installation

```bash
# Repository klonen (falls noch nicht geschehen)
cd modul-5-fortgeschrittene-ki/06-praxisprojekte/projekt-3-rag-chatbot

# Dependencies installieren
uv sync

# .env-Datei erstellen
cp .env.example .env
```

### 3. Konfiguration

Bearbeite die `.env`-Datei und füge deinen API-Key ein:

```bash
ANTHROPIC_API_KEY=dein_api_key_hier
```

Optional kannst du weitere Einstellungen anpassen:

```bash
# LLM-Einstellungen
LLM_MODEL=claude-3-5-sonnet-20241022
LLM_MAX_TOKENS=4096
LLM_TEMPERATURE=0.7

# Chunking-Einstellungen
CHUNK_SIZE=1000
CHUNK_OVERLAP=200

# Retrieval-Einstellungen
TOP_K_RESULTS=5
SIMILARITY_THRESHOLD=0.7
```

### 4. Anwendung starten

```bash
uv run streamlit run app.py
```

Die App öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📖 Nutzung

### PDF hochladen

1. Klicke in der Sidebar auf "PDF hochladen"
2. Wähle eine PDF-Datei aus (max. 50 MB)
3. Klicke auf "Verarbeiten"
4. Warte, bis die Verarbeitung abgeschlossen ist

### Fragen stellen

1. Gib deine Frage im Chat-Eingabefeld ein
2. Die App sucht automatisch relevante Textabschnitte
3. Claude generiert eine Antwort basierend auf den Dokumenten
4. Klicke auf "📚 Quellen" um die verwendeten Textabschnitte zu sehen

### Dokumente verwalten

- **Löschen**: Klicke auf 🗑️ neben einem Dokument
- **Neue Session**: Klicke auf "🔄 Neue Chat-Session" um den Chat zu leeren
- **Statistiken**: Sieh die Anzahl der gespeicherten Chunks

## 🔧 Technische Details

### PDF-Verarbeitung

- **Text-Extraktion**: PyMuPDF (fitz) für robuste PDF-Verarbeitung
- **Chunking**: LangChain RecursiveCharacterTextSplitter
  - Chunk-Größe: 1000 Zeichen
  - Overlap: 200 Zeichen
  - Erhält Kontext über Chunk-Grenzen hinweg

### Embeddings & Vector Store

- **Embedding-Modell**: sentence-transformers/all-MiniLM-L6-v2
  - Schnell und effizient
  - 384-dimensionale Vektoren
- **Vector Database**: ChromaDB
  - Persistente Speicherung
  - Cosine Similarity Search
  - Metadaten-Filterung

### LLM Integration

- **Modell**: Claude 3.5 Sonnet
- **Streaming**: Echtzeit-Antworten für bessere UX
- **Prompt Engineering**: Optimiert für quellenbasierte Antworten
- **Fehlerbehandlung**: Graceful Degradation bei API-Fehlern

## 🐛 Troubleshooting

### API-Key Fehler

```
❌ ANTHROPIC_API_KEY fehlt
```

**Lösung**: Erstelle eine `.env`-Datei mit deinem API-Key

### PDF kann nicht verarbeitet werden

```
❌ PDF kann nicht geöffnet werden
```

**Mögliche Ursachen**:
- PDF ist beschädigt
- PDF ist passwortgeschützt
- PDF ist zu gross (>50 MB)

**Lösung**: Verwende ein anderes PDF oder reduziere die Dateigrösse

### Keine relevanten Informationen gefunden

```
Ich konnte keine relevanten Informationen in den Dokumenten finden.
```

**Mögliche Ursachen**:
- Frage ist zu spezifisch
- Information ist nicht im Dokument
- Similarity-Threshold ist zu hoch

**Lösung**: 
- Formuliere die Frage allgemeiner
- Passe `SIMILARITY_THRESHOLD` in `.env` an (z.B. 0.5)

### ChromaDB Fehler

```
Error: Could not connect to ChromaDB
```

**Lösung**: Lösche das `data/chroma_db/` Verzeichnis und starte neu

## 🧪 Testing

```bash
# Syntax-Check
uv run python -m py_compile app.py
uv run python -m py_compile src/*.py

# Linting
uv run ruff check .

# Type-Checking
uv run mypy src/
```

## 📚 Verwendete Technologien

- **Streamlit**: Web-Framework für Data Apps
- **Anthropic Claude**: Large Language Model
- **ChromaDB**: Vector Database
- **Sentence Transformers**: Embedding-Generierung
- **PyMuPDF**: PDF-Verarbeitung
- **LangChain**: Text-Splitting

## 🔐 Sicherheit

- API-Keys werden über Umgebungsvariablen verwaltet
- `.env`-Datei ist in `.gitignore` ausgeschlossen
- Input-Validierung für alle User-Inputs
- Dateigrössen-Limits

## 📝 Lizenz

Dieses Projekt ist Teil des Python AI Intro Kurses.

## 🤝 Beitragen

Feedback und Verbesserungsvorschläge sind willkommen!

