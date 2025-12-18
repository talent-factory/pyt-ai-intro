# RAG-ChatBot mit Streamlit - Entwicklungsauftrag

## Projektziel
Entwickle eine produktionsreife Streamlit-Anwendung, die es Nutzern ermöglicht, PDF-Dokumente hochzuladen und mittels Retrieval-Augmented Generation (RAG) mit deren Inhalt zu interagieren.

## Technische Anforderungen

### Tech-Stack
- **Frontend/UI**: Streamlit (neueste stabile Version)
- **LLM-Integration**: Anthropic Claude API (empfohlen: Claude 3.5 Sonnet)
- **Vector Database**:  ChromaDB (für lokale Entwicklung/kleinere Projekte)
- **Embeddings**: Verwende sentence-transformers (z.B. all-MiniLM-L6-v2) oder OpenAI Embeddings
- **PDF-Verarbeitung**: pymupdf (fitz)
- **Chunking**: LangChain TextSplitter oder ähnliche Lösung

### Python-Abhängigkeiten
Verwende 'uv' für alle notwendigen Pakete inklusive Versionsangaben.

## Funktionale Anforderungen

### 1. PDF-Upload
- Implementiere einen Drag & Drop Bereich für PDF-Dateien
- Unterstütze auch den klassischen Datei-Browser-Upload als Fallback
- Validierung: Nur PDF-Dateien erlauben (max. 50 MB)
- Zeige Upload-Fortschritt und Status-Feedback
- Ermögliche das Hochladen mehrerer PDFs nacheinander

### 2. Dokumentenverarbeitung
- **Text-Extraktion**: Extrahiere vollständigen Text aus dem PDF
- **Text-Chunking**: 
  - Chunk-Größe: ~500-1000 Tokens
  - Overlap: 100-200 Tokens
  - Behalte Kontext über Chunk-Grenzen hinweg
- **Embedding-Generierung**: Erstelle Vektorrepräsentationen für jeden Chunk
- **Vector Store**: Speichere Embeddings mit Metadaten (Seitenzahl, Dateiname, Chunk-Index)
- Zeige Verarbeitungs-Status mit Progress-Bar

### 3. Chat-Interface
- **Chat-UI**: 
  - Übersichtlicher Chat-Verlauf (User/Assistant Messages)
  - Eingabefeld für User-Fragen
  - Chat-History persistieren während der Session
- **Retrieval**: 
  - Suche die Top-K relevantesten Chunks (K=3-5)
  - Verwende Similarity Search mit konfigurierbarem Threshold
- **Response-Generierung**:
  - Sende relevante Chunks als Kontext an Claude API
  - Generiere präzise, quellenbasierte Antworten
  - Zeige verwendete Quellen (Seite, Relevanz-Score) unter der Antwort
- **Streaming**: Implementiere Streaming-Responses für bessere UX

### 4. Zusätzliche Features
- **Session-Management**: 
  - Möglichkeit, neue Chat-Session zu starten
  - Upload-Historie anzeigen
- **Quellenangaben**: Zeige bei jeder Antwort, aus welchen PDF-Abschnitten die Information stammt
- **Lösch-Funktion**: Ermögliche das Löschen einzelner Dokumente aus der Vector DB

## Nicht-funktionale Anforderungen

### Performance
- PDF-Verarbeitung soll für 100-seitige Dokumente unter 30 Sekunden dauern
- Chat-Antworten (ohne Streaming) in unter 5 Sekunden
- Effizientes Caching für wiederholte Anfragen

### Benutzererfahrung
- Intuitive, selbsterklärende Benutzeroberfläche
- Klare Fehlermeldungen und Hinweise
- Loading-Indicators für alle asynchronen Operationen
- Responsive Design (funktioniert auf Desktop und Tablet)

### Code-Qualität
- Clean Code Prinzipien
- Modulare Struktur (separate Module für: PDF-Processing, Vector-Store, LLM-Integration, UI)
- Typ-Annotationen (Type Hints)
- Docstrings für alle Funktionen
- Fehlerbehandlung (try-except mit aussagekräftigen Fehlermeldungen)
- Logging für Debugging

### Sicherheit
- API-Keys über Environment-Variablen (.env-Datei)
- Input-Validierung für alle User-Inputs
- Rate-Limiting berücksichtigen

## Projektstruktur (Vorschlag)
```
rag-chatbot/
├── app.py                # Hauptanwendung (Streamlit)
├── .env.example          # Beispiel für Umgebungsvariablen
├── .gitignore
├── README.md             # Dokumentation
└── src/
    ├── __init__.py
    ├── pdf_processor.py  # PDF-Extraktion & Chunking
    ├── vector_store.py   # Vector DB Operationen
    ├── llm_handler.py    # Claude API Integration
    └── config.py         # Konfigurationen & Konstanten
```

## Implementierungs-Schritte

1. **Setup**: Projektstruktur erstellen, Dependencies installieren
2. **PDF-Processing**: Text-Extraktion und Chunking implementieren
3. **Vector Store**: Embedding-Generierung und Speicherung
4. **LLM-Integration**: Claude API anbinden mit RAG-Prompt
5. **UI**: Streamlit Interface mit allen Features
6. **Testing**: Funktionalität mit verschiedenen PDFs testen
7. **Optimization**: Performance-Tuning und UX-Verbesserungen

## Akzeptanzkriterien

- [ ] PDF-Upload funktioniert via Drag & Drop und File-Browser
- [ ] Dokumente werden korrekt verarbeitet und in Vector DB gespeichert
- [ ] Chat liefert relevante, quellenbasierte Antworten
- [ ] Quellenangaben sind präzise (Seite, Text-Snippet)
- [ ] Alle Features sind intuitiv bedienbar
- [ ] Code ist sauber strukturiert und dokumentiert
- [ ] README enthält Setup- und Nutzungsanleitung
- [ ] Fehlerfälle werden graceful behandelt

## Beispiel-Prompt für Claude API
```python
system_prompt = """Du bist ein hilfreicher Assistent, der Fragen zu hochgeladenen 
PDF-Dokumenten beantwortet. Basiere deine Antworten ausschließlich auf dem 
bereitgestellten Kontext. Falls die Information nicht im Kontext enthalten ist, 
sage dies deutlich."""

user_prompt = f"""
Kontext aus dem Dokument:
{retrieved_chunks}

Frage: {user_question}

Beantworte die Frage präzise basierend auf dem Kontext. Gib wenn möglich 
Seitenzahlen an.
"""
```

## Nice-to-Have Features (Optional)

- Multi-PDF Support (mehrere PDFs gleichzeitig durchsuchbar)
- Export von Chat-Verläufen
- Syntax-Highlighting für Code-Snippets in PDFs
- OCR-Support für gescannte PDFs
- Unterstützung weiterer Dateiformate (DOCX, TXT)
- Conversation Memory (Kontext über mehrere Fragen hinweg)

## Lieferumfang

1. Vollständiger, lauffähiger Code
2. requirements.txt
3. .env.example mit benötigten API-Keys
4. README.md mit:
   - Setup-Anleitung
   - Nutzungsanleitung
   - Architektur-Übersicht
   - Troubleshooting
5. Beispiel-PDF zum Testen

---

**Hinweis**: Verwende best practices für RAG-Systeme und achte auf gute Prompt-Engineering-Techniken für optimale Ergebnisse.
