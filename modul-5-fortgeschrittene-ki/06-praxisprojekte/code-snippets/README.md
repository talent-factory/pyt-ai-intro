# 🧩 Code-Snippets Bibliothek

Wiederverwendbare Code-Bausteine für Ihre Streamlit-Projekte.

## 📚 Verfügbare Snippets

### 1. Streamlit Basics
Formulare, Buttons, Eingabefelder, Layout

👉 [streamlit-basics.md](./streamlit-basics.md)

### 2. Datenverarbeitung
CSV, JSON, Pandas, Daten laden/speichern

👉 [daten-verarbeitung.md](./daten-verarbeitung.md)

### 3. Visualisierung
Karten, Charts, Tabellen, Plots

👉 [visualisierung.md](./visualisierung.md)

### 4. File Handling
Upload, Download, Dateien lesen/schreiben

👉 [file-handling.md](./file-handling.md)

## 💡 Wie verwende ich diese Snippets?

### 1. Snippet finden
Suchen Sie nach dem gewünschten Feature in den Kategorien oben.

### 2. Code kopieren
Kopieren Sie den Code-Snippet.

### 3. Dependencies prüfen
Prüfen Sie, welche Bibliotheken benötigt werden (siehe Import-Statements).

### 4. Dependencies installieren
Fügen Sie fehlende Dependencies zu `pyproject.toml` hinzu:

```toml
dependencies = [
    "streamlit>=1.28.0",
    "pandas>=2.0.0",  # Beispiel
]
```

Dann installieren:
```bash
uv sync
```

### 5. Code anpassen
Passen Sie den Code an Ihre Bedürfnisse an:
- Variablennamen ändern
- Texte anpassen
- Funktionalität erweitern

### 6. Testen
Testen Sie den Code in Ihrer App:
```bash
uv run streamlit run app.py
```

## 🎯 Beispiel-Workflow

**Aufgabe:** Ich möchte einen File-Upload für CSV-Dateien.

**Schritt 1:** Öffne `file-handling.md`

**Schritt 2:** Finde "CSV-Upload" Snippet

**Schritt 3:** Kopiere Code:
```python
uploaded_file = st.file_uploader("CSV hochladen", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
```

**Schritt 4:** Prüfe Dependencies: `pandas` wird benötigt

**Schritt 5:** Füge zu `pyproject.toml` hinzu (falls nicht vorhanden)

**Schritt 6:** Installiere: `uv sync`

**Schritt 7:** Füge Code in `app.py` ein

**Schritt 8:** Teste: `uv run streamlit run app.py`

**Fertig!** ✅

## 📖 Weitere Ressourcen

- [Streamlit Cheat Sheet](https://docs.streamlit.io/library/cheatsheet)
- [Streamlit API Reference](https://docs.streamlit.io/library/api-reference)
- [Streamlit Gallery](https://streamlit.io/gallery)

---

**Viel Erfolg beim Coden! 🚀**

