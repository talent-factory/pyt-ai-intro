# 🔴 Import Errors

## ModuleNotFoundError: No module named 'X'

### Problem
Python kann das Modul nicht finden.

### Ursachen
1. Modul nicht installiert
2. Falsche virtuelle Umgebung
3. Tippfehler im Import

### Lösung 1: Modul installieren

```bash
# Prüfen Sie pyproject.toml
[project]
dependencies = [
    "streamlit>=1.28.0",  # Fügen Sie fehlende Module hinzu
]

# Installieren
uv sync
```

### Lösung 2: Virtuelle Umgebung prüfen

```bash
# Prüfen welche Python-Version verwendet wird
which python
# Sollte .venv/bin/python sein

# Falls nicht, aktivieren Sie die virtuelle Umgebung
# (UV macht das automatisch mit 'uv run')
uv run python --version
```

### Lösung 3: Tippfehler prüfen

```python
# Falsch:
import streamlt  # Tippfehler!

# Richtig:
import streamlit
```

## ImportError: cannot import name 'X' from 'Y'

### Problem
Das Modul existiert, aber der spezifische Import nicht.

### Ursachen
1. Falsche Version
2. Falscher Import-Name
3. Modul-Struktur geändert

### Lösung

```python
# Prüfen Sie die Dokumentation
# Beispiel: Streamlit

# Falsch (alte Version):
from streamlit import st_folium

# Richtig:
from streamlit_folium import st_folium
```

## Beispiele

### Streamlit

```bash
# Fehler:
ModuleNotFoundError: No module named 'streamlit'

# Lösung:
# pyproject.toml:
dependencies = ["streamlit>=1.28.0"]
# Terminal:
uv sync
```

### Pandas

```bash
# Fehler:
ModuleNotFoundError: No module named 'pandas'

# Lösung:
dependencies = ["pandas>=2.0.0"]
uv sync
```

### Geopy

```bash
# Fehler:
ModuleNotFoundError: No module named 'geopy'

# Lösung:
dependencies = ["geopy>=2.4.0"]
uv sync
```

---

**Tipp:** Immer `uv sync` nach Änderungen an `pyproject.toml` ausführen!

