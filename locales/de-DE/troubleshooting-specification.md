# Fehlerbehebungs-Spezifikation

> Problem, das diese Datei löst: Definiert Struktur, Schreibweise der Einträge und Pflegemechanismus von Fehlerbehebungsdokumentation (Troubleshooting / FAQ), damit Nutzende anhand des Symptoms die Ursache finden und häufige Probleme selbst lösen können.

## 1. Anwendungsfälle

In den folgenden Fällen ist eine Fehlerbehebungsdokumentation bereitzustellen:

1. Bei Installation oder Build treten mehrere häufige Ursachen für Fehlschläge auf.
2. Konfigurationseinträge stehen zueinander in Konflikt und die Fehlermeldung reicht zur Lösungserläuterung nicht aus.
3. Für bestimmte Plattformen oder Versionen gibt es bekannte Einschränkungen.
4. Nutzende stellen wiederholt dieselbe Art von Fragen und die Antworten lassen sich standardisieren.

## 2. Dateispeicherort und Benennung

1. Bei geringem Umfang als Abschnitt der README mit der Überschrift „Häufige Fragen“ oder „Fehlerbehebung“.
2. Bei größerem Umfang als eigene Datei `docs/troubleshooting.md` oder `FAQ.md`, wobei die README einen Einstiegslink behält.
3. Probleme nach Themen gruppieren, etwa „Installation“, „Konfiguration“, „Betrieb“, „Leistung“, „Netzwerk“.

## 3. Dokumentstruktur

1. **Einleitung**: Der von diesem Dokument abgedeckte Umfang häufiger Probleme und die geltenden Versionen.
2. **Problemindex**: Problemüberschriften nach Themen auflisten, mit Sprungmarken für schnellen Zugriff.
3. **Problemeinträge**: Nach einheitlicher Struktur einzeln ausführen.
4. **Weiterhin ungelöst**: Auf Issue, Diskussionsbereich und weitere Hilfskanäle verweisen.

## 4. Struktur eines Eintrags

Jeder Problemeintrag muss die folgenden Teile enthalten:

| Teil | Inhalt | Anforderung |
| --- | --- | --- |
| Symptom | Die konkrete Erscheinung, die Nutzende sehen | Vollständige Fehlermeldung, nicht bloß „Fehler“ |
| Auslösebedingung | Wann das Problem auftritt | Version, Plattform und Vorgang klar benennen |
| Ursache | Die eigentliche Ursache | Mechanismus erläutern, nicht nur das Ergebnis nennen |
| Lösung | Ausführbare Schritte | Nummeriert, mit Befehlen oder Konfiguration |
| Verifikation | Wie die Behebung bestätigt wird | Erwartete Ausgabe angeben |
| Verwandtes | Links zu zugehöriger Dokumentation oder Issues | optional |

## 5. Beispiel für die Schreibweise eines Eintrags

```markdown
### Bei der Installation erscheint `EACCES: permission denied`

**Symptom**: Bei der Ausführung von `npm install -g <package>` wird unzureichende Berechtigung gemeldet.

**Auslösebedingung**: Installation eines globalen Pakets unter Linux oder macOS mit einem normalen Benutzerkonto.

**Ursache**: Die Schreibberechtigung für das globale Installationsverzeichnis liegt beim Systemadministrator, der aktuelle Benutzer hat keine Schreibberechtigung.

**Lösung**:

```bash
mkdir -p ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
npm install -g <package>
```

**Verifikation**: Die Ausführung von `<package> --version` gibt die Versionsnummer aus, damit ist die Behebung bestätigt.

## 6. Anforderungen an die Abfassung

1. Problemüberschriften verwenden Formulierungen, die Nutzende suchen würden, keine internen Fachbegriffe.
2. Fehlermeldungen unverändert übernehmen, damit Nutzende sie abgleichen können; sensible Informationen sind zu anonymisieren (siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)).
3. Lösungen mit vollständigen Befehlen angeben; es wird nicht vorausgesetzt, dass Nutzende Umgebungsvariablen gesetzt haben.
4. Ein Eintrag löst genau ein Problem und fasst nicht mehrere Ursachen zusammen.
5. Bei bekannten Defekten Auswirkungsumfang und Umgehung erläutern; ein Behebungszeitpunkt wird nicht zugesagt.
6. Migrationsbezogene Probleme verlinken auf den Migrationsleitfaden (siehe [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)).

## 7. Pflegemechanismus

1. Wird dasselbe Problem mehr als dreimal gestellt, ist ein Eintrag zu ergänzen oder umzuschreiben.
2. Nach einem Versionsupdate sind alle Einträge zu prüfen und nicht mehr gültige Inhalte zu entfernen.
3. Jeder Eintrag kann die zuletzt verifizierte Version kennzeichnen, um die Aktualität beurteilen zu können.
4. Der Problemindex wird mit dem Hinzukommen und Wegfallen von Einträgen synchron aktualisiert.

## 8. Verbotene Praktiken

1. Die Fehlerbehebungsdokumentation darf nicht als Funktionsvorstellung verfasst werden.
2. Antworten ohne diagnostischen Wert wie „einfach neu starten“ sind unzulässig.
3. Fehlermeldungen und Auslösebedingungen dürfen nicht entfallen.
4. Bereits behobene oder nicht mehr gültige Einträge dürfen nicht beibehalten werden.

## Verwandte Dateien

- Zuordnung zu README-Abschnitten siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md) Kapitel 15
- Offenlegung bekannter Probleme siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md) Kapitel 15
- Aktualisierungsbezogene Probleme siehe [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)
- Kanäle zur Problemsammlung siehe [Issue- und PR-Vorlagen-Spezifikation](./issue-and-pr-template-specification.md)
- Dokumentationsqualität gehört zu Dimension D12, siehe [Audit-Dimensionsmatrix](./review-dimension-matrix.md)
