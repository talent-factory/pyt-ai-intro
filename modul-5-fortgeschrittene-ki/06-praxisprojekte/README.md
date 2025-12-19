# 🚀 Praxisprojekte: Von der Idee zur fertigen App

Dieses Modul bietet einen **praxisorientierten, hands-on Ansatz** zum Programmieren mit Python und Streamlit. Statt theoretischer Konzepte arbeiten wir uns durch **zwei vollständige End-to-End Projekte**, die zeigen, wie aus einzelnen Code-Bausteinen eine funktionierende Anwendung entsteht.

## 🎯 Lernziele

Nach diesem Modul können Sie:

- ✅ Ein Python-Projekt von Grund auf strukturieren
- ✅ Streamlit-Apps mit Dateneingabe und Visualisierung erstellen
- ✅ Code-Snippets aus dem Internet finden und integrieren
- ✅ Den kompletten Entwicklungsworkflow durchlaufen
- ✅ Verstehen, wo und wie Output entsteht
- ✅ Apps deployen und mit anderen teilen

## 📁 Struktur

```text
06-praxisprojekte/
├── README.md                          # Diese Datei
├── SOP-ENTWICKLUNGSWORKFLOW.md        # Standard Operating Procedure
├── projekt-1-kunden-map/              # Hauptprojekt: Kunden-Visualisierung
│   ├── README.md
│   ├── ANLEITUNG.md                   # Schritt-für-Schritt Guide
│   ├── starter-template/              # Leeres Template zum Starten
│   └── musterloesung/                 # Vollständige Lösung
├── projekt-2-sop-generator/           # Bonusprojekt: SOP-Generator
│   ├── README.md
│   ├── ANLEITUNG.md
│   ├── starter-template/
│   └── musterloesung/
├── code-snippets/                     # Wiederverwendbare Code-Bausteine
│   ├── streamlit-basics.md
│   ├── daten-verarbeitung.md
│   ├── visualisierung.md
│   └── file-handling.md
└── troubleshooting/                   # Häufige Probleme und Lösungen
    ├── README.md
    ├── import-errors.md
    ├── file-not-found.md
    └── streamlit-probleme.md
```

## 🎓 Didaktisches Konzept

### 1. Iterative Entwicklung

Jedes Projekt wird in **kleinen, nachvollziehbaren Schritten** entwickelt:

- Schritt 1: Minimale funktionierende Version
- Schritt 2: Feature hinzufügen
- Schritt 3: Testen und committen
- Schritt 4: Nächstes Feature
- **Viele kleine Commits statt einem grossen!**

### 2. "Laut Denken"

Alle Schritte werden erklärt:

- "Warum mache ich das?"
- "Wo finde ich diese Information?"
- "Wie integriere ich diesen Code-Snippet?"
- "Wo erscheint der Output?"

### 3. Fehler als Lernchance

- Absichtlich Fehler machen
- Fehlermeldungen lesen und verstehen
- Lösungen googeln
- Fehler beheben

### 4. Checkpoints

Nach jedem Schritt:

- ✅ Funktioniert es?
- ✅ Verstehe ich, was passiert?
- ✅ Commit erstellen
- ✅ Kurze Pause für Fragen

## 📋 Projekt 1: Kunden-Adressen Visualisierung

**Ziel:** Eine Streamlit-App, die Kundenadressen entgegennimmt und auf einer Karte visualisiert.

**Was Sie lernen:**

- Streamlit Formulare und Dateneingabe
- CSV-Dateien lesen und schreiben
- Geocoding (Adressen → Koordinaten)
- Interaktive Karten mit folium
- Daten nach Region/Land filtern

**Dauer:** 3-4 Stunden

**Schwierigkeitsgrad:** ⭐⭐ Mittel

👉 [Zur Projektanleitung](./projekt-1-kunden-map/README.md)

## 📋 Projekt 2: SOP-Generator

**Ziel:** Eine App, die ein Word-Dokument hochlädt, verarbeitet und als formatierte SOP wieder ausgibt.

**Was Sie lernen:**

- File Upload in Streamlit
- Word-Dokumente lesen und schreiben (python-docx)
- Textverarbeitung und Formatierung
- File Download anbieten

**Dauer:** 1-2 Stunden

**Schwierigkeitsgrad:** ⭐ Einfach

👉 [Zur Projektanleitung](./projekt-2-sop-generator/README.md)

## 📖 Standard Operating Procedure (SOP)

Die **SOP für den Entwicklungsworkflow** ist Ihr roter Faden durch jedes Projekt:

