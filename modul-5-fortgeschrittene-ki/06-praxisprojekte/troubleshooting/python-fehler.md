# 🐍 Allgemeine Python-Fehler

Häufige Python-Fehler und ihre Lösungen.

## 🔴 NameError

### Problem: "NameError: name 'variable' is not defined"

**Ursache:** Variable wurde nicht definiert oder Tippfehler

**Lösung:**

```python
# Falsch:
print(result)  # ❌ result existiert nicht

# Richtig:
result = 42
print(result)  # ✅

# Oder: Variable prüfen
try:
    print(result)
except NameError:
    print("Variable 'result' existiert nicht")
```

## 🔵 TypeError

### Problem: "TypeError: unsupported operand type(s) for +: 'int' and 'str'"

**Ursache:** Falsche Datentypen kombiniert

**Lösung:**

```python
# Falsch:
age = 25
text = "Ich bin " + age + " Jahre alt"  # ❌

# Richtig:
age = 25
text = "Ich bin " + str(age) + " Jahre alt"  # ✅
# Oder:
text = f"Ich bin {age} Jahre alt"  # ✅ (f-string)
```

### Problem: "TypeError: 'NoneType' object is not subscriptable"

**Ursache:** Variable ist None

**Lösung:**

```python
# Falsch:
result = function_that_returns_none()
value = result[0]  # ❌

# Richtig:
result = function_that_returns_none()
if result is not None:
    value = result[0]  # ✅
else:
    print("Funktion hat None zurückgegeben")
```

## 🟡 AttributeError

### Problem: "AttributeError: 'NoneType' object has no attribute 'method'"

**Ursache:** Objekt ist None

**Lösung:**

```python
# Falsch:
df = None
df.head()  # ❌

# Richtig:
df = pd.read_csv("data.csv")
if df is not None:
    df.head()  # ✅
```

### Problem: "AttributeError: module 'streamlit' has no attribute 'function'"

**Ursache:** Funktion existiert nicht oder falsche Version

**Lösung:**

```python
# Streamlit-Version prüfen
import streamlit as st
print(st.__version__)

# Dependencies aktualisieren
# Terminal: uv sync --upgrade

# Dokumentation prüfen
# https://docs.streamlit.io
```

## 🟢 IndexError

### Problem: "IndexError: list index out of range"

**Ursache:** Index existiert nicht in Liste

**Lösung:**

```python
# Falsch:
my_list = [1, 2, 3]
value = my_list[5]  # ❌

# Richtig:
my_list = [1, 2, 3]
if len(my_list) > 5:
    value = my_list[5]  # ✅
else:
    print("Index 5 existiert nicht")

# Oder: try-except
try:
    value = my_list[5]
except IndexError:
    print("Index existiert nicht")
```

## 🟣 IndentationError

### Problem: "IndentationError: expected an indented block"

**Ursache:** Falsche Einrückung

**Lösung:**

```python
# Falsch:
def my_function():
print("Hello")  # ❌ Keine Einrückung

# Richtig:
def my_function():
    print("Hello")  # ✅ 4 Leerzeichen

# Tipp: Verwenden Sie einen Editor mit Auto-Indent (VS Code, PyCharm)
```

## 🟠 SyntaxError

### Problem: "SyntaxError: invalid syntax"

**Ursache:** Syntaxfehler im Code

**Häufige Ursachen:**

```python
# Fehlende Klammer
print("Hello"  # ❌
print("Hello")  # ✅

# Fehlender Doppelpunkt
if x > 5  # ❌
if x > 5:  # ✅

# Falsche Anführungszeichen
text = "Hello'  # ❌
text = "Hello"  # ✅

# Fehlende Komma
my_list = [1, 2 3]  # ❌
my_list = [1, 2, 3]  # ✅
```

## 🔶 ValueError

### Problem: "ValueError: invalid literal for int() with base 10"

**Ursache:** String kann nicht in Integer konvertiert werden

**Lösung:**

```python
# Falsch:
age = int("25 Jahre")  # ❌

# Richtig:
age_str = "25 Jahre"
age = int(age_str.split()[0])  # ✅ Nur Zahl extrahieren

# Oder: Fehlerbehandlung
try:
    age = int(age_str)
except ValueError:
    print(f"Kann '{age_str}' nicht in Integer konvertieren")
    age = None
```

## 🔷 ImportError / ModuleNotFoundError

### Problem: "ModuleNotFoundError: No module named 'module_name'"

**Ursache:** Modul nicht installiert

**Lösung:**

```bash
# Prüfen Sie pyproject.toml
# Fügen Sie hinzu:
dependencies = [
    "module_name>=1.0.0",
]

# Installieren:
uv sync
```

**Siehe auch:** [import-errors.md](./import-errors.md)

## 🔸 FileNotFoundError

**Siehe:** [file-not-found.md](./file-not-found.md)

## 💡 Debugging-Tipps

### 1. Print-Debugging

```python
# Variablen ausgeben
print(f"DEBUG: variable = {variable}")
print(f"DEBUG: type = {type(variable)}")

# Funktionsaufruf tracken
def my_function(x):
    print(f"DEBUG: my_function aufgerufen mit x={x}")
    result = x * 2
    print(f"DEBUG: result = {result}")
    return result
```

### 2. Type Hints verwenden

```python
# Ohne Type Hints
def add(a, b):
    return a + b

# Mit Type Hints
def add(a: int, b: int) -> int:
    return a + b

# Editor zeigt Fehler an, wenn falsche Typen verwendet werden
```

### 3. Assertions verwenden

```python
def divide(a: float, b: float) -> float:
    assert b != 0, "Division durch Null nicht erlaubt"
    return a / b

# Bei Fehler: AssertionError mit Nachricht
```

### 4. Logging statt Print

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug-Information")
logger.info("Informative Nachricht")
logger.warning("Warnung")
logger.error("Fehler")
```

## 📖 Weitere Ressourcen

- [Python Docs - Built-in Exceptions](https://docs.python.org/3/library/exceptions.html)
- [Real Python - Python Exceptions](https://realpython.com/python-exceptions/)
- [Python Debugging Guide](https://realpython.com/python-debugging-pdb/)

---

**Tipp:** Lesen Sie Fehlermeldungen von unten nach oben. Die letzte Zeile enthält meist die wichtigste Information.

