# 📈 Visualisierung - Code-Snippets

## Streamlit Charts

### Line Chart

```python
import streamlit as st
import pandas as pd

# Daten
data = pd.DataFrame({
    "Monat": ["Jan", "Feb", "Mär", "Apr", "Mai"],
    "Umsatz": [1000, 1200, 1100, 1400, 1600]
})

# Line Chart
st.line_chart(data.set_index("Monat"))
```

### Bar Chart

```python
# Bar Chart
st.bar_chart(data.set_index("Monat"))
```

### Area Chart

```python
# Area Chart
st.area_chart(data.set_index("Monat"))
```

## Plotly Charts

### Installation

```toml
# pyproject.toml
dependencies = [
    "plotly>=5.0.0",
]
```

### Line Chart

```python
import plotly.express as px
import streamlit as st

# Daten
df = pd.DataFrame({
    "Monat": ["Jan", "Feb", "Mär", "Apr", "Mai"],
    "Umsatz": [1000, 1200, 1100, 1400, 1600]
})

# Plotly Line Chart
fig = px.line(df, x="Monat", y="Umsatz", title="Umsatz pro Monat")
st.plotly_chart(fig, use_container_width=True)
```

### Bar Chart

```python
# Bar Chart
fig = px.bar(df, x="Monat", y="Umsatz", title="Umsatz pro Monat")
st.plotly_chart(fig, use_container_width=True)
```

### Pie Chart

```python
# Daten
df = pd.DataFrame({
    "Kategorie": ["A", "B", "C", "D"],
    "Wert": [30, 25, 20, 25]
})

# Pie Chart
fig = px.pie(df, values="Wert", names="Kategorie", title="Verteilung")
st.plotly_chart(fig, use_container_width=True)
```

### Scatter Plot

```python
# Daten
df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 3, 5, 6],
    "Kategorie": ["A", "B", "A", "B", "A"]
})

# Scatter Plot
fig = px.scatter(
    df, 
    x="x", 
    y="y", 
    color="Kategorie",
    title="Scatter Plot"
)
st.plotly_chart(fig, use_container_width=True)
```

## Folium Karten

### Installation

```toml
# pyproject.toml
dependencies = [
    "folium>=0.15.0",
    "streamlit-folium>=0.15.0",
]
```

### Einfache Karte

```python
import folium
from streamlit_folium import st_folium

# Karte erstellen (Schweiz)
m = folium.Map(
    location=[46.8182, 8.2275],  # Lat, Lon
    zoom_start=7
)

# In Streamlit anzeigen
st_folium(m, width=700, height=500)
```

### Marker hinzufügen

```python
# Karte erstellen
m = folium.Map(location=[47.3769, 8.5417], zoom_start=13)

# Marker hinzufügen
folium.Marker(
    location=[47.3769, 8.5417],
    popup="Zürich Hauptbahnhof",
    tooltip="Zürich HB",
    icon=folium.Icon(color="blue", icon="train", prefix="fa")
).add_to(m)

# Anzeigen
st_folium(m, width=700, height=500)
```

### Mehrere Marker

```python
import pandas as pd

# Daten
locations = pd.DataFrame({
    "name": ["Zürich", "Bern", "Basel"],
    "lat": [47.3769, 46.9480, 47.5596],
    "lon": [8.5417, 7.4474, 7.5886]
})

# Karte erstellen
m = folium.Map(location=[46.8182, 8.2275], zoom_start=7)

# Marker hinzufügen
for _, row in locations.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=row["name"],
        tooltip=row["name"]
    ).add_to(m)

# Anzeigen
st_folium(m, width=700, height=500)
```

### Popup mit HTML

```python
# HTML-Popup
popup_html = f"""
<div style="font-family: Arial; width: 200px;">
    <h4>{row['name']}</h4>
    <p><b>Einwohner:</b> {row['population']}</p>
    <p><b>Kanton:</b> {row['canton']}</p>
</div>
"""

folium.Marker(
    location=[row["lat"], row["lon"]],
    popup=folium.Popup(popup_html, max_width=250),
    tooltip=row["name"]
).add_to(m)
```

### Verschiedene Marker-Icons

```python
# Icon-Optionen
colors = ["red", "blue", "green", "purple", "orange", "darkred", 
          "lightred", "beige", "darkblue", "darkgreen", "cadetblue", 
          "darkpurple", "white", "pink", "lightblue", "lightgreen", 
          "gray", "black", "lightgray"]

icons = ["info-sign", "home", "star", "heart", "flag", "bookmark",
         "phone", "envelope", "cloud", "user", "building", "map-marker"]

# Marker mit Icon
folium.Marker(
    location=[47.3769, 8.5417],
    popup="Zürich",
    icon=folium.Icon(color="red", icon="star", prefix="fa")
).add_to(m)
```

### Circle Marker

```python
# Circle Marker
folium.CircleMarker(
    location=[47.3769, 8.5417],
    radius=10,
    popup="Zürich",
    color="red",
    fill=True,
    fillColor="red",
    fillOpacity=0.6
).add_to(m)
```

### Heatmap

```python
from folium.plugins import HeatMap

# Daten (lat, lon, weight)
heat_data = [
    [47.3769, 8.5417, 1.0],
    [46.9480, 7.4474, 0.8],
    [47.5596, 7.5886, 0.6],
]

# Heatmap hinzufügen
HeatMap(heat_data).add_to(m)
```

## Metriken

### Einfache Metrik

```python
import streamlit as st

st.metric(
    label="Temperatur",
    value="25°C"
)
```

### Metrik mit Delta

```python
st.metric(
    label="Umsatz",
    value="€1.2M",
    delta="€200K"  # Positiv (grün)
)

st.metric(
    label="Kosten",
    value="€800K",
    delta="-€50K"  # Negativ (rot)
)
```

### Mehrere Metriken

```python
col1, col2, col3 = st.columns(3)

col1.metric("Kunden", "1,234", "+12%")
col2.metric("Umsatz", "€56K", "+8%")
col3.metric("Gewinn", "€12K", "-3%")
```

## Progress Bars

### Progress Bar

```python
import time

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(100):
    progress_bar.progress(i + 1)
    status_text.text(f"Fortschritt: {i+1}%")
    time.sleep(0.01)

status_text.text("Fertig!")
```

### Spinner

```python
with st.spinner("Lädt Daten..."):
    time.sleep(2)
    # Daten laden
st.success("Daten geladen!")
```

---

**Tipp:** Verwenden Sie `use_container_width=True` bei Charts für responsive Darstellung!

