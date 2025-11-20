# GitHub Codespaces Setup

**Zeitaufwand:** 10 Minuten
**Ziel:** Cloud-basierte Entwicklungsumgebung ohne lokale Installation

## 🎯 Was ist GitHub Codespaces?

GitHub Codespaces ist eine **vollständig konfigurierte Cloud-IDE** direkt in deinem Browser:

- ✅ Keine lokale Installation nötig
- ✅ Funktioniert auf jedem Gerät (Windows, Mac, Linux, Tablet)
- ✅ Alle Tools bereits installiert
- ✅ Kostenlos mit GitHub Free Account

---

## 💰 Kostenlos mit GitHub Free Account

### Was du bekommst (ohne zusätzliche Kosten)

| Ressource | Limit |
|-----------|-------|
| **Core-Stunden/Monat** | 120 Stunden* |
| **Storage** | 15 GB |
| **Gleichzeitige Codespaces** | 1 aktiv |
| **Machine Type** | 2-core (Standard) |

*Mit 2-core Machine = **60 Stunden Nutzung** pro Monat = **2 Stunden pro Tag** ✅

### Voraussetzung

- ✅ Kostenloser GitHub Account (privat oder Firma)
- ✅ Keine .edu E-Mail nötig
- ✅ Keine Kreditkarte erforderlich

---

## 🚀 Schnellstart (5 Minuten)

### Schritt 1: GitHub Account (falls noch nicht vorhanden)

