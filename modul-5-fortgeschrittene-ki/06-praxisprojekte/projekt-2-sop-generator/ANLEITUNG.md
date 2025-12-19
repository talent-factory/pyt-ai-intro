# 📖 Schritt-für-Schritt Anleitung: SOP-Generator

Diese Anleitung führt Sie durch die Entwicklung eines **SOP-Generators** mit Streamlit.

## 🎯 Überblick

Wir entwickeln die App in **4 Iterationen**:

1. **Setup & File-Upload** - Dokument hochladen
2. **Dokument lesen** - Inhalt extrahieren
3. **SOP generieren** - Formatiertes Dokument erstellen
4. **Download** - SOP herunterladen

**Dauer:** 1-2 Stunden

---

## 🚀 Iteration 1: Setup & File-Upload

**Ziel:** Projekt aufsetzen und File-Upload implementieren

**Dauer:** 20 Minuten

### Schritt 1.1: Projekt initialisieren

```bash
# Repository erstellen (oder Starter-Template verwenden)
mkdir sop-generator
cd sop-generator

# UV initialisieren
uv init
uv python pin 3.11

# Ordner erstellen
mkdir templates
touch app.py
```

### Schritt 1.2: Dependencies hinzufügen

`pyproject.toml`:

```toml
[project]
name = "sop-generator"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "streamlit>=1.28.0",
    "python-docx>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.0",
]
```

```bash
uv sync --all-extras
```

### Schritt 1.3: Minimale App mit File-Upload

`app.py`:

```python
"""SOP-Generator mit Streamlit."""

import streamlit as st
from docx import Document
import io

# Seitenkonfiguration
st.set_page_config(
    page_title="SOP Generator",
    page_icon="📄",
    layout="centered",
)

# Titel
st.title("📄 SOP Generator")
st.write("Erstellen Sie professionelle SOPs aus Word-Dokumenten")

# File-Upload
st.header("1. Dokument hochladen")
uploaded_file = st.file_uploader(
    "Word-Dokument auswählen",
    type=["docx"],
    help="Laden Sie ein Word-Dokument (.docx) hoch"
)

if uploaded_file:
    st.success(f"✅ Datei '{uploaded_file.name}' hochgeladen!")
    st.info(f"Dateigrösse: {uploaded_file.size} Bytes")
else:
    st.info("👆 Bitte laden Sie ein Word-Dokument hoch")
```

### Schritt 1.4: Testen

```bash
uv run streamlit run app.py
```

**Prüfen:**
- File-Upload funktioniert
- Dateiname wird angezeigt
- Dateigrösse wird angezeigt

### Schritt 1.5: Commit

```bash
git add .
git commit -m "🎉 init: Initialisiere SOP-Generator mit File-Upload"
```

---

## 📖 Iteration 2: Dokument lesen

**Ziel:** Inhalt aus Word-Dokument extrahieren

**Dauer:** 20 Minuten

### Schritt 2.1: Dokument-Inhalt anzeigen

Erweitern Sie `app.py`:

```python
if uploaded_file:
    st.success(f"✅ Datei '{uploaded_file.name}' hochgeladen!")
    
    # Dokument lesen
    doc = Document(uploaded_file)
    
    # Inhalt extrahieren
    st.header("2. Dokument-Inhalt")
    
    with st.expander("📄 Vorschau", expanded=True):
        # Absätze anzeigen
        for i, para in enumerate(doc.paragraphs):
            if para.text.strip():  # Nur nicht-leere Absätze
                st.write(f"{i+1}. {para.text}")
    
    # Statistiken
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Absätze", len(doc.paragraphs))
    with col2:
        word_count = sum(len(p.text.split()) for p in doc.paragraphs)
        st.metric("Wörter", word_count)
```

### Schritt 2.2: Testen

```bash
# Erstellen Sie ein Test-Dokument in Word mit etwas Text
# Laden Sie es hoch
# Prüfen: Inhalt wird angezeigt
```

### Schritt 2.3: Commit

```bash
git commit -am "✨ feat: Füge Dokument-Lese-Funktion hinzu"
```

---

## 📝 Iteration 3: SOP generieren

**Ziel:** Formatiertes SOP-Dokument erstellen

**Dauer:** 30 Minuten

### Schritt 3.1: SOP-Formular hinzufügen

Fügen Sie nach dem Dokument-Inhalt hinzu:

```python
    # SOP-Metadaten
    st.header("3. SOP-Informationen")
    
    with st.form("sop_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            sop_title = st.text_input("SOP-Titel*", placeholder="z.B. Kundenbetreuung")
            sop_version = st.text_input("Version*", value="1.0")
        
        with col2:
            sop_author = st.text_input("Autor*", placeholder="Ihr Name")
            sop_date = st.date_input("Datum")
        
        sop_description = st.text_area(
            "Beschreibung",
            placeholder="Kurze Beschreibung der SOP..."
        )
        
        submitted = st.form_submit_button("SOP generieren")
        
        if submitted:
            if not sop_title or not sop_version or not sop_author:
                st.error("Bitte füllen Sie alle Pflichtfelder aus!")
            else:
                # SOP generieren (nächster Schritt)
                st.success("✅ SOP wird generiert...")
```

