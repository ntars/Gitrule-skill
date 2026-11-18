# Sicherheits- und Datenschutzspezifikation

> Problem, das diese Datei löst: Definiert Schutz sensibler Informationen, Datenschutzverzeichnis, SECURITY.md-Vorlage und Felder für Schwachstellenmeldungen, damit vor der Veröffentlichung keine Leckage besteht, die Datenverarbeitung konform ist und der Schwachstellenkanal erreichbar ist.

## 1. Spezifikationsbestimmungen

1. Schlüssel, Token, private Schlüssel, `.env`, Cloud-Anbieter-AK/SK sowie Datenbank-Verbindungszeichenfolgen dürfen nicht committet werden (entspricht harter Regel H3).
2. Der Schlüssel-Scan muss den Arbeitsbereich und die vollständige Historie abdecken und vor dem Push ausgeführt werden (siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)).
3. Interne Domains, IP-Adressen, personenbezogene Daten und Log-Rückstände müssen vor der Veröffentlichung bereinigt werden (entspricht Dimension D1).
4. Wurde ein Schlüssel bereits gepusht, sind unverzüglich Rotation und Historienbereinigung durchzuführen; ein reiner Lösch-Commit genügt nicht (entspricht H12).
5. Es ist anzugeben, welche Daten erhoben werden, zu welchem Zweck, an welchem Speicherort und mit welcher Aufbewahrungsfrist; Übertragung und Speicherung sind verschlüsselt, die Anzeige ist zu maskieren.
6. Das Berechtigungsmodell folgt dem Prinzip der minimalen Notwendigkeit; grenzüberschreitende Daten sind gesondert zu bewerten.
7. Ein Schwachstellenkanal, der die Maintainer direkt erreicht, ist bereitzustellen; Vertraulichkeit und Reaktionsfristen sind zuzusichern; bekannte Risiken sind wahrheitsgemäß zu benennen, absolute Sicherheit darf nicht zugesichert werden.

## 2. Vorlage zur Selbstprüfung sensibler Informationen

```markdown
# Selbstprüfung sensibler Informationen: {{项目名称}}

Prüfdatum: {{YYYY-MM-DD}} ｜ Durchführende Person: {{姓名}} ｜ Historie abgedeckt: {{是 / 否}}

| Prüfpunkt | Werkzeug / Befehl | Ergebnis | Behandlung |
| --- | --- | --- | --- |
| Schlüssel im Arbeitsbereich | {{扫描工具}} | {{命中数}} | {{已清理 / 无}} |
| Schlüssel in historischen Commits | {{扫描工具 --all}} | {{命中数}} | {{已轮换 / 无}} |
| `.env` und Anmeldedatendateien | `git ls-files \| grep -E ...` | {{文件数}} | {{已移除 / 无}} |
| Interne Domains / IP-Adressen | {{检索命令}} | {{命中数}} | {{已替换 / 无}} |
| Personenbezogene Daten | {{检索命令}} | {{命中数}} | {{已脱敏 / 无}} |
| Log- und Snapshot-Rückstände | {{检查命令}} | {{命中数}} | {{已清理 / 无}} |

Ergebnis: {{通过 / 不通过}}
- Liste rotierter Schlüssel: {{无 / 列出}}
- Prüfende Person: {{姓名}}
```

## 3. Vorlage für das Datenschutzverzeichnis

```markdown
# Datenschutzverzeichnis: {{项目名称}}

## Datenpositionen
| Datenposition | Erhebungszweck | Erhebungsart | Speicherort | Aufbewahrungsfrist | Verschlüsselung | Maskierung | Weitergabe an Dritte |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{如邮箱}} | {{账号识别}} | {{用户填写}} | {{数据库字段}} | {{删除账号后 30 天}} | {{是}} | {{展示时掩码}} | {{无}} |

## Berechtigungsmodell
| Rolle | Zugängliche Daten | Berechtigungsgrundlage | Prüfzyklus |
| --- | --- | --- | --- |
| {{角色}} | {{最小必要范围}} | {{业务需要}} | {{每季度}} |

## Konformitätsbewertung
- Anwendbare regionale Vorschriften: {{列举}}
- Grenzüberschreitende Datenübertragung: {{无 / 评估结论与措施}}
- Reaktion auf Nutzerrechte: {{查询 / 更正 / 删除的渠道与时限}}
```

## 4. SECURITY.md-Vorlage

```markdown
# Sicherheitsrichtlinie

## Unterstützte Versionen
| Version | Sicherheitsmeldungen akzeptiert |
| --- | --- |
| {{最新主版本}} | Ja |
| {{旧版本}} | Nein / nur schwerwiegende Probleme |

## Meldekanäle
- Bevorzugt: {{私密渠道，如 GitHub Security Advisories}}
- Alternativ: {{加密邮箱}}
- Schwachstellen dürfen nicht über öffentliche Issues gemeldet werden.

## Reaktionszusagen
| Phase | Frist |
| --- | --- |
| Eingang bestätigt | {{2 个工作日}} |
| Erste Bestätigung | {{5 个工作日}} |
| Behebung und Offenlegung | {{视严重程度，目标 30 天}} |

## Bearbeitungsablauf
Eingang → Bestätigung → Behebung → Offenlegung → Ankündigung

## Bekannte Risiken
{{如实说明当前已知风险；无则写「暂无已知风险」，不得承诺绝对安全}}
```