1. Gehe zu [github.com](https://github.com)
2. Klicke "Sign up"
3. Registriere mit deiner E-Mail Adresse
4. Verifiziere deine E-Mail

### Schritt 2: Codespace starten (2 Min.)

1. Gehe zum Repository: [github.com/talent-factory/pyt-ai-intro](https://github.com/talent-factory/pyt-ai-intro)
2. Klicke grüner Button **"Code"**
3. Wähle **"Codespaces"** Tab
4. Klicke **"Create codespace on main"**
5. Warte ~2 Minuten auf Initialisierung

### Schritt 3: Testen (1 Min.)

```bash
# Terminal öffnen: Ctrl+` (Backtick)
python --version
# Sollte: Python 3.13.x

# Erstes Programm
echo 'print("Hello from Codespaces!")' > test.py
python test.py
```

---

## ✅ Nach dem Start

### Automatisch installiert

- ✅ Python 3.13
- ✅ Git
- ✅ VS Code Extensions (Python, Copilot, etc.)
- ✅ Alle Dependencies aus `requirements-dev.txt`
- ✅ Alle Kursmaterialien

### Erste Aufgabe zum Testen

```bash
# 1. Terminal öffnen: Ctrl+`
# 2. Erstelle eine interaktive Datei
echo 'name = input("Wie heisst du? ")
print(f"Hallo {name}!")' > hello.py

# 3. Führe aus
python hello.py

# 4. Gib deinen Namen ein
```

---

## 🔄 Codespace verwalten

### Codespace pausieren (WICHTIG: spart Stunden!)

**Immer pausieren wenn du fertig bist!**

1. Gehe zu [github.com/codespaces](https://github.com/codespaces)
2. Klick auf dein Codespace (3 Punkte)
3. Klick **"Stop codespace"**
4. ⏸️ Pausiert = keine Stunden verbraucht

**Oder:** Automatisch nach 30 Minuten Inaktivität

### Codespace fortsetzen

1. Gehe zu [github.com/codespaces](https://github.com/codespaces)
2. Klick auf dein Codespace
3. Startet automatisch (in ~30 Sekunden)

### Codespace löschen

1. [github.com/codespaces](https://github.com/codespaces)
2. Klick **"..."** → **"Delete"**
3. Speichert Speicherplatz

**Hinweis:** Nach 30 Tagen Inaktivität werden Codespaces automatisch gelöscht

---

## 💡 Tipps & Tricks

### Keyboard Shortcuts

- `Ctrl+` ` ` - Terminal öffnen/schliessen
- `Ctrl+Shift+P` - Command Palette
- `Ctrl+/` - Kommentar
- `Ctrl+S` - Speichern (Auto-Save ist aktiviert)
- `Ctrl+B` - Sidebar ein/ausblenden

### GitHub Copilot nutzen

Wenn du GitHub Copilot hast (kostenpflichtig oder über Firma):

- Tippe in `.py` Datei
- Copilot schlägt Code vor
- `Tab` zum Akzeptieren

**Alternative:** Nutze ChatGPT/Claude parallel im Browser

### Port Forwarding

Wenn du einen Server startest (Flask, FastAPI):

```bash
python -m flask run
# Oder
uvicorn main:app --reload
```

→ Codespaces zeigt automatisch einen Link zum Öffnen im Browser

---

## ⚠️ Wichtig: Stunden-Management

### So sparst du Stunden

| Aktion | Spart Stunden? |
|--------|----------------|
| Codespace pausieren | ✅ Ja |
| Browser-Tab schliessen | ❌ Nein (läuft weiter!) |
| Nach 30 Min. Inaktivität | ✅ Pausiert automatisch |
| Mehrere Codespaces parallel | ❌ Verbraucht doppelt |

### Stunden-Verbrauch im Blick behalten

1. Gehe zu [github.com/settings/billing](https://github.com/settings/billing)
2. Unter "Codespaces" siehst du deinen Verbrauch
3. **120 Core-Stunden** = **60 Stunden** mit 2-core Machine

### Wenn Stunden aufgebraucht

- ⏰ Warte bis zum nächsten Monat (Reset am 1. des Monats)
- 💻 Nutze lokale Installation ([Installationsanleitung](./installationsanleitung.md))
- 💰 Optional: Upgrade zu GitHub Pro (~4$/Monat = 180 Stunden)

---

## 🆘 Probleme & Lösungen

| Problem | Lösung |
|---------|--------|
| Codespace startet nicht | Warte 2-3 Min., aktualisiere Seite, versuche neuen Codespace |
| Zu langsam | Schliesse andere Browser-Tabs, pausiere & starte neu |
| Stunden aufgebraucht | Warte bis nächsten Monat oder nutze lokale Installation |
| Python nicht gefunden | Terminal neu öffnen: `Ctrl+Shift+` ` ` |
| Extension fehlt | Öffne Extensions (Ctrl+Shift+X), installiere manuell |
| Git push schlägt fehl | Authentifiziere mit GitHub (folge den Anweisungen) |

---

## 📊 Vergleich: Codespaces vs. Lokal

| Kriterium | Codespaces ☁️ | Lokal 💻 |
|-----------|--------------|---------|
| Installation | Keine | 60-90 Min. |
| Geräte | Alle (inkl. Tablet) | Nur dein Computer |
| Rechenleistung | 2 cores | Deine Hardware |
| Zeitlimit | 60h/Monat | Unbegrenzt |
| Internet nötig | Ja | Nur für Git/KI |
| Kosten | Kostenlos | Kostenlos |

**Empfehlung:** Nutze **beides** - Codespaces für Kursmaterialien, lokal für grössere Projekte.

---

## 📚 Weitere Ressourcen

- [GitHub Codespaces Docs](https://docs.github.com/en/codespaces)
- [Codespaces Quickstart](https://docs.github.com/en/codespaces/getting-started/quickstart)
- [Codespaces Pricing](https://github.com/features/codespaces/pricing)
- [VS Code in Codespaces](https://code.visualstudio.com/docs/remote/codespaces)

---

## ✅ Fertig?

Dein Codespace ist bereit! Du kannst jetzt:

- ✅ Python-Code schreiben und ausführen
- ✅ Git-Befehle nutzen
- ✅ Alle Kursmaterialien bearbeiten
- ✅ Mit KI-Tools arbeiten

**Nächste Schritte:**
- 👉 [Erste Schritte mit KI](./erste-schritte.md)
- 👉 [Leseauftrag](./leseauftrag.md)
- 👉 [Lokale Installation (optional)](./installationsanleitung.md)