👉 [SOP-ENTWICKLUNGSWORKFLOW.md](./SOP-ENTWICKLUNGSWORKFLOW.md)

Diese Checkliste führt Sie durch:

1. Projekt initialisieren
2. Projektstruktur anlegen
3. Entwicklungsworkflow
4. Code-Snippets integrieren
5. Output verstehen
6. Deployment

## 🧩 Code-Snippets Bibliothek

Häufig verwendete Code-Bausteine, die Sie kopieren und anpassen können:

- **Streamlit Basics:** Formulare, Buttons, Eingabefelder
- **Datenverarbeitung:** CSV, JSON, Pandas
- **Visualisierung:** Karten, Charts, Tabellen
- **File Handling:** Upload, Download, Speichern

👉 [Code-Snippets](./code-snippets/)

## 🔧 Troubleshooting

Häufige Probleme und ihre Lösungen:

- **Import Error:** Dependencies fehlen → `uv sync`
- **File not found:** Pfade prüfen → Absolute vs. relative Pfade
- **Streamlit läuft nicht:** Port bereits belegt → Anderen Port verwenden

👉 [Troubleshooting Guide](./troubleshooting/README.md)

## 🎯 Empfohlener Ablauf

### Für den Kursabend (4 Stunden)

**Block 1: Setup & Grundlagen (60 Min)**

- SOP vorstellen
- Projekt 1 Setup gemeinsam durchführen
- Erste funktionierende Version erstellen

**Block 2: Feature-Entwicklung (90 Min)**

- Dateneingabe implementieren
- Datenverarbeitung hinzufügen
- Visualisierung erstellen
- **Viele kleine Commits!**

**Pause (15 Min)**

**Block 3: Code-Qualität & Deployment (45 Min)**

- Ruff ausführen und Fehler beheben
- Streamlit Cloud Deployment
- **Zeigen: Wo ist der Output?**

**Block 4: Bonus oder Q&A (30 Min)**

- Entweder Projekt 2 starten
- Oder: Offene Fragen, individuelle Probleme

### Für Selbststudium

1. **SOP durchlesen** (15 Min)
2. **Projekt 1 mit Anleitung** (3-4 Stunden)
3. **Projekt 2 selbstständig** (2-3 Stunden)
4. **Eigenes Projekt** (∞ Stunden 😊)

## 💡 Tipps für Dozierende

### Live-Coding Best Practices

1. **Bildschirm aufteilen:**

   - Terminal (Commands)
   - Editor (Code)
   - Browser (Output)
   - File Explorer (Dateien)

2. **Laut denken:**

   - Erklären Sie jeden Schritt
   - Zeigen Sie, wie Sie googeln
   - Lesen Sie Fehlermeldungen vor

3. **Fehler zeigen:**

   - Machen Sie absichtlich Fehler
   - Zeigen Sie, wie man debuggt
   - Normalisieren Sie Fehler als Teil des Prozesses

4. **Checkpoints:**

   - Nach jedem Feature: "Funktioniert es?"
   - Committen
   - Fragen beantworten

### Häufige Stolpersteine

- **"Wo ist der Output?"** → Explizit zeigen (Terminal, Browser, Datei)
- **"Wie passe ich Code-Snippets an?"** → Live demonstrieren
- **"Wo füge ich Code ein?"** → Projektstruktur erklären
- **"Wie bringe ich alles zusammen?"** → Schrittweise aufbauen

## 🎁 Materialien zum Mitnehmen

Nach dem Kurs haben die Teilnehmenden:

- ✅ Zwei vollständige, funktionierende Projekte
- ✅ SOP-Checkliste als Nachschlagewerk
- ✅ Code-Snippets Bibliothek
- ✅ Troubleshooting-Guide
- ✅ Starter-Templates für eigene Projekte

## 🚀 Nächste Schritte

1. **Starten Sie mit der SOP:** [SOP-ENTWICKLUNGSWORKFLOW.md](./SOP-ENTWICKLUNGSWORKFLOW.md)
2. **Wählen Sie ein Projekt:** [Projekt 1](./projekt-1-kunden-map/) oder [Projekt 2](./projekt-2-sop-generator/)
3. **Folgen Sie der Anleitung:** Schritt für Schritt
4. **Experimentieren Sie:** Passen Sie die Projekte an Ihre Bedürfnisse an

---

**Viel Erfolg! 🎉**

Bei Fragen oder Problemen: Troubleshooting-Guide konsultieren oder Dozent fragen.
