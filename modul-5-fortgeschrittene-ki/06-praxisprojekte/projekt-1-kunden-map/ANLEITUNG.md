# 📖 Schritt-für-Schritt Anleitung: Kunden-Map App

Diese Anleitung führt Sie durch die **komplette Entwicklung** der Kunden-Visualisierungs-App. Jeder Schritt baut auf dem vorherigen auf.

## 🎯 Überblick

Wir entwickeln die App in **7 Iterationen**:

1. **Setup & Minimale App** - "Hallo Welt"
2. **Dateneingabe** - Formular für Kundendaten
3. **Datenspeicherung** - CSV-Datei schreiben
4. **Datenanzeige** - Kunden auflisten
5. **Geocoding** - Adressen → Koordinaten
6. **Karten-Visualisierung** - Interaktive Karte
7. **Filter & Statistiken** - Daten filtern

**Wichtig:** Nach jedem Schritt testen und committen!

---

## 🚀 Iteration 1: Setup & Minimale App

**Ziel:** Projekt aufsetzen und erste funktionierende Streamlit-App

**Dauer:** 15 Minuten

### Schritt 1.1: Repository erstellen

```bash
# Auf GitHub
□ Neues Repository erstellen: "customer-map-app"
□ README und .gitignore (Python) hinzufügen
□ Repository erstellen

# Lokal
□ Repository klonen:
  git clone https://github.com/IHR-USERNAME/customer-map-app.git
  cd customer-map-app
```

### Schritt 1.2: UV initialisieren

```bash
□ UV initialisieren:
  uv init
  
□ Python-Version festlegen:
  uv python pin 3.11
```

**Erwartetes Ergebnis:**
- `.python-version` Datei erstellt
- `pyproject.toml` erstellt

### Schritt 1.3: Projektstruktur erstellen

```bash
□ Ordner erstellen:
  mkdir -p data utils tests
  
□ Dateien erstellen:
  touch app.py
  touch utils/__init__.py
  touch data/.gitkeep
```

**Erwartete Struktur:**
```
customer-map-app/
├── .gitignore
├── .python-version
├── pyproject.toml
├── README.md
├── app.py
├── data/
│   └── .gitkeep
└── utils/
    └── __init__.py
```

### Schritt 1.4: Dependencies hinzufügen

Öffnen Sie `pyproject.toml` und ergänzen Sie:

```toml
[project]
name = "customer-map-app"
version = "0.1.0"
description = "Kunden-Adressen Visualisierung mit Streamlit"
requires-python = ">=3.11"
dependencies = [
    "streamlit>=1.28.0",
    "pandas>=2.0.0",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.0",
    "pytest>=7.4.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I"]
```

```bash
□ Dependencies installieren:
  uv sync --all-extras
```

**Erwartetes Ergebnis:**
- `.venv/` Ordner erstellt
- `uv.lock` Datei erstellt
- Streamlit und Pandas installiert

### Schritt 1.5: Minimale App erstellen

Öffnen Sie `app.py` und schreiben Sie:

```python
"""Kunden-Adressen Visualisierung mit Streamlit."""

import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="Kunden-Map",
    page_icon="🗺️",
    layout="wide",
)

# Titel
st.title("🗺️ Kunden-Adressen Visualisierung")
st.write("Willkommen zur Kunden-Visualisierungs-App!")

# Info-Box
st.info("Diese App hilft Ihnen, Kundenadressen zu verwalten und zu visualisieren.")
```

### Schritt 1.6: App testen

```bash
□ App starten:
  uv run streamlit run app.py
  
□ Browser öffnet sich automatisch
□ Prüfen: Titel und Text werden angezeigt
□ Mit Ctrl+C stoppen
```

**Wo ist der Output?**
- Terminal: Streamlit-Logs
- Browser: Die App unter `http://localhost:8501`

### Schritt 1.7: Erster Commit

