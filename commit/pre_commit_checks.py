#!/usr/bin/env python3
"""
Pre-Commit-Checks für verschiedene Projekttypen.
Automatische Qualitätsprüfungen vor Git-Commits.
"""

import subprocess
import sys
from pathlib import Path
from typing import List, Tuple
import json


class ProjectDetector:
    """Erkennt Projekttyp basierend auf Dateien und Konfiguration."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
    
    def detect_project_types(self) -> List[str]:
        """Erkennt alle Projekttypen im aktuellen Verzeichnis."""
        types = []
        
        # Python-Projekt
        if self._has_python_files():
            types.append("python")
        
        # Java-Projekt
        if self._has_java_files():
            types.append("java")
        
        # Node.js/React-Projekt
        if self._has_nodejs_files():
            types.append("nodejs")
        
        # Dokumentation
        if self._has_docs_files():
            types.append("docs")
        
        return types
    
    def _has_python_files(self) -> bool:
        """Prüft auf Python-Projekt-Indikatoren."""
        indicators = [
            "pyproject.toml", "requirements.txt", "requirements-dev.txt",
            "setup.py", "setup.cfg", "Pipfile", "poetry.lock"
        ]
        
        for indicator in indicators:
            if (self.project_root / indicator).exists():
                return True
        
        # Prüfe auf .py-Dateien
        return len(list(self.project_root.rglob("*.py"))) > 0
    
    def _has_java_files(self) -> bool:
        """Prüft auf Java-Projekt-Indikatoren."""
        indicators = ["pom.xml", "build.gradle", "gradle.properties"]
        
        for indicator in indicators:
            if (self.project_root / indicator).exists():
                return True
        
        return len(list(self.project_root.rglob("*.java"))) > 0
    
    def _has_nodejs_files(self) -> bool:
        """Prüft auf Node.js/React-Projekt-Indikatoren."""
        indicators = ["package.json", "yarn.lock", "package-lock.json"]
        
        for indicator in indicators:
            if (self.project_root / indicator).exists():
                return True
        
        return len(list(self.project_root.rglob("*.js"))) > 0 or \
               len(list(self.project_root.rglob("*.ts"))) > 0
    
    def _has_docs_files(self) -> bool:
        """Prüft auf Dokumentations-Dateien."""
        return len(list(self.project_root.rglob("*.md"))) > 0 or \
               len(list(self.project_root.rglob("*.tex"))) > 0


class PreCommitChecker:
    """Führt Pre-Commit-Checks für verschiedene Projekttypen durch."""
    
    def __init__(self, project_root: Path, skip_tests: bool = False):
        self.project_root = project_root
        self.skip_tests = skip_tests
        self.results: List[Tuple[str, bool, str]] = []
    
    def run_checks(self, project_types: List[str]) -> bool:
        """Führt alle relevanten Checks durch."""
        all_passed = True
        
        for project_type in project_types:
            if project_type == "python":
                all_passed &= self._run_python_checks()
            elif project_type == "java":
                all_passed &= self._run_java_checks()
            elif project_type == "nodejs":
                all_passed &= self._run_nodejs_checks()
            elif project_type == "docs":
                all_passed &= self._run_docs_checks()
        
        return all_passed
    
    def _run_python_checks(self) -> bool:
        """Führt Python-spezifische Checks durch."""
        print("🐍 Python-Projekt erkannt - führe Qualitätschecks durch...")
        all_passed = True
        
        # 1. Black Formatierung
        if self._tool_available("black"):
            passed, output = self._run_command(
                ["black", "--check", "--diff", "."],
                "Code-Formatierung (Black)"
            )
            all_passed &= passed
            if not passed:
                print("   💡 Lösung: black .")
        
        # 2. Ruff Linting
        if self._tool_available("ruff"):
            passed, output = self._run_command(
                ["ruff", "check", "."],
                "Linting (Ruff)"
            )
            all_passed &= passed
        
        # 3. Tests mit pytest
        if not self.skip_tests and self._tool_available("pytest"):
            passed, output = self._run_command(
                ["pytest", "--tb=short", "-q"],
                "Tests (pytest)"
            )
            all_passed &= passed
        
        # 4. Type-Checking mit mypy (optional)
        if self._tool_available("mypy"):
            passed, output = self._run_command(
                ["mypy", ".", "--ignore-missing-imports"],
                "Type-Checking (mypy)",
                optional=True
            )
            # mypy-Fehler stoppen Commit nicht
        
        return all_passed
    
    def _run_java_checks(self) -> bool:
        """Führt Java-spezifische Checks durch."""
        print("☕ Java-Projekt erkannt - führe Qualitätschecks durch...")
        all_passed = True
        
        # Maven-Projekt
        if (self.project_root / "pom.xml").exists():
            # Kompilierung
            passed, output = self._run_command(
                ["mvn", "compile", "-q"],
                "Kompilierung (Maven)"
            )
            all_passed &= passed
            
            # Tests
            if not self.skip_tests:
                passed, output = self._run_command(
                    ["mvn", "test", "-q"],
                    "Tests (Maven)"
                )
                all_passed &= passed
        
        # Gradle-Projekt
        elif (self.project_root / "build.gradle").exists():
            gradle_cmd = "./gradlew" if (self.project_root / "gradlew").exists() else "gradle"
            
            # Kompilierung
            passed, output = self._run_command(
                [gradle_cmd, "compileJava", "-q"],
                "Kompilierung (Gradle)"
            )
            all_passed &= passed
            
            # Tests
            if not self.skip_tests:
                passed, output = self._run_command(
                    [gradle_cmd, "test", "-q"],
                    "Tests (Gradle)"
                )
                all_passed &= passed
        
        return all_passed
    
    def _run_nodejs_checks(self) -> bool:
        """Führt Node.js/React-spezifische Checks durch."""
        print("📦 Node.js-Projekt erkannt - führe Qualitätschecks durch...")
        all_passed = True
        
        # Package Manager erkennen
        package_manager = "npm"
        if (self.project_root / "yarn.lock").exists():
            package_manager = "yarn"
        
        # ESLint
        if self._has_npm_script("lint"):
            passed, output = self._run_command(
                [package_manager, "run", "lint"],
                "Linting (ESLint)"
            )
            all_passed &= passed
        
        # TypeScript Type-Checking
        if (self.project_root / "tsconfig.json").exists():
            passed, output = self._run_command(
                ["npx", "tsc", "--noEmit"],
                "Type-Checking (TypeScript)"
            )
            all_passed &= passed
        
        # Tests
        if not self.skip_tests and self._has_npm_script("test"):
            passed, output = self._run_command(
                [package_manager, "test", "--", "--passWithNoTests"],
                "Tests (Jest/Vitest)"
            )
            all_passed &= passed
        
        return all_passed
    
    def _run_docs_checks(self) -> bool:
        """Führt Dokumentations-spezifische Checks durch."""
        print("📚 Dokumentation erkannt - führe Checks durch...")
        # Dokumentations-Checks sind meist optional
        return True
    
    def _run_command(self, cmd: List[str], name: str, optional: bool = False) -> Tuple[bool, str]:
        """Führt einen Befehl aus und protokolliert das Ergebnis."""
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=True,
                text=True,
                timeout=300  # 5 Minuten Timeout
            )
            
            success = result.returncode == 0
            output = result.stdout + result.stderr
            
            if success:
                print(f"   ✅ {name}: OK")
            else:
                if optional:
                    print(f"   ⚠️ {name}: Warnung")
                    if output.strip():
                        print(f"      {output.strip()}")
                else:
                    print(f"   ❌ {name}: Fehler")
                    if output.strip():
                        print(f"      {output.strip()}")
            
            self.results.append((name, success, output))
            return success, output
            
        except subprocess.TimeoutExpired:
            print(f"   ⏰ {name}: Timeout (>5min)")
            return False, "Timeout"
        except FileNotFoundError:
            print(f"   ⏭️ {name}: Tool nicht verfügbar")
            return True, "Tool nicht gefunden"  # Nicht verfügbare Tools sind OK
    
    def _tool_available(self, tool: str) -> bool:
        """Prüft ob ein Tool verfügbar ist."""
        try:
            subprocess.run([tool, "--version"], capture_output=True, timeout=10)
            return True
        except (FileNotFoundError, subprocess.TimeoutExpired):
            return False
    
    def _has_npm_script(self, script: str) -> bool:
        """Prüft ob ein npm-Script existiert."""
        package_json = self.project_root / "package.json"
        if not package_json.exists():
            return False
        
        try:
            with open(package_json) as f:
                data = json.load(f)
                return script in data.get("scripts", {})
        except (json.JSONDecodeError, KeyError):
            return False


def main():
    """Hauptfunktion für Pre-Commit-Checks."""
    project_root = Path.cwd()
    skip_tests = "--skip-tests" in sys.argv
    
    # Projekttypen erkennen
    detector = ProjectDetector(project_root)
    project_types = detector.detect_project_types()
    
    if not project_types:
        print("ℹ️ Kein bekannter Projekttyp erkannt - überspringe Checks")
        return True
    
    print(f"🔍 Erkannte Projekttypen: {', '.join(project_types)}")
    
    # Checks durchführen
    checker = PreCommitChecker(project_root, skip_tests)
    all_passed = checker.run_checks(project_types)
    
    if all_passed:
        print("\n✅ Alle Checks erfolgreich!")
        return True
    else:
        print("\n❌ Einige Checks sind fehlgeschlagen!")
        print("   Behebe die Probleme und versuche es erneut.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