## 5. Felddefinitionen

| Feld | Pflicht | Typ | Ausfüllhinweis | Beispiel |
| --- | --- | --- | --- | --- |
| Historie abgedeckt | ja | Enumeration | Nur bei Auswahl „ja“ kann „bestanden“ festgestellt werden | `ja` |
| Prüfpunkt.Ergebnis | ja | Zahl | Trefferzahl eintragen; „vermutlich keine“ ist unzulässig | `0` |
| Liste rotierter Schlüssel | bedingt Pflicht | Liste | Pflicht bei Treffern, rotierte Anmeldedaten auflisten | `API_KEY rotiert` |
| Datenposition.Aufbewahrungsfrist | ja | Text | Konkrete Dauer; „langfristig“ ist unzulässig | `30 Tage nach Kontolöschung` |
| Datenposition.Weitergabe an Dritte | ja | Text | Ohne Weitergabe „keine“ schreiben | `keine` |
| Unterstützte Versionen | ja | Tabelle | Klarstellen, welche Versionen Meldungen akzeptieren | `2.x: ja` |
| Meldekanäle | ja | Text | Mindestens ein nicht öffentlicher Kanal | `Security Advisories` |
| Reaktionsfrist | ja | Dauer | Für jede Phase ein Zahlenwert | `2 Arbeitstage` |

## 6. Ausfüllhinweise

1. **Historien-Scan**: Der Schlüssel-Scan muss die vollständige git-Historie umfassen; nur der Arbeitsbereich gilt als ungültig.
2. **Schlüsseltreffer**: Wird ein bereits gepushter Schlüssel gefunden, zuerst rotieren, dann die Historie bereinigen; die Reihenfolge darf nicht vertauscht werden (entspricht H12).
3. **Maskierung**: Sensible Felder in Anzeige und Logs müssen maskiert werden; das vollständige Ausgeben von Token, Ausweisnummern oder Mobilfunknummern ist verboten.
4. **Aufbewahrungsfrist**: „Dauerhafte Speicherung“ ist nicht zulässig; eine klare Frist oder ein Löschauslöser ist anzugeben.
5. **Unterstützte Versionen**: Mindestens die aktuelle Hauptversion auflisten; nicht unterstützte Altversionen müssen ausdrücklich genannt werden, damit Nutzer keine Fehlmeldungen abgeben.
6. **Meldekanäle**: Es muss ein nicht öffentlicher Kanal sein; die Offenlegung einer Schwachstelle in einem öffentlichen Issue vergrößert das Risiko.
7. **Bekannte Risiken**: Wahrheitsgemäß auflisten; „Dieses System ist absolut sicher“ ist eine verbotene Formulierung.

Häufige Fehler:

| Fehlerhafte Schreibweise | Problem | Korrektur |
| --- | --- | --- |
| Schlüssel nur per Commit löschen, nicht rotieren | Verstoß gegen H12 | Zuerst rotieren, dann Historie bereinigen |
| Selbstprüfung nur im Arbeitsbereich | Historische Leckagen werden übersehen | Historien-Scan ergänzen |
| Datenaufbewahrung als „unbegrenzt“ angeben | Keine Grenze | Konkrete Frist angeben |
| Schwachstellen über öffentliches Issue melden | Vergrößert die Angriffsfläche | Auf privaten Kanal wechseln und in SECURITY.md dokumentieren |
| „Absolute Sicherheit“ zusichern | Unwahre Aussage | Durch wahrheitsgemäße Darstellung bekannter Risiken ersetzen |

## 7. Vollständiges Beispiel

```markdown
## Selbstprüfung sensibler Informationen: markdown-lint-cli

Prüfdatum: 2026-11-18 ｜ Durchführende Person: Wang Wu ｜ Historie abgedeckt: ja

| Prüfpunkt | Werkzeug / Befehl | Ergebnis | Behandlung |
| --- | --- | --- | --- |
| Schlüssel im Arbeitsbereich | gitleaks detect | 0 | keine |
| Schlüssel in historischen Commits | gitleaks detect --log-opts=--all | 0 | keine |
| `.env` und Anmeldedatendateien | git ls-files | 0 | keine |
| Interne Domains / IP-Adressen | Regex-Suche | 0 | keine |

Ergebnis: bestanden
- Liste rotierter Schlüssel: keine
- Prüfende Person: Li Si
```

## Verwandte Dateien

- Rote Linien für Schlüssel H3/H12: [Harte Regeln](./hard-rules.md)
- Behandlung von Vorfällen mit bereits geleakten Schlüsseln: [Incident-Reaktionsspezifikation](./incident-response-specification.md)
- Scan-Ausführung vor dem Push: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Log-Maskierung: [Observability-Spezifikation](./observability-specification.md)
- Abgrenzung der SECURITY-Dokumentation: [Dokumentationsmatrix](./document-matrix.md)
- Darstellung bekannter Risiken in der README: [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Vereinbarungen für das Gemeinschaftsverhalten: [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md)