```bash
□ Status prüfen:
  git status
  
□ Dateien hinzufügen:
  git add .
  
□ Committen:
  git commit -m "🎉 init: Initialisiere Projekt mit minimaler Streamlit-App"
  
□ Pushen:
  git push origin main
```

**✅ Checkpoint:** Sie haben eine funktionierende Streamlit-App!

---

## 📝 Iteration 2: Dateneingabe

**Ziel:** Formular für Kundendaten erstellen

**Dauer:** 20 Minuten

### Schritt 2.1: Formular erstellen

Erweitern Sie `app.py`:

```python
"""Kunden-Adressen Visualisierung mit Streamlit."""

import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="Kunden-Map",
    page_icon="🗺️",
    layout="wide",
)

# Titel
st.title("🗺️ Kunden-Adressen Visualisierung")

# Sidebar für Dateneingabe
st.sidebar.header("Neuen Kunden hinzufügen")

with st.sidebar.form("customer_form"):
    # Eingabefelder
    company = st.text_input("Firmenname*", placeholder="z.B. Acme GmbH")
    street = st.text_input("Strasse*", placeholder="z.B. Bahnhofstrasse 1")
    zip_code = st.text_input("PLZ*", placeholder="z.B. 8001")
    city = st.text_input("Ort*", placeholder="z.B. Zürich")
    country = st.selectbox(
        "Land*",
        options=["Schweiz", "Deutschland", "Österreich", "Frankreich", "Italien"],
    )
    
    # Submit-Button
    submitted = st.form_submit_button("Kunde hinzufügen")
    
    if submitted:
        # Validierung
        if not company or not street or not zip_code or not city:
            st.error("Bitte füllen Sie alle Pflichtfelder aus!")
        else:
            # Erfolg (vorerst nur Anzeige)
            st.success(f"✅ Kunde '{company}' erfolgreich hinzugefügt!")
            st.write(f"Adresse: {street}, {zip_code} {city}, {country}")

# Hauptbereich
st.header("Kundenliste")
st.info("Noch keine Kunden vorhanden. Fügen Sie den ersten Kunden hinzu!")
```

### Schritt 2.2: App testen

```bash
□ App starten:
  uv run streamlit run app.py
  
□ Formular ausfüllen
□ "Kunde hinzufügen" klicken
□ Prüfen: Erfolgsmeldung erscheint
□ Prüfen: Validierung funktioniert (leere Felder)
```

**Wo ist der Output?**
- Browser: Formular in der Sidebar
- Browser: Erfolgsmeldung nach Submit

### Schritt 2.3: Commit

```bash
□ git add .
□ git commit -m "✨ feat: Füge Formular für Kundendaten hinzu"
□ git push
```

**✅ Checkpoint:** Formular funktioniert und validiert Eingaben!

---

## 💾 Iteration 3: Datenspeicherung

**Ziel:** Kundendaten in CSV-Datei speichern

**Dauer:** 25 Minuten

### Schritt 3.1: Pandas importieren

Ergänzen Sie am Anfang von `app.py`:

```python
import streamlit as st
import pandas as pd
from pathlib import Path
```

### Schritt 3.2: Hilfsfunktionen erstellen

Fügen Sie nach den Imports hinzu:

```python
# Konstanten
DATA_FILE = Path("data/customers.csv")

def load_customers():
    """Lädt Kundendaten aus CSV-Datei.
    
    Returns:
        pd.DataFrame: Kundendaten oder leerer DataFrame
    """
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        # Leerer DataFrame mit Spalten
        return pd.DataFrame(columns=[
            "company", "street", "zip_code", "city", "country"
        ])

def save_customer(company, street, zip_code, city, country):
    """Speichert einen neuen Kunden.
    
    Args:
        company: Firmenname
        street: Strasse
        zip_code: PLZ
        city: Ort
        country: Land
    """
    # Bestehende Daten laden
    df = load_customers()
    
    # Neuen Kunden hinzufügen
    new_customer = pd.DataFrame([{
        "company": company,
        "street": street,
        "zip_code": zip_code,
        "city": city,
        "country": country,
    }])
    
    df = pd.concat([df, new_customer], ignore_index=True)
    
    # Speichern
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_FILE, index=False)
```

