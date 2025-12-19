# 🗺️ Kunden-Adressen Visualisierung - Musterlösung

Dies ist die **vollständige Musterlösung** für Projekt 1.

## 🚀 Schnellstart

```bash
# Dependencies installieren
uv sync --all-extras

# App starten
uv run streamlit run app.py
```

## ✨ Features

- ✅ Kundendaten eingeben (Firma, Adresse, PLZ, Ort, Land)
- ✅ Daten in CSV-Datei speichern
- ✅ Kundenliste anzeigen
- ✅ Adressen in Koordinaten umwandeln (Geocoding)
- ✅ Kunden auf interaktiver Karte visualisieren
- ✅ Nach Land filtern
- ✅ Statistiken anzeigen
- ✅ CSV-Export

## 📁 Projektstruktur

```
musterloesung/
├── .gitignore
├── pyproject.toml
├── README.md
├── app.py                 # Hauptdatei (vollständig)
├── data/
│   └── example.csv        # Beispieldaten
└── utils/
    ├── __init__.py
    ├── geocoder.py        # Geocoding-Funktionen
    └── map_creator.py     # Karten-Erstellung
```

## 🎓 Verwendung

### Als Referenz

Nutzen Sie diese Lösung als Referenz, wenn Sie bei der Entwicklung nicht weiterkommen.

### Zum Vergleichen

Vergleichen Sie Ihre eigene Lösung mit dieser Musterlösung:
- Welche Ansätze sind ähnlich?
- Welche Unterschiede gibt es?
- Was können Sie verbessern?

### Zum Lernen

Studieren Sie den Code:
- Wie ist die App strukturiert?
- Wie funktioniert das Geocoding?
- Wie wird die Karte erstellt?

## 💡 Wichtige Code-Teile

### Geocoding

<augment_code_snippet path="modul-5-fortgeschrittene-ki/06-praxisprojekte/projekt-1-kunden-map/musterloesung/utils/geocoder.py" mode="EXCERPT">
````python
def geocode_address(street, zip_code, city, country):
    """Wandelt Adresse in Koordinaten um."""
    address = f"{street}, {zip_code} {city}, {country}"
    location = geolocator.geocode(address, timeout=10)
    ...
````
</augment_code_snippet>

### Karten-Erstellung

<augment_code_snippet path="modul-5-fortgeschrittene-ki/06-praxisprojekte/projekt-1-kunden-map/musterloesung/utils/map_creator.py" mode="EXCERPT">
````python
def create_customer_map(customers_df):
    """Erstellt eine Karte mit allen Kunden."""
    m = folium.Map(location=[center_lat, center_lon], zoom_start=7)
    ...
````
</augment_code_snippet>

## 🔧 Erweiterungsideen

Möchten Sie die App erweitern? Hier sind einige Ideen:

1. **Clustering:** Gruppiere nahe Kunden zu Clustern
2. **Heatmap:** Zeige Dichte-Visualisierung
3. **Suche:** Suche Kunden nach Name
4. **Bearbeiten:** Bestehende Kunden bearbeiten
5. **CSV-Upload:** Kundenliste hochladen
6. **Export-Formate:** Excel, JSON zusätzlich zu CSV
7. **Routing:** Zeige Route zwischen Kunden
8. **Notizen:** Füge Notizen zu Kunden hinzu

## 📚 Weiterführende Ressourcen

- [Streamlit Docs](https://docs.streamlit.io)
- [Folium Docs](https://python-visualization.github.io/folium/)
- [Geopy Docs](https://geopy.readthedocs.io/)

---

**Viel Erfolg beim Lernen! 🎉**

