# 📄 Projekt 2: SOP-Generator

Eine **Streamlit-App**, die ein Word-Dokument hochlädt, verarbeitet und als formatierte Standard Operating Procedure (SOP) wieder ausgibt.

## 🎯 Lernziele

Nach diesem Projekt können Sie:

- ✅ File-Upload in Streamlit implementieren
- ✅ Word-Dokumente lesen und schreiben (python-docx)
- ✅ Textverarbeitung und Formatierung
- ✅ File-Download in Streamlit anbieten
- ✅ Formulare für Benutzer-Input erstellen

## 📸 Konzept

```
┌─────────────────────────────────────┐
│ 📄 SOP Generator                    │
├─────────────────────────────────────┤
│ 1. Word-Dokument hochladen          │
│    [Datei auswählen...]             │
│                                     │
│ 2. SOP-Informationen eingeben       │
│    Titel:     [________________]    │
│    Version:   [____]                │
│    Autor:     [________________]    │
│    Datum:     [__________]          │
│                                     │
│ 3. SOP generieren                   │
│    [SOP erstellen]                  │
│                                     │
│ 4. Download                         │
│    [📥 SOP herunterladen]           │
└─────────────────────────────────────┘
```

## 🚀 Schnellstart

### Installation

```bash
# Dependencies installieren
uv sync --all-extras

# App starten
uv run streamlit run app.py
```

## 📁 Projektstruktur

```
projekt-2-sop-generator/
├── README.md
├── ANLEITUNG.md
├── starter-template/
│   ├── .gitignore
│   ├── pyproject.toml
│   ├── README.md
│   ├── app.py
│   └── templates/
│       └── sop_template.docx
└── musterloesung/
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── app.py
    └── templates/
        └── sop_template.docx
```

## 📋 Anforderungen

### Muss-Kriterien

- [ ] **File-Upload:** Word-Dokument hochladen
- [ ] **Dokument lesen:** Inhalt extrahieren
- [ ] **Formular:** SOP-Metadaten eingeben (Titel, Version, Autor, Datum)
- [ ] **SOP generieren:** Formatiertes Dokument erstellen
- [ ] **Download:** SOP als Word-Dokument herunterladen

### Soll-Kriterien

- [ ] **Vorschau:** Inhalt vor Download anzeigen
- [ ] **Template:** Vordefiniertes SOP-Template verwenden
- [ ] **Validierung:** Pflichtfelder prüfen
- [ ] **Formatierung:** Überschriften, Listen, Nummerierung

### Kann-Kriterien

- [ ] **Mehrere Formate:** PDF-Export
- [ ] **Versionierung:** Automatische Versionsnummer
- [ ] **Genehmigung:** Genehmigungsworkflow
- [ ] **Archiv:** Alte Versionen speichern

## 🛠️ Technologien

- **Python 3.11+**
- **Streamlit** - Web-Framework
- **python-docx** - Word-Dokumente lesen/schreiben
- **Pandas** (optional) - Datenverarbeitung

## 📚 Ressourcen

### Dokumentation

- [Streamlit File Upload](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
- [Streamlit Download Button](https://docs.streamlit.io/library/api-reference/widgets/st.download_button)
- [python-docx Docs](https://python-docx.readthedocs.io/)

### Tutorials

- [python-docx Quickstart](https://python-docx.readthedocs.io/en/latest/user/quickstart.html)

## 🎯 Nächste Schritte

1. **ANLEITUNG.md lesen**
2. **Starter-Template verwenden**
3. **Schritt für Schritt umsetzen**
4. **Mit Musterlösung vergleichen**

---

**Los geht's!** 🚀

👉 [Zur Schritt-für-Schritt Anleitung](./ANLEITUNG.md)

