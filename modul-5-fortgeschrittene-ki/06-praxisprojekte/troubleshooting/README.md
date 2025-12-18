# 🔧 Troubleshooting Guide

Häufige Probleme und ihre Lösungen beim Programmieren mit Python und Streamlit.

## 🎯 Schnellhilfe

**Problem gefunden?** Nutzen Sie die Suchfunktion (Ctrl+F / Cmd+F) um nach Ihrer Fehlermeldung zu suchen.

## 📚 Kategorien

### 1. Import Errors
"ModuleNotFoundError", "ImportError"

👉 [import-errors.md](./import-errors.md)

### 2. File Not Found
"FileNotFoundError", "No such file or directory"

👉 [file-not-found.md](./file-not-found.md)

### 3. Streamlit-Probleme
App läuft nicht, Port-Probleme, Rerun-Fehler

👉 [streamlit-probleme.md](./streamlit-probleme.md)

### 4. Daten-Probleme
CSV-Fehler, Pandas-Probleme, Encoding

👉 [daten-probleme.md](./daten-probleme.md)

### 5. Allgemeine Python-Fehler
TypeError, AttributeError, NameError

👉 [python-fehler.md](./python-fehler.md)

## 🚨 Die häufigsten 5 Probleme

### 1. "ModuleNotFoundError: No module named 'streamlit'"

**Problem:** Dependency nicht installiert

**Lösung:**
```bash
# Prüfen Sie pyproject.toml
# Fügen Sie hinzu:
dependencies = [
    "streamlit>=1.28.0",
]

# Installieren:
uv sync
```

### 2. "FileNotFoundError: [Errno 2] No such file or directory: 'data/customers.csv'"

**Problem:** Datei existiert nicht oder falscher Pfad

**Lösung:**
```python
from pathlib import Path

# Pfad prüfen
file_path = Path("data/customers.csv")
if file_path.exists():
    # Datei existiert
    df = pd.read_csv(file_path)
else:
    # Datei existiert nicht
    print(f"Datei nicht gefunden: {file_path.absolute()}")
```

### 3. "Address already in use" (Streamlit)

**Problem:** Port 8501 bereits belegt

**Lösung:**
```bash
# Anderen Port verwenden:
uv run streamlit run app.py --server.port 8502

# Oder alten Prozess beenden:
# Mac/Linux:
lsof -ti:8501 | xargs kill -9

# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

### 4. "Wo ist mein Output?"

**Problem:** Output erscheint nicht wo erwartet

**Lösung:**
```python
# Terminal-Output
print("Erscheint im Terminal")  # ← Terminal

# Browser-Output (Streamlit)
st.write("Erscheint im Browser")  # ← Browser

# Datei-Output
df.to_csv("data/output.csv")  # ← Dateisystem
print(f"Gespeichert nach: {Path('data/output.csv').absolute()}")  # ← Terminal
```

### 5. "KeyError: 'column_name'" (Pandas)

**Problem:** Spalte existiert nicht im DataFrame

**Lösung:**
```python
# Spalten prüfen
print(df.columns.tolist())

# Sicher auf Spalte zugreifen
if 'column_name' in df.columns:
    value = df['column_name']
else:
    print("Spalte nicht gefunden!")
```

## 🔍 Debugging-Strategie

### Schritt 1: Fehlermeldung lesen

```
Traceback (most recent call last):
  File "app.py", line 42, in <module>
    result = process_data(df)
  File "app.py", line 15, in process_data
    return df['name'].upper()
KeyError: 'name'
```

**Wichtige Informationen:**
- **Fehlertyp:** `KeyError`
- **Zeile:** Line 15 in `process_data`
- **Problem:** Spalte 'name' existiert nicht

### Schritt 2: Problem lokalisieren

```python
# Debug-Ausgaben hinzufügen
print(f"DEBUG: DataFrame Spalten: {df.columns.tolist()}")
print(f"DEBUG: DataFrame Shape: {df.shape}")
print(f"DEBUG: Erste Zeilen:\n{df.head()}")
```

### Schritt 3: Googeln

**Gute Suchbegriffe:**
- `python KeyError name`
- `pandas KeyError column not found`
- `streamlit FileNotFoundError`

**Gute Quellen:**
- Stack Overflow
- Offizielle Dokumentation
- GitHub Issues

### Schritt 4: Lösung testen

```python
# Lösung implementieren
if 'name' in df.columns:
    result = df['name'].upper()
else:
    st.error("Spalte 'name' nicht gefunden!")
```

### Schritt 5: Committen

```bash
git commit -m "🐛 fix: Behebe KeyError bei fehlender Spalte"
```

## 💡 Präventive Massnahmen

### 1. Defensive Programmierung

```python
# Immer prüfen, bevor Sie zugreifen
if file_path.exists():
    # Datei existiert
    pass

if 'column' in df.columns:
    # Spalte existiert
    pass

if variable is not None:
    # Variable ist gesetzt
    pass
```

### 2. Try-Except verwenden

```python
try:
    df = pd.read_csv("data/customers.csv")
except FileNotFoundError:
    st.error("Datei nicht gefunden!")
    df = pd.DataFrame()  # Leerer DataFrame als Fallback
except Exception as e:
    st.error(f"Fehler beim Laden: {e}")
    df = pd.DataFrame()
```

### 3. Logging aktivieren

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Lade Daten...")
logger.info("Daten erfolgreich geladen")
logger.warning("Warnung: Einige Daten fehlen")
logger.error("Fehler beim Verarbeiten")
```

### 4. Kleine Schritte

- Schreiben Sie kleine Code-Abschnitte
- Testen Sie nach jedem Schritt
- Committen Sie oft
- Nicht alles auf einmal!

## 🆘 Wenn nichts hilft

### 1. Code vereinfachen

Reduzieren Sie den Code auf das Minimum:

```python
# Statt:
result = complex_function(data, param1, param2, param3)

# Versuchen Sie:
print(f"DEBUG: data = {data}")
print(f"DEBUG: param1 = {param1}")
result = complex_function(data, param1, param2, param3)
print(f"DEBUG: result = {result}")
```

### 2. Neu starten

```bash
# Virtual Environment neu erstellen
rm -rf .venv
uv sync --all-extras

# App neu starten
uv run streamlit run app.py
```

### 3. Vergleichen mit Musterlösung

Schauen Sie sich die Musterlösung an:
- Wie ist der Code strukturiert?
- Welche Imports werden verwendet?
- Wie werden Fehler behandelt?

### 4. Um Hilfe bitten

**Gute Frage stellen:**

```
Problem: FileNotFoundError beim Laden von CSV

Was ich versucht habe:
1. Pfad geprüft: data/customers.csv
2. Datei existiert im Ordner
3. Fehlermeldung: [Errno 2] No such file or directory

Code:
```python
df = pd.read_csv("data/customers.csv")
```

Umgebung:
- Python 3.11
- Streamlit 1.28.0
- macOS
```

**Schlechte Frage:**
"Mein Code funktioniert nicht. Hilfe!"

## 📖 Weitere Ressourcen

- [Python Docs](https://docs.python.org/3/)
- [Streamlit Docs](https://docs.streamlit.io)
- [Stack Overflow](https://stackoverflow.com)
- [Real Python Tutorials](https://realpython.com)

---

**Tipp:** Fehler sind normal! Jeder Programmierer macht Fehler. Wichtig ist, systematisch zu debuggen.

