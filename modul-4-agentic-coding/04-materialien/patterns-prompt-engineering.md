# Prompting-Patterns

**Autor:** Prof. Dr. Tobias Häberlein
**Quelle:** Basierend auf «The Prompt Report: A Systematic Survey of Prompt Engineering Techniques»

> **📖 Vollständige Dokumentation:** Dieses Dokument enthält eine Übersicht der 21 wissenschaftlich fundierten Prompting-Patterns. Die vollständige, druckbare Version mit ausführlicher Erklärung aller Patterns finden Sie in der **Kursdokumentation (PDF)** im Kapitel **Modul 4: Agentic Coding -- KI-gestützte Entwicklung**, Abschnitt **Wissenschaftliche Prompting-Patterns**.

## Inhaltsverzeichnis

1. [Vorwort](#vorwort)
2. [Einleitung](#einleitung)
3. [Systematik dieses Dokuments](#systematik-dieses-dokuments)
4. [Grundlegende Patterns](#grundlegende-patterns)
5. [Few-Shot / Zero-Shot-Prompting Patterns](#few-shot--zero-shot-prompting-patterns)
6. [Thought Generation Patterns](#thought-generation-patterns)
7. [Decomposition Patterns](#decomposition-patterns)
8. [Ensembling Patterns](#ensembling-patterns)
9. [Selbstkritik Patterns](#selbstkritik-patterns)
10. [Schlussbemerkungen](#schlussbemerkungen)
11. [Literatur](#literatur)

---

## Vorwort

Die rasante Entwicklung grosser Sprachmodelle (Large Language Models, LLMs) verändert nicht nur die Art wie wir arbeiten, sondern auch die Art wie wir denken, kommunizieren und gestalten. In einer Zeit, in der künstliche Intelligenz zunehmend als kreativer und analytischer Partner agiert, wird es entscheidend, die Sprache der Sprachmodelle zu verstehen: das Prompting.

Dieses Dokument basiert auf dem wissenschaftlichen Überblick «The Prompt Report: A Systematic Survey of Prompt Engineering Techniques» [1] der wiederum auf zentralen Erkenntnissen der letzten Jahre über Prompting-Techniken [2], [3], [4], [5], [6], [7] basiert. Daraus abgeleitet wird eine strukturierte Sammlung von Prompting-Patterns vorgestellt – bewährte Techniken, um mit LLMs effektiv zu interagieren. Die Patterns reichen von einfachen Rollenwechseln über mehrstufige Denkprozesse bis hin zu selbstkritischen Iterationen.

### Warum ist eine solche Sammlung von Prompting-Patterns wichtig?

Weil unsere Studierenden – und wir alle – künftig nicht mehr nur Software-Werkzeuge bedienen werden, sondern mit ihnen sprechen und gemeinsam mit ihnen in Co-Creation-Prozessen arbeiten werden. Wer diese Werkzeuge nur oberflächlich nutzt, schöpft ihr Potenzial nicht aus. Wer sich bewusst ist, wie LLMs Kontext verarbeiten [8], [9] und versteht, wie Prompts gestaltet sein müssen, kann die Intelligenz, Kreativität und Analysefähigkeiten von LLMs aktiv für eigene Ziele einsetzen – im Studium, im Beruf, in der Forschung.

Gleichzeitig gilt: Nur durch eigene Exploration kann man die Grenzen und Fähigkeiten dieser Systeme wirklich einschätzen. Dieses Dokument lädt daher nicht nur zum Nachlesen ein, sondern ist auch eine Aufforderung zur aktiven Erprobung. Denn nur wer selbst promptet, versteht, was möglich ist und was nicht.

---

## Einleitung

«Prompting» bezeichnet die Kunst, mit einem grossen Sprachmodell (LLM) so zu kommunizieren, dass es zielgerichtete, hilfreiche und qualitativ hochwertige Antworten liefert. Diese Fähigkeit ist zentral für den effektiven Einsatz von moderner generativer KI – sei es im Studium, in der Arbeitswelt oder im privaten Alltag.

Mit dem zunehmenden Einsatz von LLMs verändert sich die Interaktion mit digitalen Systemen grundlegend: Statt starre Befehle auszuführen, interpretieren diese Modelle unsere Anfragen flexibel im Kontext. Doch gerade diese Offenheit erfordert präzise und strategisch aufgebaute Prompts. Wer die richtigen Techniken kennt, kann das volle Potenzial dieser Systeme ausschöpfen.

Dieses Dokument bietet dafür eine praktische Anleitung. Es stellt bewährte Prompting-Patterns vor – also wiederverwendbare Denk- und Handlungsstrukturen, die sich in der Arbeit mit LLMs bewährt haben. Ziel ist es, diese Muster verständlich, anwendbar und adaptierbar zu machen – auch für Personen ohne technische Vorkenntnisse.

---

## Systematik dieses Dokuments

Die folgenden Kapitel sind nach 21 Prompting-Patterns strukturiert, die sich in der wissenschaftlichen Literatur (insbesondere im «Prompt Report», Schulhoff et al., 2024) als besonders wirkungsvoll herausgestellt haben.

**Jedes Pattern wird im gleichen Format dargestellt:**

- **Bezeichnung und Kürzel**
- **Kurzbeschreibung**
- **Warum dieses Pattern wirkt**
- **Geeignet für…** (Anwendungskontexte)
- **Beispielhafter Prompt**

Die Patterns sind thematisch gruppiert – von grundlegenden Mustern über Denkprozesse (Chain-of-Thought) bis hin zu komplexeren Selbstreflexions- und Ensembling-Techniken. Ziel ist es, Leserinnen und Leser zu befähigen, diese Muster aktiv in eigenen Prompts zu erproben und zu variieren.

---

## Grundlegende Patterns

### Pattern A: Persona

#### Kurzbeschreibung

Das Modell wird angewiesen, in der Rolle einer bestimmten Person oder Berufsgruppe zu antworten («Handle als…»). Dies ermöglicht spezifischere, stilistisch und inhaltlich passendere Antworten.

#### Warum dieses Pattern wirkt

LLMs sind besonders gut darin, sprachliche Muster und Rollenbilder zu imitieren. Durch die Zuweisung einer Persona wird das Modell in einen kontextsensitiven Modus versetzt – es passt Tonalität, Argumentation und Fokus entsprechend an.

#### Geeignet für

- Perspektivwechsel
- Rollenspiele (z. B. Coach, Jurist, Historikerin)
- Kreatives Schreiben

#### Beispiel-Prompt

```text
Du bist ein erfahrener HR-Coach. Wie würdest du eine junge Führungskraft auf ein schwieriges Mitarbeitergespräch vorbereiten?
```

---

### Pattern B: Reverse Interaction

#### Kurzbeschreibung

Das Modell übernimmt die aktive Rolle, indem es Fragen an die Benutzerin oder den Benutzer stellt, um ein Ziel besser zu verstehen oder gemeinsam zu erarbeiten.

#### Warum dieses Pattern wirkt

Reverse Interaction bringt LLMs in eine dialogische Haltung und ermöglicht eine fokussierte Exploration eines Themas – interaktiv und iterativ.

#### Geeignet für

- Beratungssituationen
- Explorative Analyse
- Gemeinsame Lösungsfindung

#### Beispiel-Prompt

```text
Ich möchte eine neue Geschäftsidee entwickeln. Stelle mir bitte Fragen, um meine Gedanken zu strukturieren und das Potenzial zu bewerten.
```

---

## Few-Shot / Zero-Shot-Prompting Patterns

### Pattern C: Few-Shot-Prompting

#### Kurzbeschreibung

Dem Modell werden ein bis wenige Beispiele mitgegeben, um den gewünschten Stil oder die Struktur zu zeigen. Das Modell lernt am Beispiel.

#### Warum dieses Pattern wirkt

LLMs imitieren stark die ihnen gezeigten Muster. Wenige gut gewählte Beispiele können reichen, um das Modell in eine gewünschte Richtung zu lenken. Das unterscheidet LLMs und generative KI deutlich vom «klassischen» Machine Learning, wo man i.A. hunderte oder tausende Beispiele braucht um zu lernen.

#### Geeignet für

- Formatierte Ausgaben (z. B. Tabellen, Bullet-Points)
- Textsorten mit klarer Struktur
- Klassifikationen

#### Beispiel-Prompt 1 (Klassifikation)

```text
Text: „Ich liebe diesen Film – die Schauspieler waren grossartig!" → Sentiment: Positiv
Text: „Die Lieferung kam verspätet und das Produkt war beschädigt." → Sentiment: Negativ
Text: „Das Essen war okay, aber nichts Besonderes." → Sentiment: Neutral
Text: „Das Hotel war fantastisch – ich komme wieder!" → Sentiment: ?
```

#### Beispiel-Prompt 2 (Tabellen, Struktur)

```text
Land: Deutschland, Hauptstadt: Berlin, Einwohner: ca. 83 Mio.
Land: Frankreich, Hauptstadt: Paris, Einwohner: ca. 67 Mio.
Land: Italien, …
```

---

### Pattern D: System-2 Attention

#### Kurzbeschreibung

Fordere das Modell auf, irrelevante Informationen im Prompt zu entfernen, bevor es mit der eigentlichen Aufgabe beginnt. Dadurch wird die Aufmerksamkeit auf das Wesentliche gelenkt.

#### Warum dieses Pattern wirkt

LLMs reagieren empfindlich auf Kontextfülle. Die aktive Reduktion auf relevante Informationen aktiviert fokussierteres «Denken» im Modell.

#### Geeignet für

- Lange, unstrukturierte Inputs
- Komplexe Fragen mit Nebenaspekten
- Analyse von Informationsdichte

#### Beispiel-Prompt

```text
Bitte entferne zuerst alle irrelevanten Informationen aus folgendem Text. Danach beantworte die Frage am Ende. Text: …
```

---

### Pattern E: Rephrase & Respond (R&R)

#### Kurzbeschreibung

Das Modell wird gebeten, den Input zuerst umzuformulieren und zu erweitern, bevor es eine Antwort generiert.

#### Warum dieses Pattern wirkt

Durch die Umformulierung klärt das Modell implizite Lücken, strukturiert Gedanken vor und verbessert so oft die Qualität der Antwort.

#### Geeignet für

- Unklare, vage Fragen
- Optimierung bestehender Prompts
- Co-Prompting

#### Beispiel-Prompt

```text
Formuliere meine folgende Frage um und beantworte sie dann. Frage: «Wie kann ich besser lernen?»
```

---

### Pattern F: Re-Read (RE2)

#### Kurzbeschreibung

Füge dem Prompt die explizite Anweisung hinzu, die Frage nochmals zu lesen («Lies die Frage nochmals, bevor du antwortest»).

#### Warum dieses Pattern wirkt

Diese einfache Metakognition steigert die Antwortgenauigkeit, besonders bei komplexen oder mehrteiligen Aufgaben.

#### Geeignet für

- Prüfungsähnliche Fragestellungen
- Missverständliche Prompts
- Mehrstufige Probleme

#### Beispiel-Prompt

```text
Lies die folgende Frage nochmals sorgfältig durch, bevor du antwortest: «…»
```

---

### Pattern G: Self-Ask

#### Kurzbeschreibung

Das Modell wird angewiesen, selbst zu entscheiden, ob Zwischenfragen nötig sind. Falls ja, generiert es diese Fragen, beantwortet sie und kehrt dann zur Hauptfrage zurück.

#### Warum dieses Pattern wirkt

Self-Ask aktiviert mehrstufiges Denken und reflektierte Problemzerlegung – das Modell wird zum «selbstkritischen» Bearbeiter.

#### Geeignet für

- Komplexe, mehrdeutige Aufgabenstellungen
- Analyse- und Argumentationsprozesse
- Exploratives Schreiben

#### Beispiel-Prompt

```text
Wenn du denkst, dass Zwischenfragen nötig sind, stelle sie dir bitte selbst, beantworte sie, und gib dann eine fundierte Antwort auf die Hauptfrage.
```

---

## Thought Generation Patterns

### Pattern H: Chain-of-Thought Prompting (CoT)

#### Kurzbeschreibung

Dieses Pattern fordert das Modell dazu auf, seine Antwort schrittweise herzuleiten, anstatt sofort eine Lösung oder Aussage zu präsentieren. Dies kann entweder mit Beispielen (Few-Shot) oder durch einleitende Formulierungen wie «Lass uns Schritt für Schritt denken» (Zero-Shot) erreicht werden.

#### Warum dieses Pattern wirkt

Gemäss Schulhoff et al. (2024) aktiviert CoT die Fähigkeit von LLMs, mehrere Denkoperationen in Serie auszuführen. Anstatt eine «Black Box»-Antwort zu liefern, durchläuft das Modell einen argumentativen Pfad, wodurch Transparenz, Genauigkeit und Nachvollziehbarkeit steigen – besonders bei logischen, mathematischen oder komplexen Aufgabenstellungen.

#### Geeignet für

- Mathematische Probleme
- Logik- und Argumentationsaufgaben
- Aufgaben mit mehreren Teilaspekten

#### Beispiel-Prompt

```text
Lass uns die folgende Frage Schritt für Schritt durchdenken: «Wie hoch ist die jährliche Rendite bei 5 % Zinsen über 3 Jahre mit Zinseszins?»
```

---

### Pattern I: Step-Back Prompting

#### Kurzbeschreibung

Das Modell wird zunächst gebeten, eine übergeordnete oder kontextualisierende Frage zu beantworten, bevor es sich der eigentlichen Aufgabe widmet. So entsteht ein «geistiger Anlauf» zur Lösung.

#### Warum dieses Pattern wirkt

Diese Technik nutzt die Fähigkeit von LLMs zur Top-down-Dekonstruktion: Wenn ein Problem zunächst in ein abstrakteres Konzept oder einen allgemeineren Rahmen gestellt wird, kann das Modell systematischer und reflektierter antworten. Dies erhöht besonders bei konzeptuell schwierigen Fragen die Relevanz und Tiefe der Antwort.

#### Geeignet für

- Theoretische oder konzeptionelle Themen
- Lernunterstützung
- Transferaufgaben (z. B. «Was bedeutet X in einem anderen Kontext?»)

#### Beispiel-Prompt

```text
Bevor du die Frage direkt beantwortest, erkläre mir bitte zuerst, worum es bei diesem Thema grundsätzlich geht. Danach beantworte die konkrete Frage: «…»
```

---

### Pattern J: Automatic Chain-of-Thought (Auto-CoT)

#### Kurzbeschreibung

Das Modell wird ohne Beispiele angewiesen, automatisch eine schrittweise Argumentation zu generieren, die einem Chain-of-Thought ähnelt. Der CoT-Prozess wird also direkt durch einen Prompt ausgelöst – meist mit einfachen Signalphrasen.

#### Warum dieses Pattern wirkt

Gemäss der Analyse von Schulhoff et al. nutzt Auto-CoT die Tendenz von LLMs, auf sprachliche Muster wie «Lass uns gemeinsam darüber nachdenken…» mit strukturierten Gedankengängen zu reagieren. Das ermöglicht Zero-Shot-Reasoning mit hoher Effizienz – besonders dann, wenn keine Beispiele verfügbar sind.

#### Geeignet für

- Schnelle Anwendung ohne Few-Shot-Beispiele
- Spontane Problemlösung
- Exploratives Denken in offenen Aufgaben

#### Beispiel-Prompt

```text
Beantworte die folgende Frage Schritt für Schritt. Denke zuerst laut nach: «Warum gibt es Jahreszeiten auf der Erde?»
```

---

### Pattern K: Thread-of-Thought (ThoT) Prompting

#### Kurzbeschreibung

Dieses Pattern leitet das Modell an, einen langen oder komplexen Kontext in kleinen Portionen zu verarbeiten, dabei jeweils kurz zusammenzufassen und gedanklich weiterzuentwickeln. So entsteht ein «Denkfaden» durch den Text.

#### Warum dieses Pattern wirkt

Laut Schulhoff et al. (2024) ist ThoT besonders wirksam, wenn grosse Mengen an Kontextinformation vorhanden sind. Die sequentielle Verarbeitung in überschaubaren Einheiten fördert die Kohärenz des Verständnisses und führt zu höherer Texttreue und Präzision, besonders bei Retrieval-Aufgaben oder langen Quellen.

#### Geeignet für

- Lange Texte oder Dokumente
- Recherche- oder Analyseaufgaben
- Kontextualisierte Frage-Antwort-Systeme

#### Beispiel-Prompt

```text
Führe mich bitte abschnittsweise durch folgenden Text. Nach jedem Teil: kurze Zusammenfassung, kurze Analyse. Beginne mit: «…»
```

---

## Decomposition Patterns

### Pattern L: Least-to-Most Prompting

#### Kurzbeschreibung

Das Modell wird zunächst aufgefordert, ein Problem in kleinere Teilprobleme zu zerlegen, ohne sie sofort zu lösen. Anschliessend werden die Teilprobleme nacheinander abgearbeitet.

#### Warum dieses Pattern wirkt

Diese Technik zwingt das Modell dazu, explizite Problemanalyse und Planung zu betreiben – ein Vorgehen, das sich besonders in symbolischen, mathematischen und logischen Kontexten als effektiv erwiesen hat. Die sequentielle Bearbeitung verhindert zudem, dass der Kontext verloren geht oder vorschnelle Schlüsse gezogen werden.

#### Geeignet für

- Mathematische Aufgaben
- Algorithmische Probleme
- Strategische Entscheidungsfindung

#### Beispiel-Prompt

```text
Zerlege folgendes Problem in kleinere Schritte, ohne sie zu lösen: «…» Danach: Löse die Teilaufgaben Schritt für Schritt.
```

---

### Pattern M: DECOMP

#### Kurzbeschreibung

Das Modell erhält anhand einiger Beispiele gezeigt, wie es ein grösseres Problem mithilfe bestimmter Hilfsfunktionen oder Werkzeuge (z. B. String-Splitting, Suchabfragen) in Teilaufgaben aufteilt und diese bearbeitet.

#### Warum dieses Pattern wirkt

DECOMP erweitert die Fähigkeiten des Modells durch die explizite Anbindung an Methoden oder «Funktionen» – entweder implizit über Sprachmuster oder explizit durch Tool-Use (in agentischen Systemen). Laut Prompt Report fördert dies die funktionale Modularisierung komplexer Aufgaben.

#### Geeignet für

- Aufgaben mit mehreren Methodenanteilen
- Prompt-Ketten oder Tool-gestützte Antworten
- Kontextsensitive Analysen

#### Beispiel-Prompt

```text
Hier ein Beispiel, wie du eine Aufgabe mithilfe von «Suche nach Informationen» und «Text extrahieren» lösen kannst. Jetzt wende dieses Muster auf folgendes Problem an: «…»
```

---

### Pattern N: Plan-and-Solve Prompting

#### Kurzbeschreibung

Das Modell wird zunächst gebeten, einen Plan zur Lösung eines Problems zu erstellen, bevor es diesen systematisch umsetzt.

#### Warum dieses Pattern wirkt

Dieses Pattern erhöht die Kohärenz und Zielgerichtetheit des Antwortprozesses. Anstatt direkt zu «raten», wird ein strukturierter Denkprozess angestossen – vergleichbar mit einer Selbstanleitung. Besonders bei reasoning-intensiven Aufgaben zeigt sich ein Performancegewinn.

#### Geeignet für

- Komplexe Entscheidungsfragen
- Argumentationen
- Multistep-Fragen

#### Beispiel-Prompt

```text
Lass uns das Problem gemeinsam lösen. Zuerst: Entwickle einen Plan zur Lösung. Dann: Führe diesen Plan Schritt für Schritt aus. Aufgabe: «…»
```

---

### Pattern O: Tree-of-Thought (ToT) Prompting

#### Kurzbeschreibung

Das Modell wird angeleitet, mehrere gedankliche Lösungswege gleichzeitig zu entwickeln. Diese bilden einen baumartigen Entscheidungsraum, in dem nach und nach der beste Pfad ausgewählt wird.

#### Warum dieses Pattern wirkt

ToT ist eine Weiterentwicklung von CoT und nutzt laut Prompt Report die Fähigkeit von LLMs zur Simultansimulation mehrerer Pfade. Statt linearer Argumentation entstehen verzweigte Denkstrukturen, was sich besonders bei kreativen, offenen oder suchbasierten Aufgaben als leistungsfähig erwiesen hat.

#### Geeignet für

- Entscheidungsfindung mit Alternativen
- Kreative Problemlösungen
- Strategieentwicklung

#### Beispiel-Prompt

```text
Erstelle verschiedene Denkansätze, wie man das folgende Problem lösen könnte. Bewerte danach, welcher Ansatz am meisten zur Lösung beiträgt. Problem: «…»
```

---

### Pattern P: Recursion-of-Thought

#### Kurzbeschreibung

Dieses Pattern erlaubt es dem Modell, Teilprobleme innerhalb einer CoT-Struktur erneut einem eigenen Denkprozess zu unterziehen – eine Art «verschachteltes Denken».

#### Warum dieses Pattern wirkt

Recursion-of-Thought ist besonders bei komplexen oder verschachtelten Aufgaben hilfreich, da es erlaubt, gedanklich zurückzutreten und gezielt Subfragen zu behandeln. Laut Schulhoff et al. führt diese rekursive Tiefe zu besserer Lösungsqualität, auch bei längeren Kontexten oder algorithmischen Herausforderungen.

#### Geeignet für

- Mehrstufige Logikprobleme
- Algorithmen und technische Aufgaben
- Aufgaben mit hoher Komplexität

#### Beispiel-Prompt

```text
Wenn während deiner Argumentation ein komplizierter Zwischenschritt auftaucht, halte inne, analysiere diesen Schritt gesondert, löse ihn und setze dann den ursprünglichen Denkprozess fort.
```

---

### Pattern Q: Program-of-Thoughts

#### Kurzbeschreibung

Das Modell wird aufgefordert, Code als Denkwerkzeug zu nutzen. Es schreibt dabei kurze Programme oder Anweisungen, um Probleme zu analysieren oder zu lösen – besonders effektiv bei numerischen und logischen Aufgaben.

#### Warum dieses Pattern wirkt

Laut Schulhoff et al. aktivieren LLMs bei dieser Technik eine formalisierte Form der Argumentation. Durch die Transformation von Gedanken in Programmcode entstehen präzise, nachvollziehbare und wiederholbare Lösungswege – ideal für Aufgaben, bei denen Klarheit und Struktur dominieren.

#### Geeignet für

- Mathematische und technische Probleme
- Rechenoperationen
- Logik und Simulation

#### Beispiel-Prompt

```text
Schreibe ein kleines Python-Programm, das folgende Fragestellung bearbeitet: «Wie viel kostet ein Darlehen von 10'000 CHF bei 3 % Zins über 5 Jahre mit jährlicher Rückzahlung?»
```

---

## Ensembling Patterns

### Pattern R: Self-Consistency

#### Kurzbeschreibung

Das Modell wird mehrfach mit demselben Prompt (oder leicht variierten Versionen) angesprochen. Die daraus resultierenden Antworten werden anschliessend miteinander verglichen, um einen Mehrheitsentscheid zu bilden.

#### Warum dieses Pattern wirkt

LLMs sind nicht deterministisch – sie generieren je nach Temperatureinstellung unterschiedliche, aber plausible Antworten. Dieses Pattern nutzt diese Eigenschaft produktiv: Durch die Erzeugung mehrerer Denkpfade (meist im CoT-Stil) und anschliessende Konsolidierung lässt sich eine robustere, weniger zufällige Antwort erzeugen. Studien (Schulhoff et al.) zeigen signifikante Verbesserungen bei mathematischem und logischem Reasoning.

#### Geeignet für

- Aufgaben mit hohem Unsicherheitsfaktor
- Kritische Entscheidungsprozesse
- Stabilisierung von CoT-Antworten

#### Beispiel-Prompt

```text
Löse dieses Problem mehrfach mit unterschiedlichen Denkansätzen und gib dann die Antwort, die am häufigsten vorkommt. Aufgabe: «…»
```

---

### Pattern S: Prompt Paraphrasing

#### Kurzbeschreibung

Der ursprüngliche Prompt wird in mehreren Varianten umformuliert, ohne die inhaltliche Intention zu verändern. Diese Varianten werden alle verwendet, um das Modell zu befragen, und die Resultate werden verglichen oder aggregiert.

#### Warum dieses Pattern wirkt

Prompt Paraphrasing wirkt wie eine Data-Augmentation-Technik: Durch leicht unterschiedliche Formulierungen wird die Antwortrobustheit verbessert und das Modell weniger anfällig für Prompt-Sensitivität. Gemäss Schulhoff et al. reduziert diese Methode das Risiko von Missverständnissen durch sprachliche Nuancen und steigert die Verlässlichkeit der Ergebnisse.

#### Geeignet für

- Evaluierung von Prompt-Stabilität
- Kombination mit Self-Consistency
- Nutzung im Prompt-Testing

#### Beispiel-Prompt

```text
Formuliere folgende Frage in drei leicht unterschiedlichen Varianten. Nutze dann jede Variante, um das Problem zu lösen, und vergleiche die Antworten: «…»
```

---

## Selbstkritik Patterns

### Pattern T: Self-Calibration

#### Kurzbeschreibung

Das Modell wird gebeten, seine eigene Antwort kritisch zu überprüfen. Dazu wird die ursprüngliche Aufgabe samt generierter Antwort in einen neuen Prompt eingebettet, in dem das Modell bewertet, ob die Antwort korrekt und sinnvoll ist.

#### Warum dieses Pattern wirkt

LLMs verfügen über ein gewisses Mass an Meta-Urteilsvermögen. Durch Self-Calibration kann das Modell gezielt zur Reflexion gebracht werden, was die Verlässlichkeit und Selbsteinschätzung verbessert. Laut Prompt Report hilft dies nicht nur zur Fehlersuche, sondern auch zur Kalibrierung von Unsicherheit (Confidence Assessment).

#### Geeignet für

- Qualitätskontrolle von Modellantworten
- Nachbearbeitung sensibler Inhalte
- Prüfungs- oder Feedbackszenarien

#### Beispiel-Prompt

```text
Hier ist eine Antwort auf eine Frage. Bitte bewerte: Ist diese Antwort korrekt und konsistent mit der ursprünglichen Frage? Falls nein, worin liegt der Fehler?
```

---

### Pattern U: Self-Refine

#### Kurzbeschreibung

Das Modell wird nach einer ersten Antwort aufgefordert, Feedback zu geben und darauf basierend eine verbesserte Version zu erstellen. Dieser Zyklus kann bei Bedarf mehrfach wiederholt werden.

#### Warum dieses Pattern wirkt

Self-Refine kombiniert Kritikfähigkeit und Überarbeitung – ähnlich wie menschliches Redigieren. In Experimenten (Schulhoff et al.) führte dies zu deutlichen Leistungssteigerungen bei Textgenerierung, Argumentation und sogar Programmcode. Der iterative Prozess erlaubt eine feinere Justierung als einmalige Prompts.

#### Geeignet für

- Optimierung längerer Texte
- Argumentations- oder Schreibaufgaben
- Programmieraufgaben mit Fehleranfälligkeit

#### Beispiel-Prompt

```text
Lies bitte deine vorherige Antwort nochmals durch. Gib dir selbst ein kurzes Feedback dazu. Verbessere anschliessend den Text basierend auf diesem Feedback.
```

---

## Schlussbemerkungen

Die hier präsentierten Prompting-Patterns bieten eine fundierte Grundlage für den effektiven und reflektierten Einsatz grosser Sprachmodelle. Sie zeigen, dass gute Ergebnisse nicht dem Zufall überlassen bleiben, sondern durch gezielte Interaktionsstrategien erreichbar sind.

Dabei geht es nicht nur darum, «richtige» Fragen zu stellen, sondern auch darum, Denkprozesse sichtbar zu machen, Antworten zu strukturieren und Reflexion zu ermöglichen. Besonders wertvoll ist der Gedanke, dass wir LLMs nicht nur als Werkzeuge, sondern als kollaborative Partner in Co-Creation-Prozessen verstehen können.

Dieses Dokument soll nicht nur als Nachschlagewerk dienen, sondern vor allem zur eigenständigen Erprobung und Weiterentwicklung der Techniken ermutigen. Denn: **Wer promptet, lernt – und wer gut promptet, erschliesst sich neue Formen von Kreativität, Analyse und Problemlösung.**

---

## Literatur

[1] S. Schulhoff und others, «The Prompt Report: A Systematic Survey of Prompt Engineering Techniques», ArXiv Prepr. ArXiv240606608, 2024.

[2] J. Wei u. a., «Chain-of-Thought Prompting Elicits Reasoning in Large Language Models», in Advances in Neural Information Processing Systems, 2022, S. 24824–24837.

[3] T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, und Y. Iwasawa, «Large Language Models are Zero-Shot Reasoners», in Advances in Neural Information Processing Systems, 2022.

[4] S. Yao u. a., «Tree of Thoughts: Deliberate Problem Solving with Large Language Models», in Advances in Neural Information Processing Systems, 2023.

[5] X. Wang u. a., «Self-Consistency Improves Chain of Thought Reasoning in Language Models», in International Conference on Learning Representations, 2023.

[6] L. Wang u. a., «Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models», in Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 2023, S. 2609–2634. doi: 10.18653/v1/2023.acl-long.147.

[7] A. Madaan u. a., «Self-Refine: Iterative Refinement with Self-Feedback», in Advances in Neural Information Processing Systems, 2023.

[8] A. Vaswani u. a., «Attention is all you need», in Advances in neural information processing systems, 2017, S. 5998–6008.

[9] T. Brown u. a., «Language Models are Few-Shot Learners», in Advances in Neural Information Processing Systems, 2020, S. 1877–1901.

---

**Zurück zu:** [Materialien README](./README.md)
