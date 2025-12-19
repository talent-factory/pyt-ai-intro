# 🎨 Streamlit Basics - Code-Snippets

## Seitenkonfiguration

```python
import streamlit as st

st.set_page_config(
    page_title="Meine App",
    page_icon="🚀",
    layout="wide",  # oder "centered"
    initial_sidebar_state="expanded",  # oder "collapsed"
)
```

## Titel und Text

```python
# Titel
st.title("🚀 Meine App")

# Header
st.header("Hauptüberschrift")

# Subheader
st.subheader("Unterüberschrift")

# Text
st.write("Normaler Text")
st.markdown("**Fetter Text** und *kursiver Text*")

# Code
st.code("print('Hello World')", language="python")
```

## Eingabefelder

```python
# Text-Input
name = st.text_input("Ihr Name:", placeholder="Max Mustermann")

# Nummer-Input
age = st.number_input("Ihr Alter:", min_value=0, max_value=120, value=25)

# Text-Area
description = st.text_area("Beschreibung:", placeholder="Geben Sie eine Beschreibung ein...")

# Selectbox (Dropdown)
option = st.selectbox(
    "Wählen Sie eine Option:",
    options=["Option 1", "Option 2", "Option 3"]
)

# Multiselect
options = st.multiselect(
    "Wählen Sie mehrere Optionen:",
    options=["A", "B", "C", "D"],
    default=["A", "B"]
)

# Slider
value = st.slider("Wählen Sie einen Wert:", min_value=0, max_value=100, value=50)

# Checkbox
agree = st.checkbox("Ich stimme zu")

# Radio Buttons
choice = st.radio("Wählen Sie:", options=["Ja", "Nein", "Vielleicht"])

# Date Input
date = st.date_input("Datum:")

# Time Input
time = st.time_input("Zeit:")
```

## Buttons

```python
# Einfacher Button
if st.button("Klick mich!"):
    st.write("Button wurde geklickt!")

# Button mit Icon
if st.button("🚀 Start"):
    st.success("Gestartet!")

# Download Button
st.download_button(
    label="📥 Datei herunterladen",
    data="Inhalt der Datei",
    file_name="datei.txt",
    mime="text/plain"
)
```

## Formulare

```python
with st.form("my_form"):
    name = st.text_input("Name:")
    email = st.text_input("E-Mail:")
    message = st.text_area("Nachricht:")
    
    submitted = st.form_submit_button("Absenden")
    
    if submitted:
        st.success(f"Danke {name}! Ihre Nachricht wurde gesendet.")
```

## Layout

```python
# Spalten
col1, col2, col3 = st.columns(3)

with col1:
    st.write("Spalte 1")

with col2:
    st.write("Spalte 2")

with col3:
    st.write("Spalte 3")

# Spalten mit unterschiedlichen Breiten
col1, col2 = st.columns([2, 1])  # 2:1 Verhältnis

# Tabs
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("Inhalt von Tab 1")

with tab2:
    st.write("Inhalt von Tab 2")

# Expander (ausklappbar)
with st.expander("Mehr Informationen"):
    st.write("Hier sind zusätzliche Informationen...")

# Container
with st.container():
    st.write("Inhalt im Container")
    st.write("Mehr Inhalt...")

# Sidebar
st.sidebar.title("Sidebar")
st.sidebar.write("Inhalt in der Sidebar")
```

## Meldungen

```python
# Info
st.info("ℹ️ Dies ist eine Information")

# Success
st.success("✅ Erfolgreich!")

# Warning
st.warning("⚠️ Warnung!")

# Error
st.error("❌ Fehler!")

# Exception
try:
    # Code der fehlschlagen könnte
    result = 1 / 0
except Exception as e:
    st.exception(e)
```

## Metriken

```python
# Einfache Metrik
st.metric(label="Temperatur", value="25°C")

# Metrik mit Delta
st.metric(label="Umsatz", value="€1.2M", delta="€200K")

# Mehrere Metriken
col1, col2, col3 = st.columns(3)
col1.metric("Kunden", "1,234", "+12%")
col2.metric("Umsatz", "€56K", "+8%")
col3.metric("Gewinn", "€12K", "-3%")
```

## Progress & Spinner

```python
import time

# Progress Bar
progress_bar = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress_bar.progress(i + 1)

# Spinner
with st.spinner("Lädt..."):
    time.sleep(2)
st.success("Fertig!")

# Status
with st.status("Verarbeite Daten...") as status:
    st.write("Lade Daten...")
    time.sleep(1)
    st.write("Verarbeite...")
    time.sleep(1)
    status.update(label="Fertig!", state="complete")
```

## Session State

```python
# Initialisieren
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Verwenden
if st.button("Zähler erhöhen"):
    st.session_state.counter += 1

st.write(f"Zähler: {st.session_state.counter}")
```

---

**Tipp:** Kombinieren Sie diese Snippets für komplexere UIs!

