# Open-Source-Promotion-Spezifikation

> Problem, das diese Datei löst: Definiert Promotionskanäle, Veröffentlichungsrhythmus, Materialien für die Startseite und Regeln für die Community-Betreuung von Open-Source-Projekten vor und nach der Veröffentlichung, damit ein Projekt mit nutzbarer Dokumentation eine Sichtbarkeit erreicht, die zu seinen Zielgruppen passt.

Die Kanalliste und die Grundsätze dieser Datei orientieren sich am Promotionskapitel aus phodals *A Guide to GitHub*; jenes Projekt hat mit 11.362 Stars die Anwendbarkeit dieser Vorgehensweisen in der chinesischen Open-Source-Community belegt.

## 1. Grundprinzipien

1. **Qualität vor Promotion**: Promotion verstärkt vorhandene Qualität, sie behebt keine Mängel. Vor der Fertigstellung von README, Beispielen, Dokumentation und Tests darf keine Promotion beginnen.
2. **Das Projekt allein ist nicht die gesamte Promotion**: Neben Code und README sind ausführliche Dokumentation, Beispielprogramme und ein Mechanismus zur Reaktion auf Probleme bereitzustellen.
3. **Klares Motiv**: Promotion dient einem konkreten Ziel (frühe Nutzende gewinnen, Beitragende anwerben, Feedback sammeln); Promotion zum Zweck der Star-Jagd ist unzulässig.
4. **Kanalpassung**: Kanäle nach Technologie-Stack und Zielgruppe wählen; unterschiedsloses Ausspielen ist zu vermeiden.
5. **Ehrliche Darstellung**: Star-Zahlen, Downloadzahlen oder Anwendungsfälle dürfen nicht erfunden werden; Funktionsvergleiche müssen auf überprüfbaren Fakten beruhen.

## 2. Checkliste vor der Veröffentlichung

| Kategorie | Anforderung | Beurteilungsgrundlage |
| --- | --- | --- |
| Startseite | README besteht die Vier-Fragen-Prüfung (was / wozu / Funktionen / Beispiel) | [README-Abschnitts-Spezifikation](./readme-sections-specification.md) |
| Einzeiler | Kategorie und einschränkende Merkmale klar benannt, eigenständig wiedergebbar | ebd., Abschnitt 1.1 |
| Beispiel | Hello World, in höchstens zwei Schritten ausführbar | [README-Standardvorlage](./readme-standard-template.md) |
| Dokumentation | Installation, Konfiguration und API-Dokumentation vollständig | [Dokumentationsmatrix](./document-matrix.md) |
| Lizenz | LICENSE vorhanden und mit der Angabe in der README identisch | [LICENSE-Spezifikation](./license-specification.md) |
| Compliance | NOTICE deckt Abhängigkeiten Dritter ab | [NOTICE-Spezifikation](./notice-specification.md) |
| Community-Einstieg | Issue-Vorlagen, Contributing Guide und Verhaltenskodex vorhanden | [Contributing-Guide-Spezifikation](./contribution-guide-specification.md) |
| Reaktionsmechanismus | Zuständige Personen und Fristen für Problemmeldungen klar benannt | [Incident-Reaktionsspezifikation](./incident-response-specification.md) |

Promotion vor Abschluss dieser Checkliste ist eine nach dieser Spezifikation verbotene Handlung.

## 3. Kategorien der Kanäle

### 3.1 Internationale technische Communities

| Kanal | Geeignete Inhalte | Hinweise |
| --- | --- | --- |
| Hacker News | Technische Umsetzung, tiefgehendes Engineering-Design | Titel sachlich halten, Marketingformulierungen vermeiden |
| Passende Reddit-Subreddits | Bibliotheken, Werkzeuge, Frameworks | Selbstpromotionsregeln des jeweiligen Subreddits beachten |
| Lobsters | Systemprogrammierung, Engineering-Praktiken | Community reagiert empfindlich auf Marketing |
| Technische Newsletter (JavaScript Weekly u. a.) | Bibliotheken und Werkzeuge | Prägnante Projektzusammenfassung bereitstellen |
| Offizieller Blog und Dokumentationsseite | Ausführliche Vorstellung und Versionshinweise | Als Zielseite für andere Kanäle |

### 3.2 Chinesische technische Communities

