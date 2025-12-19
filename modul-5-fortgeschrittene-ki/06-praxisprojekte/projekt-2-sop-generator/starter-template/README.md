# 📄 SOP-Generator

Eine Streamlit-App zum Erstellen von formatierten Standard Operating Procedures (SOPs) aus Word-Dokumenten.

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

- [ ] Word-Dokument hochladen
- [ ] Dokument-Inhalt extrahieren
- [ ] SOP-Metadaten eingeben (Titel, Version, Autor, Datum)
- [ ] Formatierte SOP generieren
- [ ] SOP als Word-Dokument herunterladen
- [ ] Vorschau des generierten Dokuments

## 🛠️ Technologien

- **Python 3.11+**
- **Streamlit** - Web-Framework
- **python-docx** - Word-Dokumente lesen/schreiben
- **Pandas** - Datenverarbeitung (optional)

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

## 📖 Anleitung

Folgen Sie der [Schritt-für-Schritt Anleitung](../ANLEITUNG.md) um die App zu entwickeln.

## 🎯 Nächste Schritte

1. Öffnen Sie `app.py` und beginnen Sie mit Iteration 1
2. Folgen Sie der ANLEITUNG.md
3. Testen Sie nach jedem Schritt
4. Committen Sie regelmässig!

---

**Viel Erfolg! 🎉**

