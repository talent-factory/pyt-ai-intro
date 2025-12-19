# 📁 File Not Found Errors

## FileNotFoundError: [Errno 2] No such file or directory

### Problem
Python kann die Datei nicht finden.

### Ursache 1: Datei existiert nicht

**Lösung:**
```python
from pathlib import Path

# Prüfen ob Datei existiert
file_path = Path("data/customers.csv")
if not file_path.exists():
    print(f"Datei nicht gefunden: {file_path.absolute()}")
    # Datei erstellen oder Fehler behandeln
```

### Ursache 2: Falscher Pfad (relativ vs. absolut)

**Problem:**
```python
# Relativer Pfad - abhängig vom aktuellen Verzeichnis!
df = pd.read_csv("data/customers.csv")
```

**Wo bin ich?**
```python
import os
print(f"Aktuelles Verzeichnis: {os.getcwd()}")
```

**Lösung 1: Relativer Pfad vom Skript**
```python
from pathlib import Path

# Pfad relativ zum Skript
script_dir = Path(__file__).parent
data_file = script_dir / "data" / "customers.csv"

df = pd.read_csv(data_file)
```

**Lösung 2: Absoluter Pfad**
```python
# Absoluter Pfad (nicht empfohlen, aber funktioniert immer)
df = pd.read_csv("/Users/daniel/projekt/data/customers.csv")
```

### Ursache 3: Ordner existiert nicht

**Problem:**
```python
# Fehler wenn 'data/' Ordner nicht existiert
df.to_csv("data/output.csv")
```

**Lösung:**
```python
from pathlib import Path

# Ordner erstellen falls nicht vorhanden
output_path = Path("data/output.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)

# Jetzt speichern
df.to_csv(output_path)
```

## Debugging-Strategie

### Schritt 1: Pfad ausgeben

```python
from pathlib import Path

file_path = Path("data/customers.csv")
print(f"Suche Datei: {file_path}")
print(f"Absoluter Pfad: {file_path.absolute()}")
print(f"Existiert: {file_path.exists()}")
```

### Schritt 2: Verzeichnis-Inhalt prüfen

```python
from pathlib import Path

# Alle Dateien im data/ Ordner
data_dir = Path("data")
if data_dir.exists():
    print("Dateien in data/:")
    for file in data_dir.iterdir():
        print(f"  - {file.name}")
else:
    print("Ordner 'data/' existiert nicht!")
```

### Schritt 3: Arbeitsverzeichnis prüfen

```python
import os
from pathlib import Path

print(f"Arbeitsverzeichnis: {os.getcwd()}")
print(f"Skript-Verzeichnis: {Path(__file__).parent}")
```

## Häufige Szenarien

### Streamlit App

```python
# app.py liegt im Projekt-Root
# data/customers.csv liegt im data/ Ordner

# ✅ Richtig:
from pathlib import Path

DATA_FILE = Path("data/customers.csv")

# Beim Laden prüfen:
if DATA_FILE.exists():
    df = pd.read_csv(DATA_FILE)
else:
    # Leerer DataFrame als Fallback
    df = pd.DataFrame(columns=["company", "street", "city"])
```

### Home-Verzeichnis

```python
from pathlib import Path

# Datei im Home-Verzeichnis
home_dir = Path.home()
config_file = home_dir / ".myapp" / "config.json"

# Ordner erstellen
config_file.parent.mkdir(parents=True, exist_ok=True)

# Datei speichern
with open(config_file, 'w') as f:
    json.dump(config, f)
```

## Best Practices

### 1. Immer Path verwenden

```python
from pathlib import Path

# ✅ Gut:
file_path = Path("data") / "customers.csv"

# ❌ Vermeiden:
file_path = "data/customers.csv"  # String
```

### 2. Existenz prüfen

```python
if file_path.exists():
    # Datei existiert
    pass
else:
    # Datei existiert nicht - Fehler behandeln
    pass
```

### 3. Ordner erstellen

```python
# Ordner erstellen falls nicht vorhanden
file_path.parent.mkdir(parents=True, exist_ok=True)
```

### 4. Try-Except verwenden

```python
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    st.error(f"Datei nicht gefunden: {file_path}")
    df = pd.DataFrame()  # Fallback
```

---

**Tipp:** Verwenden Sie immer `Path` aus `pathlib` statt String-Pfade!