### Schritt 3.2: SOP-Generierungs-Funktion

Fügen Sie vor der Streamlit-App hinzu:

```python
def create_sop(original_doc, title, version, author, date, description):
    """Erstellt ein formatiertes SOP-Dokument.
    
    Args:
        original_doc: Original Word-Dokument
        title: SOP-Titel
        version: Version
        author: Autor
        date: Datum
        description: Beschreibung
        
    Returns:
        Document: Formatiertes SOP-Dokument
    """
    # Neues Dokument erstellen
    sop_doc = Document()
    
    # Titel
    sop_doc.add_heading("Standard Operating Procedure", 0)
    sop_doc.add_heading(title, 1)
    
    # Metadaten-Tabelle
    table = sop_doc.add_table(rows=4, cols=2)
    table.style = 'Light Grid Accent 1'
    
    # Zeile 1: Version
    table.rows[0].cells[0].text = "Version:"
    table.rows[0].cells[1].text = version
    
    # Zeile 2: Autor
    table.rows[1].cells[0].text = "Autor:"
    table.rows[1].cells[1].text = author
    
    # Zeile 3: Datum
    table.rows[2].cells[0].text = "Datum:"
    table.rows[2].cells[1].text = str(date)
    
    # Zeile 4: Status
    table.rows[3].cells[0].text = "Status:"
    table.rows[3].cells[1].text = "Entwurf"
    
    # Leerzeile
    sop_doc.add_paragraph()
    
    # Beschreibung
    if description:
        sop_doc.add_heading("Beschreibung", 2)
        sop_doc.add_paragraph(description)
    
    # Original-Inhalt
    sop_doc.add_heading("Inhalt", 2)
    
    # Absätze aus Original-Dokument kopieren
    for para in original_doc.paragraphs:
        if para.text.strip():
            sop_doc.add_paragraph(para.text, style=para.style.name)
    
    return sop_doc
```

### Schritt 3.3: SOP generieren und speichern

Ändern Sie den `if submitted:` Block:

```python
        if submitted:
            if not sop_title or not sop_version or not sop_author:
                st.error("Bitte füllen Sie alle Pflichtfelder aus!")
            else:
                # SOP generieren
                with st.spinner("Generiere SOP..."):
                    sop_doc = create_sop(
                        doc, sop_title, sop_version, 
                        sop_author, sop_date, sop_description
                    )
                
                # In Session State speichern
                st.session_state['sop_doc'] = sop_doc
                st.session_state['sop_title'] = sop_title
                
                st.success("✅ SOP erfolgreich generiert!")
```

### Schritt 3.4: Testen

```bash
# Dokument hochladen
# Formular ausfüllen
# "SOP generieren" klicken
# Prüfen: Erfolgsmeldung erscheint
```

### Schritt 3.5: Commit

```bash
git commit -am "✨ feat: Implementiere SOP-Generierung"
```

---

## 📥 Iteration 4: Download

**Ziel:** SOP als Word-Dokument herunterladen

**Dauer:** 15 Minuten

### Schritt 4.1: Download-Button hinzufügen

Fügen Sie nach dem Formular hinzu:

```python
# Download-Bereich
if 'sop_doc' in st.session_state:
    st.header("4. Download")
    
    # Dokument in BytesIO speichern
    bio = io.BytesIO()
    st.session_state['sop_doc'].save(bio)
    bio.seek(0)
    
    # Download-Button
    st.download_button(
        label="📥 SOP herunterladen",
        data=bio.getvalue(),
        file_name=f"SOP_{st.session_state['sop_title'].replace(' ', '_')}.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    
    st.success("✅ Klicken Sie auf den Button um die SOP herunterzuladen")
```

### Schritt 4.2: Testen

```bash
# Kompletten Workflow durchlaufen
# Dokument hochladen
# Formular ausfüllen
# SOP generieren
# Download-Button klicken
# Heruntergeladene Datei in Word öffnen
# Prüfen: Formatierung korrekt
```

### Schritt 4.3: Finaler Commit

```bash
git commit -am "✨ feat: Füge Download-Funktion hinzu"
```

---

## 🎨 Bonus: Verbesserungen

### Template verwenden

Erstellen Sie ein vordefiniertes Template:

```python
# Template laden statt neues Dokument
template_path = "templates/sop_template.docx"
if Path(template_path).exists():
    sop_doc = Document(template_path)
else:
    sop_doc = Document()
```

### Vorschau

```python
# Vorschau des generierten Dokuments
with st.expander("👁️ Vorschau"):
    for para in sop_doc.paragraphs:
        st.write(para.text)
```

### PDF-Export (benötigt zusätzliche Library)

```python
# Mit python-docx-template und docx2pdf
# (Komplexer, optional)
```

---

## 🎉 Geschafft!

Sie haben einen funktionierenden SOP-Generator erstellt!

### Nächste Schritte

1. **Experimentieren:** Fügen Sie eigene Features hinzu
2. **Template:** Erstellen Sie ein professionelles SOP-Template
3. **Erweitern:** Siehe Bonus-Ideen
4. **Deployen:** Auf Streamlit Cloud

---

**Herzlichen Glückwunsch! 🎊**

