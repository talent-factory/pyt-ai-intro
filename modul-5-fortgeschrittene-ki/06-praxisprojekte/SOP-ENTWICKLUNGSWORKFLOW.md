# 📋 SOP: Python-Projekt von Anfang bis Ende

Diese **Standard Operating Procedure (SOP)** ist Ihr roter Faden für jedes Python-Projekt. Folgen Sie dieser Checkliste Schritt für Schritt, um strukturiert und effizient zu arbeiten.

## 🎯 Überblick

```text
1. Projekt initialisieren     → Repository, UV, Struktur
2. Entwicklungsworkflow       → Code schreiben, testen, committen
3. Code-Snippets integrieren  → Finden, anpassen, einbauen
4. Output verstehen           → Terminal, Datei, Web
5. Qualität sichern           → Ruff, Tests, Dokumentation
6. Deployment                 → App veröffentlichen
```

---

## 1️⃣ Projekt initialisieren

### 1.1 Repository auf GitHub erstellen

**Warum?** Versionskontrolle, Backup, Zusammenarbeit

**Schritte:**

```text
□ Auf GitHub.com einloggen
□ "New Repository" klicken
□ Repository-Name eingeben (z.B. "customer-map-app")
□ "Public" oder "Private" wählen
□ ✅ "Add README" aktivieren
□ ✅ "Add .gitignore" → Python auswählen
□ "Create repository" klicken
```

**Output:** Repository-URL (z.B. `https://github.com/username/customer-map-app`)

### 1.2 Repository lokal klonen

**Warum?** Lokale Kopie zum Arbeiten

**Schritte:**

```bash
# □ Terminal öffnen

# □ Zu gewünschtem Ordner navigieren: cd ~/Projekte

# □ Repository klonen:
  git clone https://github.com/username/customer-map-app.git

# □ In Projektordner wechseln: cd customer-map-app
```

**Output:** Ordner mit Repository-Inhalt

**Wo ist der Output?** Im Dateisystem unter `~/Projekte/customer-map-app/`

### 1.3 UV initialisieren

**Warum?** Dependency Management, virtuelle Umgebung

**Schritte:**

```bash
# □ UV installieren (falls noch nicht vorhanden):
  curl -LsSf https://astral.sh/uv/install.sh | sh

# □ Projekt initialisieren:
  uv init

# □ Python-Version festlegen (optional):
  uv python pin 3.11
```

**Output:**
- `.python-version` Datei
- `pyproject.toml` Datei

**Wo ist der Output?** Im Projektordner

### 1.4 .gitignore erstellen/ergänzen

**Warum?** Verhindert, dass unnötige Dateien ins Repository kommen

**Schritte:**

```bash
# □ .gitignore öffnen (sollte bereits existieren)
# □ Folgende Zeilen hinzufügen (falls nicht vorhanden):

# Python
__pycache__/
*.pyc
.venv/
.uv/

# Streamlit
.streamlit/

# Daten (optional)
data/*.csv
!data/example.csv

# IDE
.vscode/
.idea/
```

**Output:** Aktualisierte `.gitignore` Datei

### 1.5 Projektstruktur anlegen

**Warum?** Organisation, Übersichtlichkeit

**Schritte:**

```bash
# □ Ordner erstellen:
  mkdir -p app data utils tests

# □ Dateien erstellen:
  touch app.py
  touch utils/__init__.py
  touch tests/__init__.py
  touch README.md
```

**Empfohlene Struktur:**

```text
projekt-name/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── app.py              # Hauptdatei (Streamlit App)
├── data/               # Daten (CSV, JSON, etc.)
│   └── example.csv
├── utils/              # Hilfsfunktionen
│   ├── __init__.py
│   ├── data_loader.py
│   └── visualizer.py
└── tests/              # Tests
    ├── __init__.py
    └── test_data_loader.py
```

### 1.6 Erste Dependencies installieren

**Warum?** Benötigte Bibliotheken verfügbar machen

**Schritte:**

```yaml
# □ pyproject.toml öffnen
# □ Dependencies hinzufügen:

[project]
name = "customer-map-app"
version = "0.1.0"
dependencies = [
    "streamlit>=1.28.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.0",
    "pytest>=7.4.0",
]
```

```bash
# □ Dependencies installieren:
  uv sync --all-extras
```

**Output:** `.venv/` Ordner mit installierten Paketen

**Wo ist der Output?** Im Projektordner unter `.venv/`

### 1.7 Erster Commit

**Warum?** Ausgangspunkt festhalten

**Schritte:**

