# 🎈 Streamlit-Probleme

## Address already in use

### Problem
```
OSError: [Errno 48] Address already in use
```

### Ursache
Port 8501 ist bereits belegt (alte Streamlit-Instanz läuft noch).

### Lösung 1: Anderen Port verwenden

```bash
uv run streamlit run app.py --server.port 8502
```

### Lösung 2: Alten Prozess beenden

**Mac/Linux:**
```bash
# Prozess finden und beenden
lsof -ti:8501 | xargs kill -9
```

**Windows:**
```bash
# Prozess finden
netstat -ano | findstr :8501

# Prozess beenden (PID aus obigem Befehl)
taskkill /PID <PID> /F
```

## Streamlit läuft nicht / Browser öffnet sich nicht

### Problem
App startet nicht oder Browser öffnet sich nicht.

### Lösung 1: Manuell öffnen

```bash
# App starten
uv run streamlit run app.py

# Browser manuell öffnen:
# http://localhost:8501
```

### Lösung 2: Firewall prüfen

Prüfen Sie ob Ihre Firewall Port 8501 blockiert.

### Lösung 3: Streamlit neu installieren

```bash
uv sync --reinstall
```

## "Wo ist der Output?"

### Terminal vs. Browser

```python
# ❌ Erscheint NUR im Terminal:
print("Hallo Welt")

# ✅ Erscheint im Browser (Streamlit):
st.write("Hallo Welt")

# ✅ Beide:
message = "Hallo Welt"
print(f"Terminal: {message}")  # Terminal
st.write(f"Browser: {message}")  # Browser
```

### Debugging-Output

```python
# Für Entwicklung: Beide Outputs
def debug_print(message):
    """Gibt Nachricht in Terminal UND Browser aus."""
    print(f"DEBUG: {message}")  # Terminal
    st.write(f"DEBUG: {message}")  # Browser

debug_print("Lade Daten...")
```

## App lädt nicht neu / Änderungen nicht sichtbar

### Problem
Code-Änderungen werden nicht angezeigt.

### Lösung 1: "Rerun" klicken

Klicken Sie auf "Rerun" in der Streamlit-App (oben rechts).

### Lösung 2: Browser-Cache leeren

```
Ctrl+Shift+R (Windows/Linux)
Cmd+Shift+R (Mac)
```

### Lösung 3: App neu starten

```bash
# Ctrl+C zum Stoppen
# Dann neu starten:
uv run streamlit run app.py
```

## Session State Probleme

### Problem
Daten gehen verloren nach Rerun.

### Ursache
Streamlit läuft das Skript bei jeder Interaktion komplett neu.

### Lösung: Session State verwenden

```python
# ❌ Falsch - Wert geht verloren:
counter = 0
if st.button("Erhöhen"):
    counter += 1  # Geht verloren!
st.write(counter)  # Immer 0

# ✅ Richtig - Session State:
if 'counter' not in st.session_state:
    st.session_state.counter = 0

if st.button("Erhöhen"):
    st.session_state.counter += 1

st.write(st.session_state.counter)  # Bleibt erhalten!
```

## Formular wird nicht submitted

### Problem
Form Submit Button funktioniert nicht.

### Ursache
Button ausserhalb des Formulars oder falscher Code.

### Lösung

```python
# ✅ Richtig:
with st.form("my_form"):
    name = st.text_input("Name:")
    submitted = st.form_submit_button("Absenden")  # Innerhalb!
    
    if submitted:
        st.write(f"Hallo {name}")

# ❌ Falsch:
with st.form("my_form"):
    name = st.text_input("Name:")

submitted = st.form_submit_button("Absenden")  # Ausserhalb!
```

## File Upload funktioniert nicht

### Problem
Hochgeladene Datei kann nicht gelesen werden.

### Lösung

```python
uploaded_file = st.file_uploader("Datei hochladen", type=["csv"])

if uploaded_file is not None:  # Wichtig: is not None!
    # Datei lesen
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)
else:
    st.info("Bitte Datei hochladen")
```

## Karte wird nicht angezeigt (Folium)

### Problem
Folium-Karte erscheint nicht in Streamlit.

### Ursache
`streamlit-folium` nicht installiert.

### Lösung

```toml
# pyproject.toml
dependencies = [
    "folium>=0.15.0",
    "streamlit-folium>=0.15.0",  # Wichtig!
]
```

```bash
uv sync
```

```python
# Code:
import folium
from streamlit_folium import st_folium  # Wichtig!

m = folium.Map(location=[46.8182, 8.2275], zoom_start=7)
st_folium(m, width=700, height=500)  # Nicht folium_static!
```

## Performance-Probleme

### Problem
App ist langsam.

### Lösung 1: Caching verwenden

```python
@st.cache_data
def load_data():
    """Lädt Daten nur einmal."""
    df = pd.read_csv("large_file.csv")
    return df

# Wird nur beim ersten Aufruf ausgeführt
df = load_data()
```

### Lösung 2: Lazy Loading

```python
# Daten nur laden wenn benötigt
if st.button("Daten laden"):
    df = load_data()
    st.dataframe(df)
```

---

**Tipp:** Streamlit führt das gesamte Skript bei jeder Interaktion neu aus. Nutzen Sie Session State und Caching!