### Schritt 3.3: Formular anpassen

Ändern Sie den `if submitted:` Block:

```python
    if submitted:
        # Validierung
        if not company or not street or not zip_code or not city:
            st.error("Bitte füllen Sie alle Pflichtfelder aus!")
        else:
            # Speichern
            save_customer(company, street, zip_code, city, country)
            st.success(f"✅ Kunde '{company}' erfolgreich hinzugefügt!")
            st.rerun()  # App neu laden
```

### Schritt 3.4: Kundenliste anzeigen

Ersetzen Sie den "Hauptbereich" Teil:

```python
# Hauptbereich
st.header("Kundenliste")

# Daten laden
customers_df = load_customers()

if len(customers_df) == 0:
    st.info("Noch keine Kunden vorhanden. Fügen Sie den ersten Kunden hinzu!")
else:
    st.write(f"**Anzahl Kunden:** {len(customers_df)}")
    st.dataframe(customers_df, use_container_width=True)
```

### Schritt 3.5: App testen

```bash
□ App starten
□ Mehrere Kunden hinzufügen
□ Prüfen: Kunden erscheinen in der Tabelle
□ App stoppen und neu starten
□ Prüfen: Kunden sind noch da (persistiert!)
□ Prüfen: CSV-Datei existiert unter data/customers.csv
```

**Wo ist der Output?**
- Browser: Tabelle mit Kunden
- Dateisystem: `data/customers.csv`

### Schritt 3.6: Commit

```bash
□ git add .
□ git commit -m "✨ feat: Implementiere Datenspeicherung in CSV"
□ git push
```

**✅ Checkpoint:** Daten werden gespeichert und bleiben erhalten!

## 🗑️ Iteration 4: Kunden löschen (Optional)

**Ziel:** Möglichkeit zum Löschen von Kunden

**Dauer:** 15 Minuten

### Schritt 4.1: Lösch-Funktion erstellen

Fügen Sie nach `save_customer()` hinzu:

```python
def delete_customer(index):
    """Löscht einen Kunden.

    Args:
        index: Index des zu löschenden Kunden
    """
    df = load_customers()
    df = df.drop(index).reset_index(drop=True)
    df.to_csv(DATA_FILE, index=False)
```

### Schritt 4.2: Lösch-Buttons hinzufügen

Ersetzen Sie die Tabellen-Anzeige:

```python
if len(customers_df) == 0:
    st.info("Noch keine Kunden vorhanden. Fügen Sie den ersten Kunden hinzu!")
else:
    st.write(f"**Anzahl Kunden:** {len(customers_df)}")

    # Tabelle mit Lösch-Buttons
    for idx, row in customers_df.iterrows():
        col1, col2 = st.columns([5, 1])

        with col1:
            st.write(f"**{row['company']}** - {row['street']}, {row['zip_code']} {row['city']}, {row['country']}")

        with col2:
            if st.button("🗑️", key=f"delete_{idx}"):
                delete_customer(idx)
                st.rerun()
```

### Schritt 4.3: Testen & Committen

```bash
□ App testen
□ Kunde löschen
□ git commit -m "✨ feat: Füge Lösch-Funktion hinzu"
```

---

## 🌍 Iteration 5: Geocoding

**Ziel:** Adressen in Koordinaten umwandeln

**Dauer:** 30 Minuten

### Schritt 5.1: Dependency hinzufügen

Ergänzen Sie in `pyproject.toml`:

```toml
dependencies = [
    "streamlit>=1.28.0",
    "pandas>=2.0.0",
    "geopy>=2.4.0",  # NEU
]
```

