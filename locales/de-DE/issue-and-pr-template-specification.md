# Spezifikation für Issue- und PR-Vorlagen

> Problem, das diese Datei löst: Sie definiert Felddesign, Format und Schreibanforderungen der strukturierten Formulare `.github/ISSUE_TEMPLATE/*.yml` und der Selbstprüfungs-Checkliste `.github/PULL_REQUEST_TEMPLATE.md`, damit Problemrückmeldungen und Änderungseinreichungen über ausführbare Eingabevorgaben verfügen.

## 1. Entwurfsprinzipien

1. **Struktur vor Freitext**: Issue-Formulare werden in YAML definiert und lenken die Eingabe über Auswahllisten, Kontrollkästchen und Pflichtfelder, um unbrauchbare Rückmeldungen zu verringern.
2. **Minimale Pflichtfelder**: Es bleiben nur die zur Eingrenzung des Problems erforderlichen Felder erhalten; optionale Felder dürfen nicht als Pflichtfelder gekennzeichnet werden.
3. **Ausdrückliche Selbstprüfung**: Die PR-Vorlage listet prüfbare Punkte als Checkliste auf, damit Beitragende keine wesentlichen Schritte überspringen.
4. **Eindeutige Zuständigkeit**: Issue-Formulare dienen der Informationserfassung und enthalten keine Projektvorstellung; die PR-Vorlage dient der Selbstprüfung und wiederholt keine Funktionsbeschreibungen (entsprechend der [Dokumentationsmatrix](./document-matrix.md)).

## 2. Struktur der Issue-Formulare

### 2.1 Dateien und Benennung

- Der Pfad ist fest auf `.github/ISSUE_TEMPLATE/*.yml` gesetzt, je Vorlage eine Datei.
- Dateinamen verwenden Kleinschreibung und Bindestriche, etwa `bug-report.yml`, `feature-request.yml`, `question.yml`.
- Mindestens die beiden Vorlagen „Fehlerbericht“ und „Funktionswunsch“ sind bereitzustellen.

### 2.2 Standardfelder

| Feld | Typ | Erforderlich | Zweck |
| --- | --- | --- | --- |
| `name` | Zeichenkette | Ja | Anzeigename der Vorlage |
| `description` | Zeichenkette | Ja | Erläuterung des Zwecks der Vorlage |
| `title` | Zeichenkettenpräfix | Ja | Automatisch erzeugtes Präfix des Problem-Titels |
| `labels` | Array | Nein | Automatisch hinzugefügte Labels |
| `body` | Array | Ja | Liste der Formularfelder |

Häufige Feldtypen in `body`:

| Typ | Geeignete Szenarien | Beispiel |
| --- | --- | --- |
| `markdown` | Erläuterungstext ohne Eingabe | Ausfüllhinweise |
| `textarea` | Lange Textbeschreibung | Schritte zur Reproduktion |
| `input` | Kurzer einzeiliger Text | Versionsnummer |
| `dropdown` | Begrenzte Auswahl | Betriebssystem, Schweregrad |
| `checkboxes` | Mehrfachbestätigung | Ob bereits nach Duplikaten gesucht wurde |

### 2.3 Feldliste für Fehlerberichte

1. Problembeschreibung (`textarea`, erforderlich): Was ist geschehen.
2. Erwartetes Verhalten (`textarea`, erforderlich): Was hätte geschehen sollen.
3. Reproduktionsschritte (`textarea`, erforderlich): Nummeriert, eigenständig reproduzierbar.
4. Laufzeitumgebung (`input` oder `dropdown`): Betriebssystem, Laufzeit, Projektversion.
5. Protokoll oder Screenshot (`textarea`): Fehlermeldungen angeben, sensible Angaben müssen anonymisiert werden.
6. Bestätigung der Duplikatprüfung (`checkboxes`, erforderlich): Bestehende Issues wurden durchsucht.

### 2.4 Feldliste für Funktionswünsche

1. Problemdarstellung (`textarea`, erforderlich): Welche Fähigkeit fehlt derzeit.
2. Nutzungsszenario (`textarea`, erforderlich): Wer benötigt sie unter welchen Umständen.
3. Gewünschte Lösung (`textarea`): Wie die Umsetzung aussehen soll.
4. Alternativen (`textarea`): Bereits erwogene andere Wege.
5. Auswirkung auf Kompatibilität (`dropdown`): Ob eine inkompatible Änderung betroffen ist.

## 3. Struktur der PR-Vorlage

### 3.1 Pflichtblöcke

`PULL_REQUEST_TEMPLATE.md` muss die folgenden Blöcke in fester Reihenfolge enthalten:

1. Änderungsbeschreibung: Was diese Änderung bewirkt und die zugehörige Issue-Nummer.
2. Änderungstyp: per Kontrollkästchen auswählen (Funktion, Fehlerbehebung, Dokumentation, Refactoring, Tests usw.; Typen siehe [Commit-Nachrichtenspezifikation](./commit-message-specification.md)).
3. Selbsttest-Checkliste: prüfbare Punkte zur Selbstkontrolle.
4. Inkompatible Änderungen: Falls keine vorliegt, „keine“ schreiben; andernfalls den Migrationsweg angeben (siehe [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)).
5. Zugehörige Dokumentation: Ob README, CHANGELOG und API-Dokumentation synchron aktualisiert wurden.

### 3.2 Beispiel einer Selbsttest-Checkliste

```markdown
## Selbsttest-Checkliste

- [ ] Lokaler Build erfolgreich
- [ ] Zugehörige Tests bestanden, neue Funktionen wurden durch Tests ergänzt
- [ ] Commit-Nachricht gemäß [Commit-Nachrichtenspezifikation](./commit-message-specification.md) verfasst
- [ ] Dokumentation synchron aktualisiert oder als nicht aktualisierungsbedürftig bestätigt
- [ ] Keine Schlüssel, personenbezogenen Daten oder großen Dateien eingebracht
```

## 4. Kopierbare Vorlagen

### 4.1 Formular für Fehlerberichte

Als `.github/ISSUE_TEMPLATE/bug-report.yml` speichern:

```yaml
name: Fehlerbericht
description: Meldet eine reproduzierbare funktionale Anomalie
title: "[Bug]: "
labels: ["bug"]
body:
  - type: markdown
    attributes:
      value: |
        Vor dem Absenden zuerst nach bestehenden Issues suchen, um Doppelmeldungen zu vermeiden.
        Keine Schlüssel, Tokens oder personenbezogenen Daten einfügen.
  - type: checkboxes
    id: duplicate-check
    attributes:
      label: Prüfung auf Doppelmeldung
      options:
        - label: Ich habe nach bestehenden Issues gesucht und bestätige, dass dies keine Doppelmeldung ist
          required: true
  - type: textarea
    id: description
    attributes:
      label: Problembeschreibung
      description: Was tatsächlich passiert
      placeholder: Nach dem Befehl install endet das Programm mit Exit-Code 1
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Erwartetes Verhalten
      description: Was passieren sollte
    validations:
      required: true
  - type: textarea
    id: steps
    attributes:
      label: Schritte zur Reproduktion
      description: Nummeriert auflisten, damit Dritte unabhängig reproduzieren können
      placeholder: |
        1. Befehl ausführen
        2. Ausgabe beobachten
        3. Anomalie tritt auf
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Projektversion
      placeholder: v1.0.0
    validations:
      required: true
  - type: dropdown
    id: os
    attributes:
      label: Betriebssystem
      options:
        - macOS
        - Linux
        - Windows
        - Sonstiges
    validations:
      required: true
  - type: textarea
    id: logs
    attributes:
      label: Logs oder Screenshots
      description: Fehlermeldung angeben; sensible Angaben müssen entfernt werden
      render: shell
  - type: checkboxes
    id: security
    attributes:
      label: Bestätigung der Informationssicherheit
      options:
        - label: Bestätigt, dass keine Schlüssel, Tokens oder personenbezogenen Daten enthalten sind
          required: true
```

### 4.2 Formular für Funktionswünsche

Als `.github/ISSUE_TEMPLATE/feature-request.yml` speichern:

```yaml
name: Funktionsanfrage
description: Neue Fähigkeit oder Verbesserungsvorschlag einreichen
title: "[Feature]: "
labels: ["enhancement"]
body:
  - type: textarea
    id: problem
    attributes:
      label: Problemdarstellung
      description: Welche Fähigkeit derzeit fehlt
    validations:
      required: true
  - type: textarea
    id: scenario
    attributes:
      label: Anwendungsfall
      description: Wer die Fähigkeit unter welchen Umständen benötigt
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Gewünschte Lösung
      description: Wie die Umsetzung aussehen soll
  - type: textarea
    id: alternatives
    attributes:
      label: Alternativen
      description: Bereits erwogene andere Wege
  - type: dropdown
    id: breaking
    attributes:
      label: Sind Breaking Changes betroffen
      options:
        - Nein
        - Ja
        - Unklar
    validations:
      required: true
```

### 4.3 PR-Vorlage

Als `.github/PULL_REQUEST_TEMPLATE.md` speichern:

````markdown
## Änderungsbeschreibung

{{变更说明}}

