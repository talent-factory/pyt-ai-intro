# Makefile für ConTeXt-Dokumentation
# Verwendet LuaMetaTeX als Engine

# Hauptdokument (ohne .tex Endung)
MAIN = pyt-ai-intro

# ConTeXt-Befehl
CONTEXT = context

# Alle TeX-Dateien für Abhängigkeiten
TEX_FILES = $(wildcard *.tex) $(wildcard chapters/*.tex)

# Standard-Ziel
.PHONY: all
all: pdf

# PDF erstellen
.PHONY: pdf
pdf: $(MAIN).pdf

$(MAIN).pdf: $(TEX_FILES)
	$(CONTEXT) $(MAIN).tex

# Schneller Build (ohne Optimierungen)
.PHONY: draft
draft:
	$(CONTEXT) --mode=draft $(MAIN).tex

# Aufräumen - temporäre Dateien entfernen
.PHONY: clean
clean:
	rm -f *.log *.tuc *.tua *.tmp
	rm -f *.aux *.bbl *.blg
	rm -rf _minted-*

# Alles aufräumen inkl. PDF
.PHONY: distclean
distclean: clean
	rm -f $(MAIN).pdf

# Watch-Modus: Automatisch neu bauen bei Änderungen
# Benötigt: fswatch (brew install fswatch) oder entr
.PHONY: watch
watch:
	@echo "Watching for changes... (Ctrl+C to stop)"
	@if command -v fswatch >/dev/null 2>&1; then \
		fswatch -o $(TEX_FILES) | xargs -n1 -I{} make pdf; \
	elif command -v entr >/dev/null 2>&1; then \
		find . -name "*.tex" | entr make pdf; \
	else \
		echo "Please install fswatch (brew install fswatch) or entr"; \
		exit 1; \
	fi

# Hilfe anzeigen
.PHONY: help
help:
	@echo "ConTeXt Dokumentation - Makefile"
	@echo ""
	@echo "Verfügbare Ziele:"
	@echo "  make          - PDF erstellen (Standard)"
	@echo "  make pdf      - PDF erstellen"
	@echo "  make draft    - Schneller Draft-Build"
	@echo "  make clean    - Temporäre Dateien löschen"
	@echo "  make distclean- Alles löschen inkl. PDF"
	@echo "  make watch    - Auto-Rebuild bei Änderungen"
	@echo "  make help     - Diese Hilfe anzeigen"