| Kanal | Geeignete Inhalte |
| --- | --- |
| Juejin | Frontend, Mobile, Engineering-Praktiken |
| Developer Headlines | Allgemeine technische Projekte |
| V2EX | Werkzeuge, Produktivitätssoftware, Startups |
| Zhihu | Technische Einordnung und Design-Abwägungen |
| WeChat Official Account | Ausführliche Langbeiträge, Tutorial-Reihen |
| Geek Headlines | Allgemeine Techniknachrichten |

### 3.3 Projekteigene Kanäle

1. Community-Einstiege in der Projekt-README (Discussions, Discord);
2. Projekt eigene Social-Media-Konten für Versionsmeldungen und Veranstaltungen;
3. Dokumentations- und Demoseite als Zielseiten für externen Traffic.

## 4. Veröffentlichungsrhythmus

1. **Warm-up-Phase**: Checkliste aus Abschnitt 2 abschließen; Materialien wie Einzeiler, Screenshots und Demo-GIF vorbereiten.
2. **Startphase**: Auf den 1–2 am besten passenden Kanälen veröffentlichen; dasselbe Material nicht über viele Plattformen streuen.
3. **Reaktionsphase**: 72 Stunden nach dem Start mit hoher Frequenz reagieren und Issues sowie Feedback bearbeiten.
4. **Iterationsphase**: Mit dem Versionsrhythmus kontinuierlich aktualisieren; jeder Veröffentlichung Versionshinweise beifügen.
5. **Konsolidierungsphase**: Häufige Fragen zu einer FAQ zusammenfassen und in die Dokumentation zurückspielen.

## 5. Anforderungen an die Materialien der Startseite

| Material | Spezifikation | Zweck |
| --- | --- | --- |
| Einzeiler | Chinesisch max. 60 Zeichen / Englisch max. 25 Wörter; die Repository-Description verwendet das zweisprachig zusammengeführte Format „Landessprache \| Englisch“, siehe [Projektbenennungs-Spezifikation](./project-naming-specification.md) Abschnitt 5 | Repository-Description, Social-Zusammenfassung |
| Screenshots | Je eine Fassung für helles und dunkles Theme, Breite begrenzt | Erster Bildschirm der README |
| Demo-GIF | Komprimiert mit begrenzter Größe, zeigt den Kernablauf | Demo-Abschnitt der README |
| Logo | SVG-Format, mit heller und dunkler Fassung | Erster Bildschirm und Social Cards |
| Funktionsvergleichstabelle | Auf überprüfbaren Fakten beruhend, mit ungeeigneten Anwendungsfällen | README oder Dokumentationsseite |

Die Materialien sind mit den Versionen synchron zu aktualisieren, damit keine veralteten Oberflächen gezeigt werden.

## 6. Community-Betreuung

1. Erstbeitragenden einen klaren Einstieg bieten, etwa das Label `good first issue`.
2. Reaktionen auf Probleme sind zu protokollieren, damit gleiche Fragen nicht wiederholt auftreten.
3. Der Verhaltenskodex gilt für alle Community-Kanäle, siehe [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md).
4. Danksagungen an Beitragende gebündelt platzieren und nicht über den Text verstreuen.
5. Falsche Aufmerksamkeit durch Anreize für Stars oder gegenseitige Likes ist unzulässig.

## 7. Verbotene Praktiken

1. Promotion vor Abschluss der Qualitätscheckliste ist unzulässig.
2. Das Erfinden oder Übertreiben von Projektdaten und Anwendungsfällen ist unzulässig.
3. Das wiederholte Streuen desselben Inhalts über mehrere Kanäle ist unzulässig.
4. Das Herabsetzen vergleichbarer Projekte zur eigenen Imagepflege ist unzulässig.
5. Die Verwendung von Anreizen zur Erlangung von Stars ist unzulässig.

## Verwandte Dateien

- Vier-Fragen-Prüfung und Einzeiler siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md)
- Spezifikationen für visuelle Materialien siehe [README-Visual-Layout-Spezifikation](./readme-visual-layout-specification.md)
- Regeln für Community-Einstiege siehe [Contributing-Guide-Spezifikation](./contribution-guide-specification.md)
- Reaktionsmechanismus für Probleme siehe [Incident-Reaktionsspezifikation](./incident-response-specification.md)
- Versionshinweise siehe [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md)
- Recherchequelle siehe [README-Vorlagen-Recherchebericht](./readme-template-research-report.md)
