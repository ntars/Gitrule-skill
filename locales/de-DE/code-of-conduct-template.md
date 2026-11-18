# Verhaltenskodex-Vorlage

> Problem, das diese Datei löst: Stellt eine direkt kopierbare Vorlage für einen Verhaltenskodex bereit, damit Projekte `CODE_OF_CONDUCT.md` erzeugen können; sie legt Beteiligungsversprechen, erwartetes Verhalten, nicht akzeptables Verhalten, Durchsetzungsverantwortung und Meldeweg fest, und die begleitenden Ausfüllhinweise decken Anpassungsquelle und Versionsangabe ab.

## 1. Verwendungshinweise

1. Den gesamten Inhalt von „Vorlagentext“ aus Abschnitt 3 kopieren und als `CODE_OF_CONDUCT.md` im Projektwurzelverzeichnis neu anlegen.
2. Gemäß Abschnitt 4 die Platzhalter ersetzen; der Meldeweg muss eine real erreichbare Adresse sein.
3. Bei Übernahme oder Anpassung eines Verhaltenskodex mit eigener Version sind in Abschnitt 5 gemäß den Quellanforderungen Version und Lizenz zu erklären; Grundlage siehe [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md), Abschnitt 1, Punkt 8.
4. Diese Datei in der [Contributing-Guide-Vorlage](./contribution-guide-template.md) und im Beitragsabschnitt der README verlinken, um bidirektionale Erreichbarkeit zu gewährleisten.

## 2. Anpassungsprinzipien

- **Technologieunabhängig**: Der Kodex enthält keine technischen Inhalte und regelt ausschließlich das Verhalten bei der Beteiligung; zur Abgrenzung siehe [Dokumentationsmatrix](./document-matrix.md).
- **Durchsetzbar**: Abgestufte Maßnahmen müssen Auslösebedingungen und Maßnahmen nennen; Prinzipien ohne Folgen sind unzulässig.
- **Erreichbarkeit**: Der Meldeweg muss real gültig sein; Beispieladressen sind unzulässig.
- **Konforme Quelle**: Bei Anpassung eines Kodex Dritter sind dessen Namensnennungs- und Lizenzanforderungen beizubehalten, siehe [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md).

## 3. Vorlagentext

```markdown
# Verhaltenskodex

## Unser Versprechen

Wir als Beteiligte, Beitragende und Maintainer von {{项目名称}} verpflichten uns, gemeinsam ein offenes, freundliches und belästigungsfreies Umfeld der Beteiligung zu schaffen – unabhängig von Alter, Körpergröße, Behinderung, ethnischer Herkunft, Geschlechtsidentität und -ausdruck, Erfahrungsniveau, Bildung, sozioökonomischem Status, Nationalität, äußerer Erscheinung oder sexueller Orientierung.

## Geltungsbereich

Dieser Kodex gilt in Projektbereichen, Issues, Pull Requests, Code-Reviews, sozialen Kanälen sowie in der Öffentlichkeit, wenn eine Person in Vertretung des Projekts auftritt.

## Erwartetes Verhalten

- Unterschiedliche Standpunkte und Erfahrungen respektieren, in gutem Glauben kommunizieren.
- Konstruktives Feedback annehmen, auf die Sache und nicht auf die Person fokussieren.
- Das Gesamtinteresse der Community in den Blick nehmen und Schaden für das Projekt und seine Beteiligten vermeiden.
- Gegenüber Neueinsteigenden geduldig sein und umsetzbare Verbesserungsvorschläge machen.

## Nicht akzeptables Verhalten

- Persönliche Angriffe, beleidigende oder herabsetzende Äußerungen.
- Diskriminierende Äußerungen und Belästigung aufgrund eines geschützten Merkmals.
- Öffentliche oder private Belästigung, Nachstellung, unerwünschte wiederholte Kontaktaufnahme.
- Unbefugte Veröffentlichung privater Informationen anderer.
- Sonstiges Verhalten, das in einem professionellen Umfeld vernünftigerweise als unangemessen gilt.

## Durchsetzungsverantwortung

Die Maintainer des Projekts klären die Anwendung dieses Kodex, entscheiden über Verstöße und sind berechtigt, Inhalte zu löschen, zu bearbeiten oder abzulehnen, die diesem Kodex nicht entsprechen. Maintainer müssen ihre Aufgaben konsistent und unparteiisch wahrnehmen und sich bei Konflikten, die sie selbst betreffen, aktiv der Mitwirkung enthalten.

## Maßnahmen

Verstöße werden nach Schwere abgestuft behandelt:

| Stufe | Anwendungsfall | Maßnahme |
| --- | --- | --- |
| Stufe 1 | Unbeabsichtigte Kränkung, geringfügiges Fehlverhalten | Persönlicher Hinweis und Erläuterung |
| Stufe 2 | Wiederholtes Auftreten oder eindeutiger Verstoß | Öffentliche Verwarnung, Korrektur mit Frist |
| Stufe 3 | Schwere Belästigung, böswillige Angriffe | Vorübergehende Sperre der Beteiligungsrechte |
| Stufe 4 | Fortdauerndes oder nicht wiedergutzumachendes schweres Verhalten | Dauerhafte Sperre mit Aufzeichnung |

## Meldeweg

Bei Erleben oder Beobachten eines Verstoßes gegen diesen Kodex wenden Sie sich bitte über {{真实可达的举报邮箱或渠道}} an das Maintainer-Team. Alle Meldungen werden vertraulich behandelt; Maintainer dürfen die Identität der meldenden Person nicht gegenüber der gemeldeten Person offenlegen, es sei denn, die meldende Person stimmt ausdrücklich zu.

## Namensnennung und Quelle

{{准则来源声明}}
```