```bash
# □ Status prüfen: git status

# □ Alle Dateien hinzufügen: git add .

# □ Commit erstellen:
  git commit -m "🎉 init: Initialisiere Projekt mit UV und Struktur"

# □ Zum Remote pushen:
  git push origin main
```

**Output:** Commit im Repository

**Wo ist der Output?** Auf GitHub sichtbar

---

## 2️⃣ Entwicklungsworkflow

### 2.1 Feature-Branch erstellen (optional)

**Warum?** Saubere Trennung von Features

**Schritte:**

```bash
# □ Branch erstellen:
  git checkout -b feature/dateneingabe
```

### 2.2 Code schreiben (iterativ!)

**Wichtig:** Kleine Schritte! Nicht alles auf einmal.

**Iteration 1: Minimale funktionierende Version**

```python
# app.py
import streamlit as st

st.title("Meine App")
st.write("Hallo Welt!")
```

**Schritte:**
```bash
□ Code schreiben
□ Speichern
□ Lokal testen (siehe 2.3)
□ Committen (siehe 2.4)
```

**Iteration 2: Nächstes Feature**

```python
# app.py
import streamlit as st

st.title("Meine App")

name = st.text_input("Dein Name:")
if st.button("Grüssen"):
    st.success(f"Hallo {name}!")
```

**Schritte:**

```text
□ Code erweitern
□ Speichern
□ Lokal testen
□ Committen
```

**Und so weiter...**

### 2.3 Lokal testen

**Warum?** Fehler früh erkennen

**Für Streamlit-Apps:**

```text
□ Terminal öffnen
□ App starten: uv run streamlit run app.py
□ Browser öffnet sich automatisch
□ App testen
□ Mit Ctrl+C stoppen
```

**Wo ist der Output?**

- Terminal: Logs und Fehlermeldungen
- Browser: Die App selbst (meist `http://localhost:8501`)

**Für Python-Skripte:**

```text
□ Skript ausführen: uv run python mein_skript.py
□ Output im Terminal beobachten
```

**Wo ist der Output?**

- Terminal: `print()` Ausgaben
- Dateien: Wenn das Skript Dateien schreibt

### 2.4 Committen (oft!)

**Warum?** Fortschritt sichern, Änderungen nachvollziehbar

**Schritte:**

```bash
# □ Status prüfen: git status

# □ Änderungen hinzufügen: git add .

# □ Commit erstellen:
  git commit -m "✨ feat: Füge Begrüssungsformular hinzu"
```

**Commit-Message Format:**

```
<emoji> <typ>: <kurze Beschreibung>

<optionale Details>
```

**Häufige Typen:**

- ✨ `feat`: Neues Feature
- 🐛 `fix`: Fehlerbehebung
- 📚 `docs`: Dokumentation
- ♻️ `refactor`: Code-Umstrukturierung
- 🧪 `test`: Tests

**Wie oft committen?**

- Nach jedem funktionierenden Feature
- Mindestens 1x pro Stunde
- Lieber zu oft als zu selten!

---

## 3️⃣ Code-Snippets integrieren

### 3.1 Code-Snippet finden

**Wo suchen?**

```text
□ Google: "streamlit file upload example"
□ Streamlit Docs: https://docs.streamlit.io
□ GitHub: Suche nach ähnlichen Projekten
□ Stack Overflow: Spezifische Probleme
```

**Beispiel-Suche:**

"Wie lade ich eine CSV-Datei in Streamlit hoch?"

### 3.2 Dependencies identifizieren

**Schritte:**

```python
# □ Code-Snippet anschauen
# □ Import-Statements identifizieren:
  import pandas as pd          → pandas
  import streamlit as st       → streamlit
  from PIL import Image        → pillow

# □ Notieren, welche Pakete fehlen
```

### 3.3 Dependencies installieren

**Schritte:**

```yaml
# □ pyproject.toml öffnen
# □ Dependency hinzufügen:
  dependencies = [
      "streamlit>=1.28.0",
      "pandas>=2.0.0",
      "pillow>=10.0.0",  # NEU
  ]

# □ Installieren: uv sync
```

**Output:** Paket wird heruntergeladen und installiert

**Wo ist der Output?** Terminal zeigt Installation

### 3.4 Code-Snippet anpassen

**Schritte:**

```text
□ Code-Snippet kopieren
□ In eigene Datei einfügen
□ Variablennamen anpassen
□ An eigene Struktur anpassen
□ Kommentare hinzufügen
```

**Beispiel:**

