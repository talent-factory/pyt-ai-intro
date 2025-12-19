# 📁 File Handling - Code-Snippets

## Streamlit File Upload

### Einfacher Upload

```python
import streamlit as st

uploaded_file = st.file_uploader("Datei hochladen")

if uploaded_file is not None:
    st.success(f"Datei '{uploaded_file.name}' hochgeladen!")
    st.write(f"Grösse: {uploaded_file.size} Bytes")
```

### Upload mit Typ-Filter

```python
# Nur CSV-Dateien
uploaded_file = st.file_uploader(
    "CSV-Datei hochladen",
    type=["csv"]
)

# Mehrere Typen
uploaded_file = st.file_uploader(
    "Dokument hochladen",
    type=["csv", "xlsx", "txt", "json"]
)

# Bilder
uploaded_file = st.file_uploader(
    "Bild hochladen",
    type=["png", "jpg", "jpeg", "gif"]
)
```

### Mehrere Dateien hochladen

```python
uploaded_files = st.file_uploader(
    "Dateien hochladen",
    type=["csv"],
    accept_multiple_files=True
)

if uploaded_files:
    st.write(f"{len(uploaded_files)} Dateien hochgeladen:")
    for file in uploaded_files:
        st.write(f"- {file.name}")
```

### CSV hochladen und lesen

```python
import pandas as pd

uploaded_file = st.file_uploader("CSV hochladen", type=["csv"])

if uploaded_file is not None:
    # CSV lesen
    df = pd.read_csv(uploaded_file)
    
    # Anzeigen
    st.dataframe(df)
    
    # Statistiken
    st.write(f"Zeilen: {len(df)}")
    st.write(f"Spalten: {len(df.columns)}")
```

### JSON hochladen und lesen

```python
import json

uploaded_file = st.file_uploader("JSON hochladen", type=["json"])

if uploaded_file is not None:
    # JSON lesen
    data = json.load(uploaded_file)
    
    # Anzeigen
    st.json(data)
```

### Bild hochladen und anzeigen

```python
from PIL import Image

uploaded_file = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Bild öffnen
    image = Image.open(uploaded_file)
    
    # Anzeigen
    st.image(image, caption=uploaded_file.name, use_column_width=True)
    
    # Informationen
    st.write(f"Grösse: {image.size}")
    st.write(f"Format: {image.format}")
```

### Word-Dokument hochladen

```python
from docx import Document
import io

uploaded_file = st.file_uploader("Word-Dokument hochladen", type=["docx"])

if uploaded_file is not None:
    # Dokument lesen
    doc = Document(uploaded_file)
    
    # Absätze anzeigen
    st.write("Inhalt:")
    for para in doc.paragraphs:
        if para.text.strip():
            st.write(para.text)
```

## Streamlit File Download

### Text-Datei Download

```python
import streamlit as st

# Text-Inhalt
text_content = "Hallo Welt!\nDies ist eine Test-Datei."

# Download-Button
st.download_button(
    label="📥 Text herunterladen",
    data=text_content,
    file_name="output.txt",
    mime="text/plain"
)
```

### CSV Download

```python
import pandas as pd

# DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Alter": [25, 30, 35]
})

# CSV als String
csv = df.to_csv(index=False)

# Download-Button
st.download_button(
    label="📥 CSV herunterladen",
    data=csv,
    file_name="daten.csv",
    mime="text/csv"
)
```

### JSON Download

```python
import json

# Daten
data = {
    "name": "Meine App",
    "version": "1.0.0",
    "settings": {"theme": "dark"}
}

# JSON als String
json_str = json.dumps(data, indent=2, ensure_ascii=False)

# Download-Button
st.download_button(
    label="📥 JSON herunterladen",
    data=json_str,
    file_name="config.json",
    mime="application/json"
)
```

### Excel Download

```python
import pandas as pd
import io

# DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Alter": [25, 30, 35]
})

# Excel in BytesIO schreiben
buffer = io.BytesIO()
with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
    df.to_excel(writer, index=False, sheet_name='Daten')

# Download-Button
st.download_button(
    label="📥 Excel herunterladen",
    data=buffer.getvalue(),
    file_name="daten.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
```

### Word-Dokument Download

```python
from docx import Document
import io

# Dokument erstellen
doc = Document()
doc.add_heading("Mein Dokument", 0)
doc.add_paragraph("Dies ist ein Test-Dokument.")

# In BytesIO schreiben
bio = io.BytesIO()
doc.save(bio)
bio.seek(0)

# Download-Button
st.download_button(
    label="📥 Word herunterladen",
    data=bio.getvalue(),
    file_name="dokument.docx",
    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
)
```

## Dateien lesen/schreiben (Python)

### Text-Datei lesen

```python
from pathlib import Path

# Lesen
file_path = Path("data/text.txt")
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
else:
    content = ""
```

### Text-Datei schreiben

```python
from pathlib import Path

# Schreiben
file_path = Path("data/output.txt")
file_path.parent.mkdir(parents=True, exist_ok=True)

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Hallo Welt!")
```

### Zeilen lesen

```python
# Alle Zeilen lesen
with open("data/text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Zeile für Zeile
with open("data/text.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

### Zeilen schreiben

```python
lines = ["Zeile 1", "Zeile 2", "Zeile 3"]

with open("data/output.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")
```

## Pfad-Operationen

### Pfad prüfen

```python
from pathlib import Path

file_path = Path("data/file.txt")

# Existiert?
if file_path.exists():
    print("Datei existiert")

# Ist Datei?
if file_path.is_file():
    print("Ist eine Datei")

# Ist Ordner?
if file_path.is_dir():
    print("Ist ein Ordner")
```

### Ordner erstellen

```python
from pathlib import Path

# Ordner erstellen
folder = Path("data/subfolder")
folder.mkdir(parents=True, exist_ok=True)
```

### Dateien auflisten

```python
from pathlib import Path

# Alle Dateien in einem Ordner
folder = Path("data")
for file in folder.iterdir():
    print(file.name)

# Nur CSV-Dateien
for file in folder.glob("*.csv"):
    print(file.name)

# Rekursiv
for file in folder.rglob("*.csv"):
    print(file)
```

### Pfad-Informationen

```python
from pathlib import Path

file_path = Path("data/subfolder/file.txt")

# Name
print(file_path.name)  # file.txt

# Ordner
print(file_path.parent)  # data/subfolder

# Endung
print(file_path.suffix)  # .txt

# Absoluter Pfad
print(file_path.absolute())
```

---

**Tipp:** Verwenden Sie immer `Path` aus `pathlib` für Pfad-Operationen!

