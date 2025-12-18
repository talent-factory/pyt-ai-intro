# 📊 Daten-Probleme

Häufige Probleme beim Arbeiten mit Daten (CSV, Pandas, Encoding).

## 🚨 CSV-Fehler

### Problem: "ParserError: Error tokenizing data"

**Ursache:** CSV-Datei ist fehlerhaft formatiert

**Lösung:**

```python
import pandas as pd

# Option 1: Fehlerhafte Zeilen überspringen
df = pd.read_csv("data.csv", on_bad_lines='skip')

# Option 2: Fehlerhafte Zeilen warnen
df = pd.read_csv("data.csv", on_bad_lines='warn')

# Option 3: Separator explizit angeben
df = pd.read_csv("data.csv", sep=';')  # Statt Komma

# Option 4: Encoding anpassen
df = pd.read_csv("data.csv", encoding='utf-8')
```

### Problem: "UnicodeDecodeError"

**Ursache:** Falsches Encoding

**Lösung:**

```python
# Verschiedene Encodings probieren
encodings = ['utf-8', 'latin-1', 'iso-8859-1', 'cp1252']

for enc in encodings:
    try:
        df = pd.read_csv("data.csv", encoding=enc)
        print(f"✅ Erfolgreich mit Encoding: {enc}")
        break
    except UnicodeDecodeError:
        print(f"❌ Fehlgeschlagen mit Encoding: {enc}")
```

### Problem: "EmptyDataError: No columns to parse"

**Ursache:** CSV-Datei ist leer

**Lösung:**

```python
from pathlib import Path

file_path = Path("data.csv")

# Prüfen ob Datei leer ist
if file_path.stat().st_size == 0:
    st.warning("Datei ist leer!")
    df = pd.DataFrame()  # Leerer DataFrame
else:
    df = pd.read_csv(file_path)
```

## 🔑 KeyError

### Problem: "KeyError: 'column_name'"

**Ursache:** Spalte existiert nicht im DataFrame

**Lösung:**

```python
# Spalten anzeigen
print(f"Verfügbare Spalten: {df.columns.tolist()}")

# Sicher auf Spalte zugreifen
if 'column_name' in df.columns:
    value = df['column_name']
else:
    st.error("Spalte 'column_name' nicht gefunden!")
    
# Alternative: get() verwenden
value = df.get('column_name', default=None)
```

### Problem: Spaltenname mit Leerzeichen

**Ursache:** Spaltenname enthält führende/nachfolgende Leerzeichen

**Lösung:**

```python
# Spaltennamen bereinigen
df.columns = df.columns.str.strip()

# Oder: Leerzeichen durch Underscore ersetzen
df.columns = df.columns.str.replace(' ', '_')
```

## 📝 Datentyp-Probleme

### Problem: "TypeError: unsupported operand type(s)"

**Ursache:** Falscher Datentyp

**Lösung:**

```python
# Datentypen anzeigen
print(df.dtypes)

# Datentyp konvertieren
df['age'] = df['age'].astype(int)
df['price'] = df['price'].astype(float)
df['date'] = pd.to_datetime(df['date'])

# Fehlerhafte Werte behandeln
df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Fehler → NaN
```

### Problem: "ValueError: could not convert string to float"

**Ursache:** String kann nicht in Zahl konvertiert werden

**Lösung:**

```python
# Fehlerhafte Werte finden
print(df[df['price'].apply(lambda x: not str(x).replace('.', '').isdigit())])

# Bereinigen
df['price'] = df['price'].str.replace(',', '.')  # Komma → Punkt
df['price'] = pd.to_numeric(df['price'], errors='coerce')  # Fehler → NaN
df = df.dropna(subset=['price'])  # NaN entfernen
```

## 🔍 Fehlende Daten

### Problem: NaN-Werte

**Ursache:** Fehlende Daten im DataFrame

**Lösung:**

```python
# NaN-Werte finden
print(df.isnull().sum())

# Option 1: NaN entfernen
df_clean = df.dropna()

# Option 2: NaN füllen
df['column'] = df['column'].fillna(0)  # Mit 0
df['column'] = df['column'].fillna('Unbekannt')  # Mit String
df['column'] = df['column'].fillna(df['column'].mean())  # Mit Durchschnitt

# Option 3: Nur bestimmte Spalten prüfen
df = df.dropna(subset=['wichtige_spalte'])
```

## 💾 Speichern-Probleme

### Problem: "PermissionError: [Errno 13] Permission denied"

**Ursache:** Datei ist geöffnet oder keine Schreibrechte

**Lösung:**

```python
# Prüfen ob Datei geöffnet ist
# → Datei schliessen (Excel, Editor, etc.)

# Alternative: Anderen Dateinamen verwenden
from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"data_{timestamp}.csv"
df.to_csv(filename, index=False)
```

### Problem: Index wird mitgespeichert

**Ursache:** Pandas speichert standardmässig den Index

**Lösung:**

```python
# Index nicht speichern
df.to_csv("data.csv", index=False)
```

## 🔄 Daten-Transformation

### Problem: Datum wird nicht erkannt

**Ursache:** Datumsformat nicht erkannt

**Lösung:**

```python
# Datum parsen
df['date'] = pd.to_datetime(df['date'], format='%d.%m.%Y')  # 31.12.2023
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')  # 2023-12-31

# Automatisch erkennen
df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)

# Fehlerhafte Werte behandeln
df['date'] = pd.to_datetime(df['date'], errors='coerce')
```

## 📖 Weitere Ressourcen

- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Real Python - Pandas Tutorial](https://realpython.com/pandas-python-explore-dataset/)

---

**Tipp:** Verwenden Sie `df.info()` und `df.describe()` um einen Überblick über Ihre Daten zu bekommen.