```python
# Original-Snippet
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)

# Angepasst
uploaded_file = st.file_uploader(
    "Kundenliste hochladen (CSV)",
    type=['csv']
)
if uploaded_file is not None:
    # CSV einlesen
    customers_df = pd.read_csv(uploaded_file)

    # Erste 5 Zeilen anzeigen
    st.write("Vorschau:")
    st.dataframe(customers_df.head())
```

### 3.5 Testen!

**Schritte:**

```text
□ App starten: uv run streamlit run app.py
□ Funktion testen
□ Fehler beheben (siehe Troubleshooting)
□ Erneut testen
```

**Häufige Fehler:**

- `ModuleNotFoundError` → Dependency fehlt
- `FileNotFoundError` → Pfad falsch
- `AttributeError` → Falscher Variablenname

---

## 4️⃣ Output verstehen

### 4.1 Terminal-Output

**Was erscheint im Terminal?**

- `print()` Ausgaben
- Logging-Meldungen
- Fehlermeldungen
- Streamlit-Status

**Beispiel:**

```python
print("Lade Daten...")  # Erscheint im Terminal
st.write("Lade Daten...")  # Erscheint in der App
```

**Wo sehe ich es?** Im Terminal-Fenster

### 4.2 Datei-Output

**Wo werden Dateien gespeichert?**

**Relative Pfade:**

```python
# Speichert im Projektordner
df.to_csv("data/customers.csv")
# → projekt-name/data/customers.csv
```

**Absolute Pfade:**

```python
# Speichert an spezifischem Ort
df.to_csv("/Users/daniel/Desktop/customers.csv")
# → Desktop
```

**Tipp:** Immer relative Pfade verwenden!

**Wo sehe ich es?** Im Dateisystem (Finder/Explorer)

### 4.3 Web-Output (Streamlit)

**Was erscheint im Browser?**

- `st.write()`, `st.text()`, `st.markdown()`
- `st.dataframe()`, `st.table()`
- `st.pyplot()`, `st.plotly_chart()`
- Alle Streamlit-Widgets

**Wo sehe ich es?** Im Browser unter `http://localhost:8501`

**Wichtig:** Terminal-Output ≠ Browser-Output!

### 4.4 Debugging: Wo ist mein Output?

**Checkliste:**

```text
□ Terminal prüfen: Gibt es print() Ausgaben?
□ Browser prüfen: Läuft Streamlit? Richtige URL?
□ Dateisystem prüfen: Wurde Datei erstellt?
□ Pfade prüfen: Relativer vs. absoluter Pfad?
□ Logs prüfen: Gibt es Fehlermeldungen?
```

**Beispiel-Debugging:**

```python
# Debugging-Ausgaben hinzufügen
print(f"DEBUG: Speichere Datei nach: {filepath}")  # Terminal
st.write(f"DEBUG: Speichere Datei nach: {filepath}")  # Browser

# Datei speichern
df.to_csv(filepath)

# Prüfen ob erfolgreich
import os
if os.path.exists(filepath):
    print("✅ Datei erfolgreich gespeichert")  # Terminal
    st.success("✅ Datei erfolgreich gespeichert")  # Browser
else:
    print("❌ Datei nicht gefunden!")  # Terminal
    st.error("❌ Datei nicht gefunden!")  # Browser
```

---

## 5️⃣ Qualität sichern

### 5.1 Code formatieren mit Ruff

**Warum?** Einheitlicher Code-Stil, weniger Fehler

**Schritte:**

```bash
# □ Ruff ausführen (Check):
  uv run ruff check .

# □ Fehler anschauen

# □ Automatisch beheben:
  uv run ruff check --fix .

# □ Formatierung anwenden:
  uv run ruff format .
```

**Output:** Liste von Problemen oder "All checks passed!"

**Wo ist der Output?** Terminal

### 5.2 Tests schreiben (optional, aber empfohlen)

**Warum?** Sicherstellen, dass Code funktioniert

**Beispiel:**
```python
# tests/test_data_loader.py
import pandas as pd
from utils.data_loader import load_customers

def test_load_customers():
    """Test ob Kundendaten korrekt geladen werden."""
    df = load_customers("data/example.csv")

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "name" in df.columns
```

**Schritte:**
```text
□ Test-Datei erstellen
□ Test-Funktion schreiben
□ Tests ausführen: uv run pytest
□ Alle Tests grün? ✅
```

**Output:** Test-Ergebnisse

**Wo ist der Output?** Terminal

### 5.3 README aktualisieren

**Warum?** Andere (und Sie selbst später) verstehen das Projekt