## 4. Platzhaltertabelle und Felddefinitionen

| Platzhalter | Pflicht | Felddefinition | Ausfüllbeispiel |
| --- | --- | --- | --- |
| `{{项目名称}}` | ja | Öffentlicher Projektname, identisch mit der ersten Zeile der README | `FooBar` |
| `{{真实可达的举报邮箱或渠道}}` | ja | Reale Adresse, über die Maintainer direkt erreichbar sind | `conduct@example.com` |
| `{{准则来源声明}}` | ja | Bei Original „Original“ eintragen; bei Anpassung Name der Quelle, Version und Lizenz angeben | `Angepasst von Contributor Covenant 2.1 (CC BY 4.0)` |

## 5. Ausfüllhinweise und Szenariovarianten

| Szenario | Anpassungsschwerpunkte |
| --- | --- |
| Persönliches Projekt | Als Maintainer die eigene Person eintragen; für den Meldeweg eine langfristig gehaltene E-Mail-Adresse verwenden |
| Unternehmensprojekt | Rechts- oder Community-Team als durchsetzende Stelle benennen; Maßnahmen müssen mit internen Richtlinien übereinstimmen |
| Übernahme eines bekannten Kodex | Vollständigen Originaltext und Version beibehalten, nur Meldeweg und Namensnennung ergänzen |
| Mehrsprachiges Projekt | Klauseln der Sprachfassungen entsprechen einander Punkt für Punkt; englische oder chinesische Fassung als maßgeblich bestimmen und kennzeichnen |

Gegenüberstellung häufiger Fehler:

| Fehlerhafte Schreibweise | Folge | Korrekte Schreibweise |
| --- | --- | --- |
| Nur „freundliche Kommunikation ist willkommen“ schreiben | Keine Durchsetzungsgrundlage, Konflikte nicht entscheidbar | Erwartetes Verhalten, nicht akzeptables Verhalten und abgestufte Maßnahmen auflisten |
| Platzhalter-E-Mail als Meldeweg belassen | Nicht erreichbar, Meldeweg funktionslos | Reale und langfristig gültige Adresse eintragen |
| Angepasster Kodex ohne Namensnennung | Verstoß gegen Lizenzanforderungen der Quelle | Quelle, Version und Lizenz erklären |

## 6. Vollständiges Beispiel

Im Folgenden ein Auszug für ein Anpassungsszenario, nur als Formatreferenz.

```markdown
## Meldeweg

Bei Erleben oder Beobachten eines Verstoßes gegen diesen Kodex wenden Sie sich bitte über conduct@example.com an das Maintainer-Team. Alle Meldungen werden vertraulich behandelt.

## Namensnennung und Quelle

Dieser Kodex ist angepasst von Contributor Covenant 2.1 und steht unter der Lizenz CC BY 4.0.
```

## Verwandte Dateien

- Zugehörige Spezifikation: [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md)
- Begleitende Vorlagen: [Contributing-Guide-Vorlage](./contribution-guide-template.md), [SECURITY-Vorlage](./security-template.md)
- Dimension Community-Governance: [Audit-Dimensionsmatrix](./review-dimension-matrix.md)
- Zurück zum chinesischen Index: [README](./README.md)
