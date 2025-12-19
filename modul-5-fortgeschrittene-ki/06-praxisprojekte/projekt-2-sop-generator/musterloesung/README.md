# 📄 SOP-Generator - Musterlösung

Eine vollständige Streamlit-App zum Erstellen von formatierten Standard Operating Procedures (SOPs) aus Word-Dokumenten.

## 🚀 Schnellstart

### Installation

```bash
# Dependencies installieren
uv sync --all-extras

# App starten
uv run streamlit run app.py
```

Die App öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📋 Features

- ✅ Word-Dokument hochladen
- ✅ Dokument-Inhalt extrahieren
- ✅ SOP-Metadaten eingeben (Titel, Version, Autor, Datum)
- ✅ Formatierte SOP generieren
- ✅ SOP als Word-Dokument herunterladen
- ✅ Vorschau des generierten Dokuments

## 🛠️ Technologien

- **Python 3.11+**
- **Streamlit** - Web-Framework
- **python-docx** - Word-Dokumente lesen/schreiben
- **Pandas** - Datenverarbeitung

## 📁 Projektstruktur

```
sop-generator/
├── .gitignore
├── pyproject.toml
├── README.md
├── app.py              # Hauptdatei (Streamlit App)
└── templates/          # SOP-Templates
    └── sop_template.docx
```

## 🎯 Verwendung

1. **Dokument hochladen:** Laden Sie ein Word-Dokument mit dem Inhalt hoch
2. **Metadaten eingeben:** Füllen Sie Titel, Version, Autor und Datum aus
3. **SOP generieren:** Klicken Sie auf "SOP erstellen"
4. **Download:** Laden Sie die formatierte SOP herunter

## 📚 Code-Struktur

### Hauptfunktionen

- `read_docx(file)` - Liest ein Word-Dokument und extrahiert den Inhalt
- `create_sop(content, metadata)` - Erstellt ein formatiertes SOP-Dokument
- `add_header(doc, metadata)` - Fügt den SOP-Header hinzu
- `add_content(doc, content)` - Fügt den Hauptinhalt hinzu

## 🔧 Anpassungen

Sie können die SOP-Formatierung in der `create_sop()` Funktion anpassen:

- Schriftarten und -grössen
- Überschriften-Stile
- Nummerierung
- Farben und Layout

---

**Viel Erfolg! 🎉**

