# Prüfungsdimensionsmatrix

> Problem, das diese Datei löst: Sie definiert die 14 Dimensionen der parallelen Prüfung in Phase 2, deren jeweilige Prüfpunkte, empfohlene Agents und Fehlerstufen als Grundlage für Zuweisung und Bewertung.

## Prüfungsdimensionsmatrix

| # | Dimension | Prüfpunkte (Schlagwörter, Details werden vom Sub-Agent entfaltet) | Empfohlener Agent | Fehlerstufe |
|---|---|---|---|---|
| D1 | Sicherheit und Datenschutz | Secret-Scan, `.env`, private Schlüssel, interne Domains/IPs, personenbezogene Daten, Log-Rückstände | security-auditor | P0 |
| D2 | Lizenz und Recht | Vorhandensein und Typ der LICENSE, Lizenzkompatibilität der Abhängigkeiten, NOTICE, Drittanbieterhinweise | license-checker | P0 |
| D3 | Repository-Hygiene | Abdeckung der .gitignore, Artefakt- und Abhängigkeitsverzeichnisse, .gitattributes, Zeilenenden LF, Ausführungsbits, Namenskonflikte durch Groß-/Kleinschreibung | repo-hygienist | P0/P1 |
| D4 | Umfang und Binärdateien | Dateien >50 MB, Bildkompression, LFS-Konfiguration, Historienaufblähung | repo-hygienist | P1 |
| D5 | Reproduzierbarer Build | Lockfile eingecheckt, Deklaration der Engine-Version, Build-Skripte, Build in sauberer Umgebung erfolgreich | build-verifier | P0 |
| D6 | Tests und statische Analyse | Unit-Tests bestanden, Abdeckung, Lint, Formatierung, Typprüfung | ci-runner | P0/P1 |
| D7 | Commit-Historie | Conventional Commits, Atomarität, kein WIP, Autoreninformationen, keine sensiblen Commit-Nachrichten | commit-reviewer | P1 |
| D8 | Branch und Veröffentlichung | Schutz von main, Branch-Benennung, Tag nach SemVer, annotierter Tag, Release Notes | release-manager | P1 |
| D9 | Automatisierung | CI-Workflow ausführbar, Status-Badges, Dependabot, CODEOWNERS, Issue-/PR-Vorlagen | ci-runner | P1 |
| D10 | Repository-Metadaten | description (zweisprachiges Sammelformat `Landessprache \| Englisch`, je Sprache ≤120 Zeichen), topics (alle 20 belegt, nur Englisch, durchgehend Kleinbuchstaben), Standard-Branch, About-Links, Social Preview | metadata-agent | P1 |
| D11 | Dokumentationsvollständigkeit | Existenzprüfung jedes Eintrags der Dokumentationsmatrix | docs-orchestrator | P0/P1 |
| D12 | Dokumentationsqualität | Überschriftenhierarchie, Sprachkennzeichnung von Codeblöcken, Linkgültigkeit, Bild-Alt-Texte, Leerzeichen zwischen Chinesisch und Englisch, keine Platzhalter | docs-orchestrator | P1/P2 |
| D13 | README-Startseite | Positionierung in einem Satz, Installation, Schnellstart, Badges ≤4, Screenshot, keine lokalen absoluten Pfade | readme-writer | P1 |
| D14 | Community-Governance | CONTRIBUTING, CODE_OF_CONDUCT, SECURITY, Issue-Vorlagen, Supportkanäle | docs-orchestrator | P2 |

## Bedeutung der Stufen

- **P0**: Blockiert den Push.
- **P1**: Vor dem Push zu beheben oder zwingend als Aufgabe zu erfassen.
- **P2**: Optimierung empfohlen.

## Zuweisung und Zusammenfassung

- Die Zuweisungsweise je Dimension siehe [Sub-Agent-Dispatch-Vertrag](./sub-agent-dispatch-contract.md).
- Die Bewertungsergebnisse werden in die Problemliste des [Prüfberichtsformats](./audit-report-format.md) zusammengeführt; jeder Eintrag muss einen Nachweis enthalten.
- Prüfgrundlagen für D11/D12 siehe [Dokumentationsmatrix](./document-matrix.md) und [Qualitätstor](./quality-gate.md).

## Verwandte Dateien

- Zeitpunkt der Ausführung siehe Phase 2 in [Ausführungsprozess](./execution-process.md)
- Freigabebedingungen der Qualitätstore siehe [Qualitätstor](./quality-gate.md)
