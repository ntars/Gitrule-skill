# SECURITY-Vorlage

> Problem, das diese Datei löst: Stellt eine direkt kopierbare Vorlage für eine Sicherheitsrichtlinie bereit, mit der ein Projekt SECURITY.md erzeugen kann, und legt unterstützte Versionen, Meldekanäle für Schwachstellen, Reaktionsablauf und Offenlegungsgrundsätze fest; die begleitenden Ausfüllhinweise decken die Auswahl der Meldekanäle und den Umgang mit sensiblen Informationen ab.

## 1. Gebrauchsanweisung

1. Den gesamten Inhalt von Abschnitt 3 „Vorlagentext“ kopieren und als `SECURITY.md` im Projektwurzelverzeichnis neu anlegen.
2. Die Platzhalter gemäß Abschnitt 4 ersetzen; Meldekanäle müssen real erreichbar sein und dürfen die Angriffsfläche nicht öffentlich exponieren.
3. Gemäß Abschnitt 5 auf die jeweilige Situation zuschneiden: Projekte ohne Mehrversionspflege löschen die Zeile der Altversion aus der Tabelle der unterstützten Versionen.
4. Sicherheitsregeln und Anforderungen an sensible Informationen siehe [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md); zur Dimension der Gemeinschaftsgovernance siehe [Prüfdimensionsmatrix](./review-dimension-matrix.md).

## 2. Anpassungsgrundsätze

- **Privater Kanal zuerst**: Schwachstellen werden über einen privaten Kanal gemeldet; Meldende dürfen nicht aufgefordert werden, Details in öffentlichen Tickets offenzulegen.
- **Klare Fristen**: Zeiträume für die erste Reaktion und die Behebung angeben, um unbefristete Zusagen zu vermeiden.
- **Minimierung von Informationen**: Meldende sind aufzufordern, nur die für die Reproduktion erforderlichen Mindestinformationen bereitzustellen; echte Produktivdaten dürfen nicht eingereicht werden.
- **Rechtliche Konsistenz**: Die Offenlegungsgrundsätze müssen mit geltendem Recht und Plattformrichtlinien übereinstimmen; in regulierten Branchen ist eine juristische Prüfung erforderlich.

## 3. Vorlagentext

```markdown
# Sicherheitsrichtlinie

> Diese Datei beschreibt den Sicherheits-Supportumfang von {{项目名称}} und den Meldeweg für Schwachstellen; sie gilt für Sicherheitsforschende, Beitragende und Nutzende.

## Unterstützte Versionen

| Version | Sicherheitsmeldungen akzeptiert |
| --- | --- |
| {{当前版本}} | Ja |
| {{上一版本}} | {{是否接受}} |
| Ältere Versionen | Nein |

## Meldekanäle

Sicherheitslücken dürfen nicht über öffentliche Tickets, Diskussionsforen oder soziale Kanäle gemeldet werden. Bitte nutzen Sie folgende private Kanäle:

- Sicherheits-E-Mail: {{真实可达的安全邮箱}}
- Privater Meldezugang: {{私有漏洞报告地址}}

Sind diese Kanäle nicht verfügbar, wenden Sie sich über {{备用私有联系方式}} an die Maintainer.

## Inhalt der Meldung

Zur Steigerung der Bearbeitungseffizienz bitte möglichst angeben:

- betroffene Version und Komponente;
- Schwachstellentyp und potenzielle Auswirkung;
- minimale Reproduktionsschritte oder Proof of Concept;
- empfohlene Behebungsrichtung (optional).

Bitte keine echten Produktivdaten, Schlüssel oder personenbezogenen Identifikationsdaten einreichen.

## Reaktionsablauf

| Phase | Zeitraum | Erläuterung |
| --- | --- | --- |
| Eingang bestätigt | {{首次响应时限}} | Maintainer bestätigen den Eingang der Meldung |
| Erste Bewertung | {{评估时限}} | Feststellung, ob ein Sicherheitsproblem vorliegt, und des Auswirkungsbereichs |
| Behebung und Verifikation | {{修复时限}} | Behebung abschließen und verifizieren; komplexe Fälle werden gesondert abgestimmt |
| Öffentliche Veröffentlichung | {{发布延迟}} nach Abschluss der Behebung | Sicherheitshinweis und korrigierte Version veröffentlichen |

## Offenlegungsgrundsätze

- Die Maintainer behandeln Identität und Inhalt der Meldung vertraulich bis zur Veröffentlichung der Behebung.
- Ohne Zustimmung der Maintainer dürfen Meldende Details der Schwachstelle nicht vor der Veröffentlichung der Behebung offenlegen.
- Nach der Veröffentlichung der Behebung danken die Maintainer den Meldenden im Sicherheitshinweis (mit deren Zustimmung).
- Gutgläubige Sicherheitsforschung im Einklang mit dieser Richtlinie wird nicht verfolgt.

## Ausnahmen und Haftungsausschluss

Diese Richtlinie stellt keine Zusage einer Sicherheitsgarantie dar; die Projektinhalte werden „wie besehen“ bereitgestellt, siehe [Haftungsausschluss](./DISCLAIMER.md) und [LICENSE](./LICENSE).
```

