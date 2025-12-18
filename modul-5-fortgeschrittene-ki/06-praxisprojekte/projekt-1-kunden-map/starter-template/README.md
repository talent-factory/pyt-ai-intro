# 🗺️ Kunden-Adressen Visualisierung

Eine Streamlit-App zur Verwaltung und Visualisierung von Kundenadressen auf einer interaktiven Karte.

## 🚀 Schnellstart

### Installation

```bash
# Dependencies installieren
uv sync --all-extras

# App starten
uv run streamlit run app.py
```

Die App öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📋 Features

- [ ] Kundendaten eingeben (Firma, Adresse, PLZ, Ort, Land)
- [ ] Daten in CSV-Datei speichern
- [ ] Kundenliste anzeigen
- [ ] Adressen in Koordinaten umwandeln (Geocoding)
- [ ] Kunden auf interaktiver Karte visualisieren
- [ ] Nach Land filtern
- [ ] Statistiken anzeigen

## 🛠️ Technologien

- **Python 3.11+**
- **Streamlit** - Web-Framework
- **Pandas** - Datenverarbeitung
- **Folium** - Interaktive Karten
- **Geopy** - Geocoding

## 📁 Projektstruktur

```
customer-map-app/
├── .gitignore
├── pyproject.toml
├── README.md
├── app.py              # Hauptdatei (Streamlit App)
├── data/               # Daten
│   └── .gitkeep
└── utils/              # Hilfsfunktionen
    ├── __init__.py
    ├── geocoder.py     # Geocoding
    └── map_creator.py  # Karten-Erstellung
```

## 📖 Anleitung

Folgen Sie der [Schritt-für-Schritt Anleitung](../ANLEITUNG.md) um die App zu entwickeln.

## 🎯 Nächste Schritte

1. Öffnen Sie `app.py` und beginnen Sie mit Iteration 1
2. Folgen Sie der ANLEITUNG.md
3. Testen Sie nach jedem Schritt
4. Committen Sie regelmässig!

---

**Viel Erfolg! 🎉**

