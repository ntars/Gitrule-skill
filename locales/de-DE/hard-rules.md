# Harte Regeln

> Problem, das diese Datei löst: Listet die unverletzbaren Regeln auf, deren Verletzung den Push blockiert – „erst pushen, dann korrigieren“ ist nicht zulässig.

## Tabelle der harten Regeln

| # | Regel |
|---|---|
| H1 | Der Repository-Name muss der [Projektnamens-Spezifikation](./project-naming-specification.md) entsprechen; Groß-/Kleinschreibung, Zeichen und Länge müssen vollständig konform sein |
| H2 | Eine `LICENSE`-Datei muss vorhanden sein; keine Lizenz = standardmäßig alle Rechte vorbehalten, eine Veröffentlichung ist unzulässig |
| H3 | Es dürfen keine Schlüssel, Tokens, privaten Schlüssel, `.env`-Dateien, Cloud-AK/SK oder Datenbank-Verbindungszeichenketten committet werden |
| H4 | Es dürfen keine Build-Artefakte, Abhängigkeitsverzeichnisse, IDE-Konfigurationen oder Systemmüll-Dateien committet werden |
| H5 | Eine einzelne Datei darf 100 MB nicht überschreiten; ab 50 MB muss LFS verwendet oder die Datei ausgeschlossen werden |
| H6 | Eine `README.md` muss vorhanden sein und Folgendes enthalten: Positionierung in einem Satz, Installation, minimales lauffähiges Beispiel, Lizenz |
| H7 | Der Standard-Branch muss geschützt sein; ein direkter Push auf `main`/`master` ist verboten |
| H8 | `git push --force` auf öffentliche Branches ist verboten; bei persönlichen Branches ist ausschließlich `--force-with-lease` zulässig |
| H9 | Vor dem Push müssen `build` und `test` erfolgreich sein; bei rotem CI darf nicht in den Hauptzweig zusammengeführt werden |
| H10 | Commit-Nachrichten müssen Conventional Commits entsprechen; informationsfreie Commits wie `wip`/`update`/`fix bug` sind verboten |
| H11 | Jedes Dokument ist eine eigenständige Datei mit eigenständiger Verantwortung; es ist verboten, alle Inhalte in die README zu stopfen (siehe [Dokumentmatrix](./document-matrix.md)) |
| H12 | Sobald ein Schlüssel gepusht wurde, muss er sofort rotiert und die Historie bereinigt werden; ein reiner Lösch-Commit ist nicht zulässig |

## Durchsetzungsvorgaben

- Die Verletzung einer einzigen Regel **blockiert den Push**; „erst pushen, dann korrigieren“ ist nicht zulässig.
- Das Ergebnis der Prüfung von H1–H12 muss in der Problemliste des [Prüfberichtsformats](./audit-report-format.md) erscheinen, jeweils mit Beleg (Pfad:Zeile / Befehlsausgabe).
- Bei einer Verletzung von H12 ist das Incident-Verfahren der [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md) anzuwenden.

## Verwandte Dateien

- Namensdetails siehe [Projektnamens-Spezifikation](./project-naming-specification.md)
- Freigabebedingungen des Qualitätstors siehe [Qualitätstor](./quality-gate.md)
- Zusammenfassung der verbotenen Praktiken siehe [Verbotene Praktiken](./prohibited-practices.md)
