#!/usr/bin/env python3
"""
Professionelles Git-Commit-System mit automatischen Qualitätschecks.
Erstellt deutsche Emoji Conventional Commit Nachrichten.

Verwendung:
    python commit/commit.py                    # Standard-Commit
    python commit/commit.py --no-verify        # Überspringt Pre-Commit-Checks
    python commit/commit.py --skip-tests       # Überspringt Tests
    python commit/commit.py --force-push       # Führt force push aus
    python commit/commit.py --message "text"   # Eigene Commit-Nachricht
"""

import argparse
import sys
import subprocess
from pathlib import Path
from typing import List, Optional

# Importiere Module aus dem gleichen Verzeichnis
try:
    from .pre_commit_checks import ProjectDetector, PreCommitChecker
    from .commit_message_generator import CommitMessageGenerator
except ImportError:
    # Fallback für direkten Aufruf
    from pre_commit_checks import ProjectDetector, PreCommitChecker
    from commit_message_generator import CommitMessageGenerator


class GitCommitSystem:
    """Hauptklasse für das Git-Commit-System."""
    
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.detector = ProjectDetector(project_root)
        self.message_generator = CommitMessageGenerator(project_root)
    
    def commit(self, 
               no_verify: bool = False,
               skip_tests: bool = False, 
               force_push: bool = False,
               custom_message: Optional[str] = None) -> bool:
        """Führt den kompletten Commit-Workflow durch."""
        
        print("🚀 Git-Commit-System gestartet")
        print("=" * 50)
        
        # 1. Pre-Commit-Checks (optional überspringen)
        if not no_verify:
            print("\n📋 Schritt 1: Pre-Commit-Checks")
            if not self._run_pre_commit_checks(skip_tests):
                print("\n❌ Pre-Commit-Checks fehlgeschlagen!")
                print("   Verwende --no-verify zum Überspringen")
                return False
        else:
            print("\n⏭️ Pre-Commit-Checks übersprungen (--no-verify)")
        
        # 2. Staging-Analyse
        print("\n📁 Schritt 2: Staging-Analyse")
        if not self._analyze_and_stage_files():
            print("\n❌ Keine Änderungen zum Committen gefunden!")
            return False
        
        # 3. Diff-Analyse und Commit-Nachricht
        print("\n📝 Schritt 3: Commit-Nachricht generieren")
        analysis = self.message_generator.analyze_changes()
        
        # Prüfe auf mehrere logische Änderungen
        if self._should_split_commit(analysis):
            print("\n⚠️ Warnung: Mehrere logische Änderungen erkannt!")
            print("   Erwäge, den Commit aufzuteilen für bessere Historie.")
            if not self._confirm_continue():
                return False
        
        # Commit-Nachricht generieren
        commit_message = self.message_generator.generate_commit_message(
            analysis, custom_message
        )
        
        print("\n📋 Vorgeschlagene Commit-Nachricht:")
        print("-" * 40)
        print(commit_message)
        print("-" * 40)
        
        # 4. Commit erstellen
        print("\n💾 Schritt 4: Commit erstellen")
        if not self._create_commit(commit_message):
            return False
        
        # 5. Optional: Push anbieten
        print("\n🌐 Schritt 5: Push zum Remote-Repository")
        if self._should_push(force_push):
            return self._push_changes(force_push)
        
        print("\n✅ Commit erfolgreich erstellt!")
        print("   Verwende 'git push' zum Hochladen der Änderungen.")
        return True
    
    def _run_pre_commit_checks(self, skip_tests: bool) -> bool:
        """Führt Pre-Commit-Checks durch."""
        project_types = self.detector.detect_project_types()
        
        if not project_types:
            print("ℹ️ Kein bekannter Projekttyp - überspringe Checks")
            return True
        
        checker = PreCommitChecker(self.project_root, skip_tests)
        return checker.run_checks(project_types)
    
    def _analyze_and_stage_files(self) -> bool:
        """Analysiert und stagt Dateien für Commit."""
        # Git-Status prüfen
        status_output = self._run_git_command(["git", "status", "--porcelain"])
        
        if not status_output.strip():
            return False
        
        # Gestakte und ungestakte Änderungen
        staged_files = []
        unstaged_files = []
        
        for line in status_output.strip().split("\n"):
            if len(line) >= 3:
                status = line[:2]
                filename = line[3:]
                
                if status[0] != " ":  # Gestakt
                    staged_files.append(filename)
                if status[1] != " ":  # Ungestakt
                    unstaged_files.append(filename)
        
        # Automatisches Staging falls nötig
        if not staged_files and unstaged_files:
            print(f"📦 {len(unstaged_files)} ungestakte Änderungen gefunden")
            print("   Füge automatisch alle Änderungen hinzu...")
            
            result = subprocess.run(
                ["git", "add", "."],
                cwd=self.project_root,
                capture_output=True
            )
            
            if result.returncode != 0:
                print("❌ Fehler beim Hinzufügen der Dateien!")
                return False
            
            staged_files = unstaged_files
        
        # Übersicht der zu committenden Dateien
        print(f"📋 {len(staged_files)} Dateien zum Committen:")
        for filename in staged_files[:10]:  # Maximal 10 anzeigen
            print(f"   • {filename}")
        
        if len(staged_files) > 10:
            print(f"   ... und {len(staged_files) - 10} weitere")
        
        return len(staged_files) > 0
    
    def _should_split_commit(self, analysis: dict) -> bool:
        """Prüft ob Commit aufgeteilt werden sollte."""
        file_types = analysis["file_types"]
        staged_files = analysis["staged_files"]
        
        # Viele verschiedene Dateitypen
        if len(file_types) > 3:
            return True
        
        # Viele Dateien
        if len(staged_files) > 20:
            return True
        
        # Tests und Code gleichzeitig
        if file_types.get("test", 0) > 0 and file_types.get(".py", 0) > 0:
            return True
        
        return False
    
    def _confirm_continue(self) -> bool:
        """Fragt Benutzer ob fortgefahren werden soll."""
        try:
            response = input("Trotzdem fortfahren? (j/N): ").lower()
            return response in ["j", "ja", "y", "yes"]
        except KeyboardInterrupt:
            print("\n\n❌ Abgebrochen durch Benutzer")
            return False
    
    def _create_commit(self, message: str) -> bool:
        """Erstellt den Git-Commit."""
        # WICHTIG: Keine automatischen Signaturen hinzufügen!
        # Commit-Nachricht darf KEINE "Co-Authored-By" oder "Generated with" enthalten
        
        result = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=self.project_root,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✅ Commit erfolgreich erstellt!")
            
            # Commit-Hash anzeigen
            hash_result = subprocess.run(
                ["git", "rev-parse", "--short", "HEAD"],
                cwd=self.project_root,
                capture_output=True,
                text=True
            )
            
            if hash_result.returncode == 0:
                commit_hash = hash_result.stdout.strip()
                print(f"   Commit-Hash: {commit_hash}")
            
            return True
        else:
            print("❌ Fehler beim Erstellen des Commits!")
            print(f"   {result.stderr}")
            return False
    
    def _should_push(self, force_push: bool) -> bool:
        """Prüft ob gepusht werden soll."""
        if force_push:
            return True
        
        # Prüfe ob Remote-Branch existiert
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}"],
            cwd=self.project_root,
            capture_output=True
        )
        
        if result.returncode == 0:
            try:
                response = input("Push zum Remote-Repository? (j/N): ").lower()
                return response in ["j", "ja", "y", "yes"]
            except KeyboardInterrupt:
                print("\n")
                return False
        
        return False
    
    def _push_changes(self, force_push: bool) -> bool:
        """Pusht Änderungen zum Remote-Repository."""
        cmd = ["git", "push"]
        if force_push:
            cmd.append("--force-with-lease")
            print("⚠️ Force Push wird ausgeführt...")
        
        result = subprocess.run(cmd, cwd=self.project_root)
        
        if result.returncode == 0:
            print("✅ Änderungen erfolgreich gepusht!")
            return True
        else:
            print("❌ Fehler beim Pushen!")
            return False
    
    def _run_git_command(self, cmd: List[str]) -> str:
        """Führt Git-Befehl aus."""
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


def main():
    """Hauptfunktion."""
    parser = argparse.ArgumentParser(
        description="Professionelles Git-Commit-System",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "--no-verify", 
        action="store_true",
        help="Überspringt Pre-Commit-Checks"
    )
    
    parser.add_argument(
        "--skip-tests",
        action="store_true", 
        help="Überspringt Testausführung"
    )
    
    parser.add_argument(
        "--force-push",
        action="store_true",
        help="Führt force push aus (Vorsicht!)"
    )
    
    parser.add_argument(
        "--message", "-m",
        type=str,
        help="Eigene Commit-Nachricht"
    )
    
    args = parser.parse_args()
    
    # Projekt-Root ermitteln
    project_root = Path.cwd()
    
    # Git-Repository prüfen
    if not (project_root / ".git").exists():
        print("❌ Kein Git-Repository gefunden!")
        print("   Führe 'git init' aus oder wechsle in ein Git-Repository.")
        sys.exit(1)
    
    # Commit-System starten
    system = GitCommitSystem(project_root)
    success = system.commit(
        no_verify=args.no_verify,
        skip_tests=args.skip_tests,
        force_push=args.force_push,
        custom_message=args.message
    )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