## 4. Platzhalterübersicht und Felddefinitionen

| Platzhalter | Pflicht | Felddefinition | Ausfüllbeispiel |
| --- | --- | --- | --- |
| `{{项目名称}}` | ja | Externer Projektname | `FooBar` |
| `{{当前版本}}` | ja | Aktuell gepflegte neueste Version oder `main` | `v2.3.0` |
| `{{上一版本}}` | nein | Noch gepflegte vorherige Version | `v2.2.x` |
| `{{是否接受}}` | ja | Ob diese Version Sicherheitsmeldungen akzeptiert | `ja` |
| `{{真实可达的安全邮箱}}` | ja | Ausschließlich für Sicherheitsmeldungen genutzte E-Mail-Adresse | `security@example.com` |
| `{{私有漏洞报告地址}}` | ja | Privater Meldezugang | `https://github.com/owner/repo/security/advisories/new` |
| `{{备用私有联系方式}}` | nein | Alternativer Weg bei Nichtverfügbarkeit des Hauptkanals | `Direktnachricht über das Maintainer-Konto` |
| `{{首次响应时限}}` | ja | Zeitraum bis zur Bestätigung des Eingangs | `3 Arbeitstage` |
| `{{评估时限}}` | ja | Zeitraum bis zum Abschluss der ersten Bewertung | `7 Arbeitstage` |
| `{{修复时限}}` | ja | Zeitraum bis zum Abschluss der Behebung | `30 Tage` |
| `{{发布延迟}}` | ja | Abstand zwischen Behebung und öffentlicher Veröffentlichung | `7 Tage` |

## 5. Ausfüllhinweise und Szenariovarianten

| Szenario | Zwingend beizubehaltende Abschnitte | Kürzbare Abschnitte | Anpassungspunkte |
| --- | --- | --- | --- |
| Projekt mit einer Version | Meldekanäle, Inhalt der Meldung, Reaktionsablauf, Offenlegungsgrundsätze | Zeile der Altversion in der Tabelle der unterstützten Versionen löschen | Aktuelle Version als `main` oder neuesten Tag angeben |
| Pflege mehrerer Versionen | alle | keine | Zeilenweise alle Versionen auflisten, die Meldungen noch akzeptieren |
| Privates Projekt | alle | Tabelle der unterstützten Versionen kann verkürzt werden | Für den privaten Kanal eine dauerhaft betreute E-Mail-Adresse verwenden |
| Unternehmensprojekt | alle | keine | Fristen müssen mit der internen Sicherheitsrichtlinie übereinstimmen und juristisch geprüft sein |
| Regulierte Branche | alle | keine | Meldepflichten gegenüber Aufsichtsbehörden und Anforderungen an die Datenaufbewahrung ergänzen |

Übersicht häufiger Fehler:

| Fehlerhafte Schreibweise | Folge | Korrekte Schreibweise |
| --- | --- | --- |
| „Bitte Schwachstellen im Issue melden“ | Details werden öffentlich, Risiko steigt | Privaten Kanal verwenden |
| „Wir bearbeiten das so schnell wie möglich“ | Keine klare Erwartung, Meldende können nicht planen | Zeiträume phasenweise angeben |
| Frist „Behebung innerhalb von 24 Stunden“ | Überzogene Zusage, nicht einhaltbar | Angemessenen Zeitraum angeben und komplexe Fälle als gesondert abzustimmen kennzeichnen |
| Keine Maskierungsanforderung | Meldende reichen möglicherweise echte Produktivdaten ein | Echte Daten und Schlüssel ausdrücklich verbieten |

## 6. Vollständiges Beispiel

Nachfolgend ein ausgefülltes Beispiel für den Abschnitt „Meldekanäle“, nur als Formatreferenz.

```markdown
## Meldekanäle

Sicherheitslücken dürfen nicht über öffentliche Tickets, Diskussionsforen oder soziale Kanäle gemeldet werden. Bitte nutzen Sie folgende private Kanäle:

- Sicherheits-E-Mail: security@example.com
- Privater Meldezugang: https://github.com/example/democli/security/advisories/new

Bitte keine echten Produktivdaten, Schlüssel oder personenbezogenen Identifikationsdaten einreichen.
```

## Verwandte Dateien

- Zugehörige Spezifikation: [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md)
- Begleitende Vorlagen: [Verhaltenskodex-Vorlage](./code-of-conduct-template.md), [Contributing-Guide-Vorlage](./contribution-guide-template.md), [Haftungsausschluss-Vorlage](./disclaimer-template.md)
- Dimension der Schwachstellenmeldung: [Prüfdimensionsmatrix](./review-dimension-matrix.md)
- Behandlung von Schlüsselleckagen: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Zurück zum chinesischen Index: [README](./README.md)
