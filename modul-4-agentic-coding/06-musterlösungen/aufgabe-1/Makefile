# Makefile für Task Manager CLI
# Vereinfacht häufige Entwicklungsaufgaben

.PHONY: help install install-dev test test-cov lint format type-check clean demo

help:  ## Zeigt diese Hilfe an
	@echo "Task Manager CLI - Makefile Commands"
	@echo "====================================="
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Installiert das Paket
	uv pip install -e .

install-dev:  ## Installiert das Paket mit Dev-Dependencies
	uv sync --all-extras

sync:  ## Synchronisiert Dependencies (empfohlen)
	uv sync --all-extras

test:  ## Führt alle Tests aus
	uv run pytest -v

test-cov:  ## Führt Tests mit Coverage-Report aus
	uv run pytest --cov=task_manager --cov-report=term-missing --cov-report=html
	@echo ""
	@echo "Coverage-Report: htmlcov/index.html"

lint:  ## Führt Linting mit flake8 aus
	uv run flake8 task_manager tests --max-line-length=100

format:  ## Formatiert Code mit black
	uv run black task_manager tests

format-check:  ## Prüft Code-Formatierung
	uv run black --check task_manager tests

type-check:  ## Führt Type-Checking mit mypy aus
	uv run mypy task_manager

clean:  ## Entfernt generierte Dateien
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf .venv/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	uv cache clean

demo:  ## Führt Demo-Skript aus
	@chmod +x demo.sh
	@./demo.sh

build:  ## Erstellt Distribution-Pakete
	uv build

all: format lint type-check test  ## Führt alle Checks aus

ci: lint type-check test-cov  ## Simuliert CI-Pipeline lokal