**Mindestinhalt:**
```markdown
# Projekt-Name

Kurze Beschreibung

## Installation

git clone <url>
cd projekt-name
uv sync --all-extras


## Verwendung

uv run streamlit run app.py


## Features

- Feature 1
- Feature 2

## Technologien

- Python 3.11
- Streamlit
- Pandas
```

---

## 6️⃣ Deployment

### 6.1 Vorbereitung

**Schritte:**

```text
□ Alle Änderungen committen
□ Zum Remote pushen: git push origin main
□ README prüfen
□ .gitignore prüfen (keine Secrets!)
```

### 6.2 Streamlit Cloud Deployment

**Warum?** App mit anderen teilen, im Internet verfügbar

**Schritte:**

```text
□ Auf https://share.streamlit.io einloggen (mit GitHub)
□ "New app" klicken
□ Repository auswählen
□ Branch auswählen (meist "main")
□ Main file path angeben (z.B. "app.py")
□ "Deploy!" klicken
□ Warten (1-2 Minuten)
□ App-URL erhalten (z.B. https://username-app.streamlit.app)
```

**Output:** Öffentlich zugängliche URL

**Wo ist der Output?** Im Internet, für alle sichtbar!

### 6.3 Deployment testen

**Schritte:**

```text
□ App-URL im Browser öffnen
□ Alle Features testen
□ Mit Freunden/Kollegen teilen
□ Feedback sammeln
```

### 6.4 Updates deployen

**Schritte:**

```text
□ Änderungen lokal machen
□ Committen
□ Pushen: git push origin main
□ Streamlit Cloud deployed automatisch neu!
```

**Dauer:** 1-2 Minuten

---

## 📊 Checkliste: Kompletter Workflow

### Projekt-Start

- [ ] Repository auf GitHub erstellen
- [ ] Lokal klonen
- [ ] UV initialisieren
- [ ] Projektstruktur anlegen
- [ ] Dependencies installieren
- [ ] Erster Commit

### Entwicklung (iterativ)
- [ ] Feature planen
- [ ] Code schreiben (kleine Schritte!)
- [ ] Lokal testen
- [ ] Funktioniert? → Committen
- [ ] Nächstes Feature

### Code-Snippet Integration
- [ ] Snippet finden (Google, Docs)
- [ ] Dependencies identifizieren
- [ ] Dependencies installieren
- [ ] Code anpassen
- [ ] Testen
- [ ] Committen

### Qualität
- [ ] Ruff ausführen
- [ ] Tests schreiben (optional)
- [ ] README aktualisieren
- [ ] Committen

### Deployment
- [ ] Alle Änderungen pushen
- [ ] Streamlit Cloud konfigurieren
- [ ] Deployen
- [ ] Testen
- [ ] Teilen!

---

## 🎯 Häufige Fragen

### "Wie oft soll ich committen?"
**Antwort:** Nach jedem funktionierenden Feature. Lieber zu oft als zu selten!

### "Muss ich Tests schreiben?"
**Antwort:** Für Lernprojekte: Optional. Für echte Projekte: Ja!

### "Wo finde ich gute Code-Snippets?"
**Antwort:**
- Offizielle Dokumentation (z.B. Streamlit Docs)
- GitHub (ähnliche Projekte)
- Stack Overflow
- Unsere Code-Snippets Bibliothek

### "Wie passe ich Code-Snippets an?"
**Antwort:**
1. Verstehen, was der Code macht
2. Variablennamen anpassen
3. An eigene Struktur anpassen
4. Testen!

### "Wo erscheint mein Output?"
**Antwort:** Kommt drauf an:
- `print()` → Terminal
- `st.write()` → Browser (Streamlit)
- `df.to_csv()` → Dateisystem
- `logging.info()` → Log-Datei

### "Was mache ich bei Fehlern?"
**Antwort:**
1. Fehlermeldung lesen
2. Googeln: "python <fehlermeldung>"
3. Troubleshooting-Guide konsultieren
4. Dozent fragen

---

## 🚀 Nächste Schritte

1. **Drucken Sie diese SOP aus** oder speichern Sie sie als Lesezeichen
2. **Starten Sie mit Projekt 1:** [Kunden-Map](./projekt-1-kunden-map/)
3. **Folgen Sie der Checkliste** Schritt für Schritt
4. **Experimentieren Sie!** Das ist der beste Weg zu lernen

---

**Viel Erfolg! 🎉**

Diese SOP ist Ihr Begleiter für alle Python-Projekte. Je öfter Sie sie durchlaufen, desto natürlicher wird der Workflow!