```bash
□ Installieren:
  uv sync
```

### Schritt 5.2: Geocoder-Modul erstellen

Erstellen Sie `utils/geocoder.py`:

```python
"""Geocoding-Funktionen für Adress-Umwandlung."""

from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import time

# Geocoder initialisieren
geolocator = Nominatim(user_agent="customer_map_app")

def geocode_address(street, zip_code, city, country):
    """Wandelt Adresse in Koordinaten um.

    Args:
        street: Strasse
        zip_code: PLZ
        city: Ort
        country: Land

    Returns:
        tuple: (latitude, longitude) oder (None, None) bei Fehler
    """
    # Adresse zusammensetzen
    address = f"{street}, {zip_code} {city}, {country}"

    try:
        # Geocoding durchführen
        location = geolocator.geocode(address, timeout=10)

        if location:
            return location.latitude, location.longitude
        else:
            # Fallback: Nur Stadt und Land
            location = geolocator.geocode(f"{city}, {country}", timeout=10)
            if location:
                return location.latitude, location.longitude

        return None, None

    except (GeocoderTimedOut, GeocoderServiceError) as e:
        print(f"Geocoding-Fehler: {e}")
        return None, None
```

### Schritt 5.3: Geocoding beim Speichern

Ändern Sie `save_customer()` in `app.py`:

```python
import streamlit as st
import pandas as pd
from pathlib import Path
from utils.geocoder import geocode_address  # NEU

# ... (Rest bleibt gleich)

def save_customer(company, street, zip_code, city, country):
    """Speichert einen neuen Kunden mit Geocoding."""
    # Geocoding durchführen
    with st.spinner("Ermittle Koordinaten..."):
        lat, lon = geocode_address(street, zip_code, city, country)

    # Bestehende Daten laden
    df = load_customers()

    # Neuen Kunden hinzufügen
    new_customer = pd.DataFrame([{
        "company": company,
        "street": street,
        "zip_code": zip_code,
        "city": city,
        "country": country,
        "latitude": lat,
        "longitude": lon,
    }])

    df = pd.concat([df, new_customer], ignore_index=True)

    # Speichern
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DATA_FILE, index=False)
```

### Schritt 5.4: load_customers() anpassen

```python
def load_customers():
    """Lädt Kundendaten aus CSV-Datei."""
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    else:
        return pd.DataFrame(columns=[
            "company", "street", "zip_code", "city", "country",
            "latitude", "longitude"  # NEU
        ])
```

### Schritt 5.5: Testen

```bash
□ App starten
□ Neuen Kunden hinzufügen
□ Prüfen: "Ermittle Koordinaten..." Spinner erscheint
□ Prüfen: CSV enthält latitude und longitude Spalten
□ CSV-Datei öffnen und Koordinaten prüfen
```

**Wo ist der Output?**
- Browser: Spinner während Geocoding
- CSV: Neue Spalten `latitude` und `longitude`

### Schritt 5.6: Commit

```bash
□ git add .
□ git commit -m "✨ feat: Implementiere Geocoding für Adressen"
□ git push
```

**✅ Checkpoint:** Adressen werden in Koordinaten umgewandelt!

---

## 🗺️ Iteration 6: Karten-Visualisierung

**Ziel:** Kunden auf interaktiver Karte anzeigen

**Dauer:** 30 Minuten

### Schritt 6.1: Dependencies hinzufügen

Ergänzen Sie in `pyproject.toml`:

```toml
dependencies = [
    "streamlit>=1.28.0",
    "pandas>=2.0.0",
    "geopy>=2.4.0",
    "folium>=0.15.0",  # NEU
    "streamlit-folium>=0.15.0",  # NEU
]
```

```bash
□ Installieren:
  uv sync
```

### Schritt 6.2: Map-Creator Modul erstellen

Erstellen Sie `utils/map_creator.py`:

