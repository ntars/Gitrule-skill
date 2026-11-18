# Git-Workflow- und Branch-Spezifikation

> Problem, das diese Datei löst: Sie definiert Branch-Modell, Namensregeln, Vorlage der Pull-Request-Beschreibung und Zusammenführungsstrategie, damit der Hauptzweig stabil bleibt, die Zusammenarbeit geordnet verläuft und Änderungen nachvollziehbar sind.

## 1. Spezifikationsregeln

1. Der Standardbranch (`main` oder `master`) muss geschützt sein; ein direkter Push ist unzulässig (entspricht der harten Regel H7).
2. Alle Änderungen werden über einen persönlichen Branch und einen Pull Request in den Hauptzweig zusammengeführt.
3. Langfristige und kurzfristige Branches sind klar zu trennen, damit Branches nicht dauerhaft unzusammengeführt bleiben.
4. `git push --force` auf gemeinsame Branches ist unzulässig; für das Umschreiben persönlicher Branches ist `--force-with-lease` zu verwenden (entspricht H8).
5. Ein Rebase oder Amend bereits gepushter gemeinsamer Branches ist unzulässig; vor der Zusammenführung müssen CI und Code-Review bestanden sein.

## 2. Branch-Modell

| Branch-Typ | Lebenszyklus | Erstellt von | Zusammengeführt nach | Namensformat | Beispiel |
| --- | --- | --- | --- | --- | --- |
| Standardbranch | Langfristig | — | — | `main` | `main` |
| Feature-Branch | Kurzfristig, ≤2 Wochen | `main` | `main` | `feat/<简述>` | `feat/user-login` |
| Fix-Branch | Kurzfristig, ≤1 Woche | `main` | `main` | `fix/<简述>` | `fix/token-expiry` |
| Dokumentations-Branch | Kurzfristig | `main` | `main` | `docs/<简述>` | `docs/api-guide` |
| Release-Branch | Mittelfristig | `main` | `main` + Tag | `release/<版本>` | `release/1.2.0` |
| Notfallkorrektur | Kurzfristig, ≤24 Stunden | Release-Tag | `main` + Tag | `hotfix/<简述>` | `hotfix/payment-error` |

Namensregeln: Kleinschreibung in kebab-case, die Kurzbeschreibung muss die Absicht ausdrücken; `test`, `temp`, `wip`, `my-xxx` sind unzulässig; bei Bezug zu einer Anforderung wird die Anforderungsnummer angehängt, zum Beispiel `feat/spacing-rule-req001`.

## 3. Vorlage der Pull-Request-Beschreibung

```markdown
## Zweck der Änderung
{{一句话说明为什么需要此变更，关联需求编号}}

## Änderungsinhalt
- {{具体改动 1}}
- {{具体改动 2}}

## Auswirkungsumfang
- Betroffene Module: {{模块名}}
- Kompatibilität beeinträchtigt: {{是 / 否；是则给出迁移说明}}
- Konfigurations- oder Datenmigration betroffen: {{是 / 否；是则说明}}

## Nachweis
- Selbsttest-Befehl: {{命令}}
- Neue oder geänderte Tests: {{TC 编号}}
- CI-Lauf-URL: {{URL}}

## Verknüpfungen
- Anforderung: {{REQ-NNN}}
- Verfolgungsmatrix: {{已更新 / 待更新}}
- Dokumentation: {{docs/api.md#章节 / 无}}
- Issue: {{#编号 / 无}}

## Selbstprüfung
- [ ] Commit-Nachricht entspricht der Spezifikation
- [ ] Keine sensiblen Informationen enthalten
- [ ] Anforderungs-Verfolgungsmatrix aktualisiert
- [ ] Breaking Change im Änderungsprotokoll eingetragen
```

## 4. Felddefinitionen

| Feld | Pflichtfeld | Typ | Hinweise zum Ausfüllen | Beispiel |
| --- | --- | --- | --- | --- |
| Branch-Kurzbeschreibung | Ja | kebab-case | Muss die Absicht eigenständig ausdrücken, informationslose Wörter unzulässig | `spacing-rule` |
| Zugeordnete Anforderung | Ja | `REQ-NNN` | Muss mit der Projektstart-Nummer übereinstimmen | `REQ-001` |
| Zweck der Änderung | Ja | Text | Beschreibt das „Warum“, nicht das „Was“ | `Falschmeldung bei chinesischen Satzzeichen beheben` |
| Auswirkungsumfang | Ja | Text | Muss angeben, ob die Kompatibilität beeinträchtigt wird | `Nein` |
| Selbsttest-Befehl | Ja | Befehl | Kopierbar und ausführbar | `npm test -- -t spacing` |
| Testnummer | Ja | `TC-NNN` | Muss mit der Nummerierung der Test-Spezifikation übereinstimmen | `TC-001` |
| CI-URL | Ja | URL | Erleichtert die Nachprüfung durch Prüfende | `https://github.com/.../runs/123` |
| Selbstprüfungsliste | Ja | Auswahlfeld | Punkt für Punkt auswählen, nicht den ganzen Block auf einmal | — |

