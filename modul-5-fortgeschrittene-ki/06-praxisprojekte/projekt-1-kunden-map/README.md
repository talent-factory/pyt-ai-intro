# 🗺️ Projekt 1: Kunden-Adressen Visualisierung

Eine **Streamlit-App**, die Kundenadressen entgegennimmt, speichert und auf einer interaktiven Karte visualisiert.

## 🎯 Lernziele

Nach diesem Projekt können Sie:

- ✅ Streamlit-Formulare erstellen und Daten entgegennehmen
- ✅ CSV-Dateien lesen und schreiben mit Pandas
- ✅ Adressen in Koordinaten umwandeln (Geocoding)
- ✅ Interaktive Karten mit folium erstellen
- ✅ Daten filtern und gruppieren
- ✅ Eine vollständige App von Grund auf entwickeln

## 📸 Screenshots

**Dateneingabe:**
```
┌─────────────────────────────────────┐
│ 🗺️ Kunden-Adressen Visualisierung  │
├─────────────────────────────────────┤
│ Neuen Kunden hinzufügen             │
│                                     │
│ Firmenname: [________________]      │
│ Strasse:    [________________]      │
│ PLZ:        [____]                  │
│ Ort:        [________________]      │
│ Land:       [▼ Schweiz        ]     │
│                                     │
│ [Kunde hinzufügen]                  │
└─────────────────────────────────────┘
```

**Karten-Visualisierung:**
```
┌─────────────────────────────────────┐
│ Alle Kunden (15)                    │
├─────────────────────────────────────┤
│ Filter: [▼ Alle Länder]             │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │        🗺️ Interaktive Karte    │ │
│ │                                 │ │
│ │    📍 Zürich (5 Kunden)         │ │
│ │    📍 Bern (3 Kunden)           │ │
│ │    📍 Basel (2 Kunden)          │ │
│ │                                 │ │
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

## 🚀 Schnellstart

### Voraussetzungen

- Python 3.11 oder höher
- UV Package Manager
- Git

### Installation

```bash
# Repository klonen (oder Starter-Template verwenden)
git clone <your-repo-url>
cd customer-map-app

# Dependencies installieren
uv sync --all-extras

# App starten
uv run streamlit run app.py
```

Die App öffnet sich automatisch im Browser unter `http://localhost:8501`

## 📁 Projektstruktur

```
projekt-1-kunden-map/
├── README.md                   # Diese Datei
├── ANLEITUNG.md               # Schritt-für-Schritt Anleitung
├── starter-template/          # Leeres Template zum Starten
│   ├── .gitignore
│   ├── pyproject.toml
│   ├── README.md
│   ├── app.py                 # Hauptdatei (leer)
│   ├── data/
│   │   └── .gitkeep
│   └── utils/
│       ├── __init__.py
│       ├── geocoder.py        # Geocoding-Funktionen
│       └── map_creator.py     # Karten-Erstellung
└── musterloesung/             # Vollständige Lösung
    ├── .gitignore
    ├── pyproject.toml
    ├── README.md
    ├── app.py                 # Vollständige App
    ├── data/
    │   ├── customers.csv      # Beispieldaten
    │   └── example.csv
    └── utils/
        ├── __init__.py
        ├── geocoder.py
        └── map_creator.py
```

## 🎓 Lernansatz

### Option 1: Geführte Entwicklung (Empfohlen für Anfänger)

1. **Starter-Template verwenden**
2. **ANLEITUNG.md folgen** - Schritt für Schritt
3. **Jeden Schritt selbst umsetzen**
4. **Bei Problemen:** Musterlösung konsultieren

### Option 2: Selbstständige Entwicklung (Fortgeschrittene)

1. **Anforderungen lesen** (siehe unten)
2. **Eigene Lösung entwickeln**
3. **Mit Musterlösung vergleichen**

### Option 3: Code-Review (Lernende mit Erfahrung)

1. **Musterlösung studieren**
2. **Code verstehen und kommentieren**
3. **Eigene Variante entwickeln**

## 📋 Anforderungen

### Muss-Kriterien (Must-Have)

- [ ] **Dateneingabe:** Formular für Kundendaten (Name, Adresse, PLZ, Ort, Land)
- [ ] **Datenspeicherung:** Kunden in CSV-Datei speichern
- [ ] **Datenanzeige:** Liste aller Kunden anzeigen
- [ ] **Geocoding:** Adressen in Koordinaten umwandeln
- [ ] **Karten-Visualisierung:** Kunden auf interaktiver Karte anzeigen
- [ ] **Fehlerbehandlung:** Sinnvolle Fehlermeldungen bei ungültigen Eingaben

### Soll-Kriterien (Should-Have)

- [ ] **Filter:** Kunden nach Land filtern
- [ ] **Statistiken:** Anzahl Kunden pro Land/Region
- [ ] **Validierung:** PLZ und Adresse validieren
- [ ] **Bearbeiten:** Bestehende Kunden bearbeiten
- [ ] **Löschen:** Kunden löschen

### Kann-Kriterien (Nice-to-Have)

- [ ] **CSV-Upload:** Bestehende Kundenliste hochladen
- [ ] **Export:** Gefilterte Liste als CSV exportieren
- [ ] **Clustering:** Kunden nach Regionen gruppieren
- [ ] **Heatmap:** Dichte-Visualisierung
- [ ] **Suche:** Kunden nach Name suchen

## 🛠️ Technologien

- **Python 3.11+**
- **Streamlit** - Web-Framework für Daten-Apps
- **Pandas** - Datenverarbeitung
- **Folium** - Interaktive Karten
- **Geopy** - Geocoding (Adressen → Koordinaten)
- **Streamlit-Folium** - Folium-Integration für Streamlit

## 📚 Ressourcen

### Dokumentation

- [Streamlit Docs](https://docs.streamlit.io)
- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Folium Docs](https://python-visualization.github.io/folium/)
- [Geopy Docs](https://geopy.readthedocs.io/)

### Tutorials

- [Streamlit Tutorial](https://docs.streamlit.io/get-started/tutorials)
- [Folium Quickstart](https://python-visualization.github.io/folium/quickstart.html)

### Code-Snippets

- [../code-snippets/streamlit-basics.md](../code-snippets/streamlit-basics.md)
- [../code-snippets/daten-verarbeitung.md](../code-snippets/daten-verarbeitung.md)
- [../code-snippets/visualisierung.md](../code-snippets/visualisierung.md)

## 🎯 Nächste Schritte

### Für Kursabend (Live-Coding)

1. **Starter-Template kopieren**
2. **ANLEITUNG.md öffnen**
3. **Gemeinsam durcharbeiten**
4. **Viele Commits!**

### Für Selbststudium

1. **ANLEITUNG.md lesen**
2. **Schritt für Schritt umsetzen**
3. **Bei Problemen:** Troubleshooting-Guide
4. **Musterlösung vergleichen**

---

**Los geht's!** 🚀

👉 [Zur Schritt-für-Schritt Anleitung](./ANLEITUNG.md)