## Änderungstyp

- [ ] Funktion (feat)
- [ ] Fehlerbehebung (fix)
- [ ] Dokumentation (docs)
- [ ] Formatierung (style)
- [ ] Refactoring (refactor)
- [ ] Tests (test)
- [ ] Build oder Toolchain (build / ci)

## Selbsttest-Checkliste

- [ ] Lokaler Build erfolgreich
- [ ] Zugehörige Tests bestanden, neue Funktionen wurden durch Tests ergänzt
- [ ] Commit-Nachricht gemäß Commit-Nachrichtenspezifikation verfasst
- [ ] Dokumentation synchron aktualisiert oder als nicht aktualisierungsbedürftig bestätigt
- [ ] Keine Schlüssel, personenbezogenen Daten oder großen Dateien eingebracht

## Inkompatible Änderungen

{{破坏性变更说明}}

## Zugehörige Dokumentation

- [ ] README synchron aktualisiert oder nicht aktualisierungsbedürftig
- [ ] CHANGELOG eingetragen
- [ ] API-Dokumentation synchron aktualisiert oder nicht aktualisierungsbedürftig
````

### 4.4 Platzhalter-Übersicht

| Platzhalter | Erforderlich | Hinweise zum Ausfüllen |
| --- | --- | --- |
| `{{变更说明}}` | Ja | In einem Satz die Änderung benennen und die Issue-Nummer im Format `#数字` angeben |
| `{{破坏性变更说明}}` | Ja | Ohne inkompatible Änderung „keine“ schreiben; andernfalls Migrationsschritte nennen und auf den Migrationsleitfaden verlinken |

Die Felder `name`, `description`, `title` und `labels` der YAML-Formulare sind Vorlagen-Metadaten und werden an das tatsächliche Projekt angepasst; Feldtypen und `required`-Werte in `body` werden gemäß den Feldlisten in Abschnitt 2 und 3 angepasst, Pflichtfelder dürfen nicht gestrichen werden.

### 4.5 Vollständiges Ausfüllbeispiel

Ausfüllbeispiel eines Fehlerberichts:

````markdown
## Problembeschreibung

Nach Ausführung von `npm run build` endet der Prozess mit Rückgabecode 1.

## Erwartetes Verhalten

Der Build ist erfolgreich und gibt das Verzeichnis `dist/` aus.

## Reproduktionsschritte

1. Tag v1.0.0 auschecken
2. `npm ci` ausführen
3. `npm run build` ausführen, Rückgabecode 1 wird beobachtet

## Projektversion

v1.0.0

## Betriebssystem

macOS

## Protokoll oder Screenshot

```
Error: Cannot find module 'mdlint-core'
```

## Bestätigung der Informationssicherheit

- [x] Bestätigt, dass keine Schlüssel, Tokens oder personenbezogenen Daten enthalten sind
````

## 5. Schreibanforderungen

1. Feldbeschreibungen verwenden Imperativ- oder Aussagesätze und dürfen nicht umgangssprachlich sein.
2. Für jedes Pflichtfeld wird ein Ausfüllbeispiel oder eine Formatvorgabe angegeben.
3. Hinweistexte müssen erläutern, „warum diese Information benötigt wird“; pauschale Aufforderungen sind zu vermeiden.
4. Felder mit Datenschutzbezug müssen auf die Anonymisierung hinweisen (siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)).
5. Vorlagen werden mit der Projektentwicklung aktualisiert; verworfene Felder müssen entfernt und dürfen nicht dauerhaft mitgeschleppt werden.

## 6. Verbotene Praktiken

1. Es ist unzulässig, alle Problemtypen in einer einzigen Freitextvorlage zusammenzufassen.
2. Es ist unzulässig, Pflichtfelder festzulegen, die für die Eingrenzung des Problems irrelevant sind.
3. Es ist unzulässig, Projektvorstellungen oder Marketinginhalte in die Vorlagen aufzunehmen.
4. Es ist unzulässig, dass die PR-Vorlage die Selbsttest-Checkliste oder die Erklärung zu inkompatiblen Änderungen auslässt.

## Verwandte Dateien

- Abgrenzung der Dateizuständigkeiten siehe [Dokumentationsmatrix](./document-matrix.md)
- Beitragsablauf siehe [Beitragsleitfaden-Spezifikation](./contribution-guide-specification.md)
- Prüfmaßstäbe siehe [Code-Review-Spezifikation](./code-review-specification.md)
- Migration bei inkompatiblen Änderungen siehe [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md)
- Die Prüfung der Community-Governance gehört zu Dimension D14, siehe [Review-Dimensionsmatrix](./review-dimension-matrix.md)
