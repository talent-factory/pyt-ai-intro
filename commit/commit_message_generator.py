#!/usr/bin/env python3
"""
Commit-Nachrichten-Generator mit automatischer Typerkennung.
Generiert deutsche Emoji Conventional Commit Nachrichten.
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional
import subprocess


class CommitMessageGenerator:
    """Generiert Commit-Nachrichten basierend auf Git-Diff-Analyse."""
    
    # Commit-Typen mit Emojis und deutschen Beschreibungen
    COMMIT_TYPES = {
        "feat": {"emoji": "✨", "desc": "Neue Funktionalität"},
        "fix": {"emoji": "🐛", "desc": "Fehlerbehebung"},
        "docs": {"emoji": "📚", "desc": "Dokumentation"},
        "style": {"emoji": "💎", "desc": "Code-Formatierung"},
        "refactor": {"emoji": "♻️", "desc": "Code-Umstrukturierung"},
        "perf": {"emoji": "⚡", "desc": "Performance-Verbesserung"},
        "test": {"emoji": "🧪", "desc": "Tests"},
        "chore": {"emoji": "🔧", "desc": "Build/Tools/Konfiguration"},
        "deploy": {"emoji": "🚀", "desc": "Deployment"},
        "security": {"emoji": "🔒", "desc": "Sicherheit"},
        "i18n": {"emoji": "🌐", "desc": "Internationalisierung"},
        "ui": {"emoji": "📱", "desc": "User Interface"},
        "db": {"emoji": "🗃️", "desc": "Datenbank"},
        "remove": {"emoji": "🔥", "desc": "Code entfernen"},
        "breaking": {"emoji": "🚨", "desc": "Breaking Changes"}
    }
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
    
    def analyze_changes(self) -> Dict:
        """Analysiert Git-Änderungen und schlägt Commit-Typ vor."""
        # Git-Status abrufen
        status_output = self._run_git_command(["git", "status", "--porcelain"])
        staged_files = self._parse_git_status(status_output)
        
        # Git-Diff für gestakte Änderungen
        diff_output = self._run_git_command(["git", "diff", "--cached"])
        
        # Änderungen analysieren
        analysis = {
            "staged_files": staged_files,
            "file_types": self._analyze_file_types(staged_files),
            "change_patterns": self._analyze_change_patterns(diff_output),
            "suggested_type": self._suggest_commit_type(staged_files, diff_output),
            "scope": self._suggest_scope(staged_files),
            "breaking_changes": self._detect_breaking_changes(diff_output)
        }
        
        return analysis
    
    def generate_commit_message(self, analysis: Dict, custom_message: Optional[str] = None) -> str:
        """Generiert eine Commit-Nachricht basierend auf der Analyse."""
        commit_type = analysis["suggested_type"]
        scope = analysis["scope"]
        
        # Emoji und Typ
        emoji = self.COMMIT_TYPES[commit_type]["emoji"]
        type_name = commit_type
        
        # Scope hinzufügen falls vorhanden
        scope_part = f"({scope})" if scope else ""
        
        # Beschreibung generieren
        if custom_message:
            description = custom_message
        else:
            description = self._generate_description(analysis)
        
        # Commit-Nachricht zusammenbauen
        subject = f"{emoji} {type_name}{scope_part}: {description}"
        
        # Body generieren falls nötig
        body_parts = []
        
        # Datei-Übersicht hinzufügen
        if len(analysis["staged_files"]) > 5:
            body_parts.append(f"Geänderte Dateien: {len(analysis['staged_files'])}")
        
        # Breaking Changes hinzufügen
        if analysis["breaking_changes"]:
            body_parts.append("BREAKING CHANGE: " + analysis["breaking_changes"])
        
        # Vollständige Nachricht
        if body_parts:
            return subject + "\n\n" + "\n".join(body_parts)
        else:
            return subject
    
    def _run_git_command(self, cmd: List[str]) -> str:
        """Führt Git-Befehl aus und gibt Ausgabe zurück."""
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            return ""
    
    def _parse_git_status(self, status_output: str) -> List[Tuple[str, str]]:
        """Parst Git-Status-Ausgabe."""
        files = []
        for line in status_output.strip().split("\n"):
            if len(line) >= 3:
                status = line[:2]
                filename = line[3:]
                files.append((status, filename))
        return files
    
    def _analyze_file_types(self, staged_files: List[Tuple[str, str]]) -> Dict[str, int]:
        """Analysiert Dateitypen der geänderten Dateien."""
        file_types = {}
        
        for status, filename in staged_files:
            path = Path(filename)
            
            # Dateierweiterung
            ext = path.suffix.lower()
            if ext:
                file_types[ext] = file_types.get(ext, 0) + 1
            
            # Spezielle Verzeichnisse
            parts = path.parts
            if "test" in parts or "tests" in parts:
                file_types["test"] = file_types.get("test", 0) + 1
            if "doc" in parts or "docs" in parts:
                file_types["docs"] = file_types.get("docs", 0) + 1
        
        return file_types
    
    def _analyze_change_patterns(self, diff_output: str) -> Dict[str, int]:
        """Analysiert Änderungsmuster im Diff."""
        patterns = {
            "additions": len(re.findall(r"^\+[^+]", diff_output, re.MULTILINE)),
            "deletions": len(re.findall(r"^-[^-]", diff_output, re.MULTILINE)),
            "new_files": len(re.findall(r"^new file mode", diff_output, re.MULTILINE)),
            "deleted_files": len(re.findall(r"^deleted file mode", diff_output, re.MULTILINE)),
            "renamed_files": len(re.findall(r"^rename from", diff_output, re.MULTILINE))
        }
        
        return patterns
    
    def _suggest_commit_type(self, staged_files: List[Tuple[str, str]], diff_output: str) -> str:
        """Schlägt Commit-Typ basierend auf Änderungen vor."""
        file_types = self._analyze_file_types(staged_files)
        patterns = self._analyze_change_patterns(diff_output)
        
        # Test-Dateien -> test
        if file_types.get("test", 0) > 0 or any(".py" in f[1] and "test" in f[1] for f in staged_files):
            return "test"
        
        # Dokumentation -> docs
        if file_types.get(".md", 0) > 0 or file_types.get("docs", 0) > 0:
            return "docs"
        
        # Neue Dateien -> feat (meist)
        if patterns["new_files"] > 0:
            return "feat"
        
        # Gelöschte Dateien -> remove
        if patterns["deleted_files"] > 0:
            return "remove"
        
        # Konfigurationsdateien -> chore
        config_files = [".json", ".toml", ".yaml", ".yml", ".cfg", ".ini"]
        if any(file_types.get(ext, 0) > 0 for ext in config_files):
            return "chore"
        
        # Viele Löschungen -> refactor oder remove
        if patterns["deletions"] > patterns["additions"] * 2:
            return "refactor"
        
        # Standard: feat für neue Funktionalität
        return "feat"
    
    def _suggest_scope(self, staged_files: List[Tuple[str, str]]) -> Optional[str]:
        """Schlägt einen Scope basierend auf geänderten Dateien vor."""
        # Häufige Verzeichnisse sammeln
        dirs = set()
        for status, filename in staged_files:
            path = Path(filename)
            if len(path.parts) > 1:
                dirs.add(path.parts[0])
        
        # Eindeutiger Scope
        if len(dirs) == 1:
            scope = list(dirs)[0]
            # Bekannte Scopes
            if scope in ["api", "ui", "db", "auth", "tests", "docs", "config"]:
                return scope
        
        return None
    
    def _detect_breaking_changes(self, diff_output: str) -> Optional[str]:
        """Erkennt Breaking Changes im Diff."""
        # Einfache Heuristiken für Breaking Changes
        breaking_indicators = [
            r"def\s+\w+\([^)]*\).*->.*:",  # Funktionssignaturen geändert
            r"class\s+\w+\([^)]*\):",      # Klassenvererbung geändert
            r"from\s+\w+\s+import",        # Import-Struktur geändert
        ]
        
        for pattern in breaking_indicators:
            if re.search(pattern, diff_output):
                return "API-Änderungen erkannt"
        
        return None
    
    def _generate_description(self, analysis: Dict) -> str:
        """Generiert automatische Beschreibung basierend auf Analyse."""
        file_types = analysis["file_types"]
        patterns = analysis["change_patterns"]
        commit_type = analysis["suggested_type"]
        
        # Beschreibung basierend auf Commit-Typ
        if commit_type == "feat":
            if file_types.get(".py", 0) > 0:
                return "neue Python-Funktionalität implementiert"
            else:
                return "neue Funktionalität hinzugefügt"
        
        elif commit_type == "fix":
            return "Fehler behoben"
        
        elif commit_type == "docs":
            if file_types.get(".md", 0) > 0:
                return "Markdown-Dokumentation aktualisiert"
            else:
                return "Dokumentation aktualisiert"
        
        elif commit_type == "test":
            return f"Tests hinzugefügt ({patterns['additions']} Zeilen)"
        
        elif commit_type == "chore":
            if file_types.get(".toml", 0) > 0:
                return "Projektkonfiguration aktualisiert"
            elif file_types.get(".json", 0) > 0:
                return "JSON-Konfiguration aktualisiert"
            else:
                return "Build-Konfiguration aktualisiert"
        
        elif commit_type == "refactor":
            return "Code-Struktur verbessert"
        
        elif commit_type == "remove":
            return f"{patterns['deleted_files']} Dateien entfernt"
        
        else:
            # Fallback: Anzahl geänderte Dateien
            num_files = len(analysis["staged_files"])
            if num_files == 1:
                return "Datei aktualisiert"
            else:
                return f"{num_files} Dateien aktualisiert"
