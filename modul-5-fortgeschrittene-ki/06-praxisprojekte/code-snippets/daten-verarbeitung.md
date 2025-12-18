# 📊 Datenverarbeitung - Code-Snippets

## CSV-Dateien

### CSV lesen

```python
import pandas as pd
from pathlib import Path

# Einfaches Lesen
df = pd.read_csv("data/customers.csv")

# Mit Optionen
df = pd.read_csv(
    "data/customers.csv",
    sep=",",           # Trennzeichen
    encoding="utf-8",  # Encoding
    header=0,          # Erste Zeile als Header
)

# Sicher lesen (mit Fehlerbehandlung)
file_path = Path("data/customers.csv")
if file_path.exists():
    df = pd.read_csv(file_path)
else:
    # Leerer DataFrame mit Spalten
    df = pd.DataFrame(columns=["name", "email", "city"])
```

### CSV schreiben

```python
# Einfaches Schreiben
df.to_csv("data/output.csv", index=False)

# Mit Optionen
df.to_csv(
    "data/output.csv",
    index=False,        # Keine Index-Spalte
    encoding="utf-8",   # Encoding
    sep=",",            # Trennzeichen
)

# Sicher schreiben (Ordner erstellen)
from pathlib import Path

output_path = Path("data/output.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)
```

### CSV an DataFrame anhängen

```python
# Neue Zeile hinzufügen
new_row = {
    "name": "Max Mustermann",
    "email": "max@example.com",
    "city": "Zürich"
}

# Mit pd.concat (empfohlen)
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Speichern
df.to_csv("data/customers.csv", index=False)
```

## JSON-Dateien

### JSON lesen

```python
import json
from pathlib import Path

# JSON lesen
with open("data/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

# Sicher lesen
file_path = Path("data/config.json")
if file_path.exists():
    with open(file_path, "r", encoding="utf-8") as f:
        config = json.load(f)
else:
    config = {}  # Leeres Dict als Fallback
```

### JSON schreiben

```python
import json
from pathlib import Path

# Daten
config = {
    "app_name": "Meine App",
    "version": "1.0.0",
    "settings": {
        "theme": "dark",
        "language": "de"
    }
}

# JSON schreiben (formatiert)
with open("data/config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

# Sicher schreiben
output_path = Path("data/config.json")
output_path.parent.mkdir(parents=True, exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2, ensure_ascii=False)
```

## Pandas DataFrame Operationen

### DataFrame erstellen

```python
import pandas as pd

# Aus Dictionary
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],
    "city": ["Zürich", "Bern", "Basel"]
}
df = pd.DataFrame(data)

# Aus Liste von Dictionaries
data = [
    {"name": "Alice", "age": 25, "city": "Zürich"},
    {"name": "Bob", "age": 30, "city": "Bern"},
]
df = pd.DataFrame(data)

# Leerer DataFrame mit Spalten
df = pd.DataFrame(columns=["name", "age", "city"])
```

### Zeilen filtern

```python
# Nach Bedingung
filtered_df = df[df["age"] > 25]

# Mehrere Bedingungen (UND)
filtered_df = df[(df["age"] > 25) & (df["city"] == "Zürich")]

# Mehrere Bedingungen (ODER)
filtered_df = df[(df["age"] > 25) | (df["city"] == "Zürich")]

# Nach Wert in Liste
cities = ["Zürich", "Bern"]
filtered_df = df[df["city"].isin(cities)]
```

### Spalten auswählen

```python
# Einzelne Spalte
names = df["name"]

# Mehrere Spalten
subset = df[["name", "city"]]

# Alle Spalten ausser eine
df_without_age = df.drop(columns=["age"])
```

### Zeilen hinzufügen

```python
# Neue Zeile
new_row = {"name": "David", "age": 28, "city": "Luzern"}

# Anhängen (empfohlen)
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
```

### Zeilen löschen

```python
# Nach Index
df = df.drop(index=0)  # Erste Zeile löschen

# Nach Bedingung
df = df[df["age"] != 25]  # Alle mit age=25 entfernen

# Index zurücksetzen
df = df.reset_index(drop=True)
```

### Sortieren

```python
# Nach einer Spalte
df_sorted = df.sort_values("age")

# Absteigend
df_sorted = df.sort_values("age", ascending=False)

# Nach mehreren Spalten
df_sorted = df.sort_values(["city", "age"])
```

### Aggregationen

```python
# Anzahl Zeilen
count = len(df)

# Summe
total_age = df["age"].sum()

# Durchschnitt
avg_age = df["age"].mean()

# Minimum / Maximum
min_age = df["age"].min()
max_age = df["age"].max()

# Gruppieren und aggregieren
grouped = df.groupby("city")["age"].mean()
```

## Fehlende Werte behandeln

```python
# Fehlende Werte prüfen
has_missing = df.isnull().any().any()

# Zeilen mit fehlenden Werten entfernen
df_clean = df.dropna()

# Fehlende Werte ersetzen
df_filled = df.fillna(0)  # Mit 0
df_filled = df.fillna({"age": 0, "city": "Unbekannt"})  # Pro Spalte
```

## Streamlit Integration

### DataFrame anzeigen

```python
import streamlit as st

# Interaktive Tabelle
st.dataframe(df)

# Statische Tabelle
st.table(df)

# Mit Formatierung
st.dataframe(
    df,
    use_container_width=True,
    hide_index=True,
)
```

### DataFrame bearbeiten

```python
# Editierbare Tabelle (Streamlit >= 1.23)
edited_df = st.data_editor(
    df,
    num_rows="dynamic",  # Zeilen hinzufügen/löschen
    use_container_width=True,
)

# Änderungen speichern
if st.button("Speichern"):
    edited_df.to_csv("data/customers.csv", index=False)
    st.success("Gespeichert!")
```

---

**Tipp:** Verwenden Sie immer `index=False` beim CSV-Schreiben, um die Index-Spalte zu vermeiden!