## 5. Hinweise zum Ausfüllen

1. **Lebenszyklus von Branches**: Feature-Branches, die länger als 2 Wochen nicht zusammengeführt sind, erfordern eine Erläuterung in der Iterationsretrospektive sowie eine Aufteilung oder Schließung.
2. **Benennung der Kurzbeschreibung**: Aus dem Zweck der Änderung das zentrale Substantiv und die Aktion entnehmen; unklare Namen wie `fix2` oder `new-feature` sind unzulässig.
3. **Zweck der Änderung**: Problem und Nutzen beschreiben; „Code aktualisieren“ oder „Logik optimieren“ sind unzureichend.
4. **Auswirkungsumfang**: Wird eine Beeinträchtigung der Kompatibilität markiert, ist zugleich im Änderungsprotokoll `BREAKING CHANGE:` zu vermerken.
5. **Selbsttest-Befehl**: Prüfende müssen ihn direkt kopieren und ausführen können und zum selben Ergebnis gelangen; bei komplexen Schritten ist der Skriptpfad anzugeben.
6. **Verfolgungsmatrix**: Vor der Zusammenführung des PR sind im [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md) die Felder Umsetzungs-PR und Status zu aktualisieren.
7. **Force Push**: `--force-with-lease` ist ausschließlich für den eigenen, noch nicht von anderen geprüften Branch zu verwenden, und der Grund ist im PR anzugeben.

Häufige Fehler:

| Fehlerhafte Formulierung | Problem | Korrektur |
| --- | --- | --- |
| Branch-Name `test`, `temp` | Keine Absicht erkennbar | Ändern in `feat/<具体能力>` |
| PR-Beschreibung enthält nur „Bug behoben“ | Auswirkung nicht prüfbar | Zweck, Auswirkung und Nachweis ergänzen |
| Direkter Push auf `main` | Verstoß gegen H7 | Über PR zusammenführen |
| Geprüfter Branch wird umgeschrieben und force gepusht | Review-Ergebnis verliert Gültigkeit | Neue Commits zur Beantwortung der Anmerkungen |
| Quellbranch wird nach der Zusammenführung nicht gelöscht | Branchliste wächst | Unmittelbar nach der Zusammenführung löschen |

## 6. Vollständiges Beispiel

```markdown
## Zweck der Änderung
Falschmeldung der Leerzeichenregel bei chinesischen Satzzeichen direkt neben englischen Wörtern beheben (REQ-004).

## Änderungsinhalt
- Regel-Engine um Prüfung der Satzzeichengrenze erweitert
- Zugehörigen Regressionstestfall ergänzt

## Auswirkungsumfang
- Betroffene Module: Regel spacing
- Kompatibilität beeinträchtigt: Nein
- Konfigurations- oder Datenmigration betroffen: Nein

## Nachweis
- Selbsttest-Befehl: `npm test -- -t "中文标点"`
- Neue oder geänderte Tests: TC-007-regression-142
- CI-Lauf-URL: https://github.com/example/markdown-lint-cli/actions/runs/128

## Verknüpfungen
- Anforderung: REQ-004
- Verfolgungsmatrix: Aktualisiert
- Dokumentation: Keine
- Issue: #142

## Selbstprüfung
- [x] Commit-Nachricht entspricht der Spezifikation
- [x] Keine sensiblen Informationen enthalten
- [x] Anforderungs-Verfolgungsmatrix aktualisiert
- [x] Breaking Change im Änderungsprotokoll eingetragen (diese Änderung ist nicht breaking)
```

## Verwandte Dateien

- Prüfmaßstab und Stufung der Anmerkungen: [Code-Review-Spezifikation](./code-review-specification.md)
- Commit-Format: [Commit-Nachrichten-Spezifikation](./commit-message-specification.md)
- Aktualisierung des Verfolgungsstatus: [Anforderungs-Verfolgungsmatrix-Spezifikation](./requirements-traceability-matrix-specification.md)
- Branches und Veröffentlichung als Dimension D8: [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
- Verbindliche Regeln H7/H8: [Harte Regeln](./hard-rules.md)
- Push-Vorgänge: [Push- und Veröffentlichungs-Spezifikation](./push-and-release-specification.md)