```python
"""Karten-Erstellung mit Folium."""

import folium
import pandas as pd

def create_customer_map(customers_df):
    """Erstellt eine Karte mit allen Kunden.

    Args:
        customers_df: DataFrame mit Kundendaten (inkl. latitude, longitude)

    Returns:
        folium.Map: Interaktive Karte
    """
    # Kunden mit Koordinaten filtern
    valid_customers = customers_df.dropna(subset=["latitude", "longitude"])

    if len(valid_customers) == 0:
        # Leere Karte (Schweiz zentriert)
        return folium.Map(location=[46.8182, 8.2275], zoom_start=7)

    # Zentrum berechnen (Durchschnitt aller Koordinaten)
    center_lat = valid_customers["latitude"].mean()
    center_lon = valid_customers["longitude"].mean()

    # Karte erstellen
    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)

    # Marker für jeden Kunden
    for _, customer in valid_customers.iterrows():
        # Popup-Text
        popup_text = f"""
        <b>{customer['company']}</b><br>
        {customer['street']}<br>
        {customer['zip_code']} {customer['city']}<br>
        {customer['country']}
        """

        # Marker hinzufügen
        folium.Marker(
            location=[customer["latitude"], customer["longitude"]],
            popup=folium.Popup(popup_text, max_width=200),
            tooltip=customer["company"],
            icon=folium.Icon(color="blue", icon="building", prefix="fa"),
        ).add_to(m)

    return m
```

### Schritt 6.3: Karte in App einbinden

Ergänzen Sie in `app.py`:

```python
import streamlit as st
import pandas as pd
from pathlib import Path
from streamlit_folium import st_folium  # NEU
from utils.geocoder import geocode_address
from utils.map_creator import create_customer_map  # NEU
```

Fügen Sie nach der Kundenliste hinzu:

```python
# Hauptbereich
st.header("Kundenliste")

# Daten laden
customers_df = load_customers()

if len(customers_df) == 0:
    st.info("Noch keine Kunden vorhanden. Fügen Sie den ersten Kunden hinzu!")
else:
    st.write(f"**Anzahl Kunden:** {len(customers_df)}")

    # Tabs für Tabelle und Karte
    tab1, tab2 = st.tabs(["📋 Tabelle", "🗺️ Karte"])

    with tab1:
        # Tabelle anzeigen
        st.dataframe(customers_df, use_container_width=True)

    with tab2:
        # Karte erstellen und anzeigen
        customer_map = create_customer_map(customers_df)
        st_folium(customer_map, width=1200, height=600)
```

### Schritt 6.4: Testen

```bash
□ App starten
□ Zur "Karte" Tab wechseln
□ Prüfen: Karte wird angezeigt
□ Prüfen: Marker für jeden Kunden
□ Auf Marker klicken → Popup mit Infos
□ Karte zoomen und verschieben
```

**Wo ist der Output?**
- Browser: Interaktive Karte im "Karte" Tab

### Schritt 6.5: Commit

```bash
□ git add .
□ git commit -m "✨ feat: Füge interaktive Karten-Visualisierung hinzu"
□ git push
```

**✅ Checkpoint:** Kunden werden auf Karte visualisiert!

---

## 📊 Iteration 7: Filter & Statistiken

**Ziel:** Daten filtern und Statistiken anzeigen

**Dauer:** 20 Minuten

### Schritt 7.1: Filter hinzufügen

Ergänzen Sie vor den Tabs:

```python
if len(customers_df) > 0:
    st.write(f"**Anzahl Kunden:** {len(customers_df)}")

    # Filter
    col1, col2 = st.columns([2, 1])

    with col1:
        # Länder-Filter
        countries = ["Alle"] + sorted(customers_df["country"].unique().tolist())
        selected_country = st.selectbox("Filter nach Land:", countries)

    with col2:
        # Statistiken
        st.metric("Länder", customers_df["country"].nunique())

    # Daten filtern
    if selected_country != "Alle":
        filtered_df = customers_df[customers_df["country"] == selected_country]
    else:
        filtered_df = customers_df

    st.write(f"**Angezeigte Kunden:** {len(filtered_df)}")

    # Tabs mit gefilterten Daten
    tab1, tab2 = st.tabs(["📋 Tabelle", "🗺️ Karte"])

    with tab1:
        st.dataframe(filtered_df, use_container_width=True)

    with tab2:
        customer_map = create_customer_map(filtered_df)  # Gefilterte Daten!
        st_folium(customer_map, width=1200, height=600)
```

### Schritt 7.2: Statistiken erweitern

Fügen Sie nach dem Filter hinzu:

```python
    # Erweiterte Statistiken
    with st.expander("📊 Statistiken"):
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Gesamt Kunden", len(customers_df))

        with col2:
            st.metric("Länder", customers_df["country"].nunique())

        with col3:
            geocoded = customers_df["latitude"].notna().sum()
            st.metric("Geocodiert", f"{geocoded}/{len(customers_df)}")

        # Kunden pro Land
        st.subheader("Kunden pro Land")
        country_counts = customers_df["country"].value_counts()
        st.bar_chart(country_counts)
```

### Schritt 7.3: Testen

```bash
□ App starten
□ Filter testen (verschiedene Länder)
□ Prüfen: Tabelle und Karte werden gefiltert
□ Statistiken anschauen
□ Balkendiagramm prüfen
```

### Schritt 7.4: Finaler Commit

```bash
□ git add .
□ git commit -m "✨ feat: Füge Filter und Statistiken hinzu"
□ git push
```

**✅ Checkpoint:** App ist vollständig funktionsfähig!

---

## 🎨 Bonus: Verbesserungen (Optional)

### CSV-Export

```python
# In der Tabellen-Tab
csv = filtered_df.to_csv(index=False)
st.download_button(
    label="📥 Als CSV exportieren",
    data=csv,
    file_name="kunden_export.csv",
    mime="text/csv",
)
```

### CSV-Upload

```python
# In der Sidebar
st.sidebar.header("CSV importieren")
uploaded_file = st.sidebar.file_uploader("CSV-Datei hochladen", type=["csv"])

if uploaded_file:
    import_df = pd.read_csv(uploaded_file)
    # Validierung und Import...
```

### Fehlerbehandlung verbessern

```python
# In save_customer()
if lat is None or lon is None:
    st.warning("⚠️ Koordinaten konnten nicht ermittelt werden. Kunde wird ohne Koordinaten gespeichert.")
```

---

## 🚀 Deployment

### Vorbereitung

```bash
□ Alle Änderungen committen
□ README.md aktualisieren
□ .gitignore prüfen (keine data/customers.csv!)
```

### Streamlit Cloud

```bash
□ Auf https://share.streamlit.io einloggen
□ "New app" klicken
□ Repository auswählen
□ Branch: main
□ Main file: app.py
□ "Deploy!" klicken
```

**Dauer:** 1-2 Minuten

**Ergebnis:** Öffentliche URL (z.B. `https://username-customer-map.streamlit.app`)

---

## 🎉 Geschafft!

Sie haben eine vollständige Streamlit-App entwickelt mit:

- ✅ Dateneingabe und Validierung
- ✅ CSV-Persistenz
- ✅ Geocoding
- ✅ Interaktive Karten-Visualisierung
- ✅ Filter und Statistiken
- ✅ Deployment

### Nächste Schritte

1. **Experimentieren:** Fügen Sie eigene Features hinzu
2. **Teilen:** Zeigen Sie die App Freunden/Kollegen
3. **Erweitern:** Siehe Bonus-Ideen oben
4. **Nächstes Projekt:** [Projekt 2 - SOP-Generator](../projekt-2-sop-generator/)

---

**Herzlichen Glückwunsch! 🎊**

