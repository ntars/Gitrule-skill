# Badge-Spezifikation

> Problem, das diese Datei löst: Sie definiert URL-Syntax, Stilparameter, Farbkodierung, Informationsauswahl, Anordnungsreihenfolge und Mengenbegrenzung von Badges in der README, mit Shields.io als Hauptumsetzung, und stellt direkt kopierbare Formatbeispiele sowie empfohlene Parameterkonfigurationen bereit.

Alle in diesem Dokument genannten Parameter wurden anhand der offiziellen Shields.io-Dokumentation (Seiten Static Badge und Logos, Formatspezifikation von badge-maker) geprüft; die Häufigkeitsdaten stammen aus der Stichprobenerhebung dieses Projekts zu READMEs führender Open-Source-Projekte und sind als „gemessen“ gekennzeichnet.

## 1. Grundsyntax

### 1.1 URL-Struktur statischer Badges

Statische Badges übergeben Parameter über den URL-Pfad; die Standardstruktur lautet:

```text
https://img.shields.io/badge/<标签>-<消息>-<颜色>?style=<样式>&<其他查询参数>
```

Die drei Pfadsegmente werden durch Bindestriche `-` getrennt:

| Segment | Bezeichnung | Erforderlich | Erläuterung |
| --- | --- | --- | --- |
| Segment 1 | Label (label) | Nein | Linker Text, benennt die Kennzahl |
| Segment 2 | Nachricht (message) | Ja | Rechter Text, zeigt den Kennzahlwert |
| Segment 3 | Farbe (color) | Ja | Hintergrundfarbe rechts |

Die zweiteilige Schreibweise (Label entfällt, nur Nachricht und Farbe) ist ebenfalls zulässig:

```text
https://img.shields.io/badge/<消息>-<颜色>
```

### 1.2 Regeln zur Zeichenmaskierung

Leerzeichen und Sonderzeichen im URL-Pfad müssen maskiert werden; die Regeln lauten:

| Eingabezeichen | URL-Schreibweise | Beispiel |
| --- | --- | --- |
| Leerzeichen | `_` oder `%20` | `v0.1 prototype` → `v0.1%20prototype` |
| Unterstrich `_` | `__` (doppelter Unterstrich) | `my_label` → `my__label` |
| Bindestrich `-` | `--` (doppelter Bindestrich) | `dev-build` → `dev--build` |

Das vom Nutzer bereitgestellte Prototypbeispiel entspricht dieser Syntax und kann direkt verwendet werden:

```markdown
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
```

Seine Bedeutung: Label `status`, Nachricht `v0.1 prototype` (Leerzeichen als `%20`), Farbe `8957e5` (hexadezimales Violett), Stil `flat-square`.

### 1.3 Markdown-Einbettungsformat

```markdown
![Version](https://img.shields.io/badge/version-1.2.0-blue?style=flat-square)
```

Soll das Badge anklickbar sein, wird das Bild mit einem Link umschlossen:

```markdown
[![Lizenz](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
```

## 2. Stilparameter (style)

`style` bestimmt das gesamte visuelle Design des Badges, kennt fünf Werte; der Standardwert ist `flat`.

| Wert | Visuelle Merkmale | Geeignete Szenarien | Gemessene Häufigkeit (N=120) |
| --- | --- | --- | --- |
| `flat` | Rechteckig, flach, Shields.io-Standard | Universell bevorzugt, mit den meisten Designs kompatibel | 32 |
| `flat-square` | Rechteckig, ohne abgerundete Ecken, etwas kompakter | Startbildschirme mit dem Wunsch nach klarer, strenger Wirkung | 60 |
| `for-the-badge` | Groß und fett, kontrastreich | Hauptvisualisierung oben, betonende Badges | 65 |
| `social` | Abgerundet, links und rechts farblich getrennt, flach | Startbildschirme im Social-Stil | 12 |
| `plastic` | Glanzverlauf, skeuomorph | Retro-Stil, heute kaum noch verwendet | 1 |

**Empfohlene Konfiguration**:

- Innerhalb derselben README müssen alle Badges einheitlich `style` verwenden; Mischungen sind unzulässig. Dies ist die wichtigste Anforderung an die visuelle Konsistenz.
- Für universelle Projekte sind `flat` oder `flat-square` zu bevorzugen; soll der Marken-Startbildschirm betont werden, wird einheitlich `for-the-badge` verwendet.
- Gemessen sind `for-the-badge` (65 Mal) und `flat-square` (60 Mal) am verbreitetsten; beide eignen sich als Standardwahl.

Formatbeispiel:

```markdown
![build](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)
![build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)
```

## 3. Farbparameter (color / labelColor)

### 3.1 Drei Farbnotationen

Nach der badge-maker-Dokumentation unterstützen `color` (rechts) und `labelColor` (Hintergrund links) die folgenden drei Schreibweisen:

**Methode 1: Shields.io-Namensfarben**

| Semantik | Namensfarben |
| --- | --- |
| Erfolg | `brightgreen`、`green`、`success` |
| Hinweis | `yellow`、`yellowgreen`、`orange`、`important` |
| Warnung | `red`、`critical` |
| Information | `blue`、`informational` |
| Neutral | `grey` / `gray`、`lightgrey` / `lightgray`、`inactive` |

Hinweis: Der Standardwert von `labelColor` ist `grey`, der von `color` ist `lightgrey` (die Dokumentation merkt zusätzlich an, dass auch `inactive` zu den Standardfarben zählt); einzelne Namensfarben weichen leicht von den gleichnamigen CSS-Farben ab, maßgeblich ist das Renderingergebnis von Shields.io.

**Methode 2: Hexadezimalfarben**

Unterstützt werden drei- oder sechsstellige Hexadezimalwerte, mit oder ohne Präfix `#`:

```text
?color=8957e5
?color=007fff
?color=%23007fff    ← 保留 # 时需编码为 %23
```

**Methode 3: CSS-Farbwerte**

Unterstützt werden `rgb(...)`, `rgba(...)`, `hsl(...)`, `hsla(...)` sowie CSS-Namensfarben (etwa `aqua`, `fuchsia`, `lightslategray`); bei der Verwendung ist eine URL-Kodierung erforderlich.

### 3.2 Semantische Farbzuordnung (empfohlene Konfiguration)

| Informationsart | Empfohlene Farbe | Beispielnachricht |
| --- | --- | --- |
| Build bestanden, Tests bestanden | `brightgreen` / `success` | `passing` |
| Build fehlgeschlagen | `red` / `critical` | `failing` |
| Stabile Version | `blue` | `v1.2.0` |
| Vorabversion, Prototyp | Eigenes Violett `8957e5` / `orange` | `v0.1 prototype` |
| Lizenz | `blue` / `green` | `MIT` |
| Dokumentationsstatus | `yellowgreen` | `docs` |
| Veraltet, Wartung eingestellt | `red` / `inactive` | `deprecated` |

**Empfohlene Konfiguration**: Markenfarbe und Statusfarben werden je Projekt fest vereinbart und dürfen nicht beliebig gewechselt werden; dieselbe Semantik verwendet im gesamten Repository dieselbe Farbkodierung.

Formatbeispiel:

```markdown
![Abdeckung](https://img.shields.io/badge/coverage-95%25-orange?style=flat-square)
![Status](https://img.shields.io/badge/status-v0.1%20prototype-8957e5?style=flat-square)
![Lizenz](https://img.shields.io/badge/license-MIT-blue?style=flat-square)
```

## 4. Symbolparameter (logo / logoColor / logoSize)

### 4.1 Verwendung von Simple Icons

Der Parameter `logo` übernimmt den Icon-Slug von Simple Icons im Format `?logo=<slug>`. Häufige Slugs sind:

| Verwendungszweck | Slug | Gemessene Häufigkeit (N=120) |
| --- | --- | --- |
| GitHub-Repository | `github` | 35 |
| Discord-Community | `discord` | 20 |
| npm-Paket | `npm` | 4 |
| Apple-Plattform | `apple` | 3 |
| Docker | `docker` | 3 |
| Social-Plattform X | `x` | 3 |
| Python-Paket | `pypi` | 2 |

Maßgeblich für vollständige Slugs sind die Simple-Icons-Website oder die Datei `slugs.md` im Repository simple-icons.

### 4.2 Symbolfarbe und -größe

- `logoColor`: legt die Farbe des Simple-Icons-Symbols fest; unterstützt Hexadezimal, rgb, hsl und CSS-Namensfarben; wirkt nur bei Simple-Icons-Symbolen, nicht bei eigenen Symbolen.
- `logoSize`: Bei `auto` skaliert das Symbol inhaltsabhängig, geeignet für breitere Symbole; wirkt ebenfalls nur bei Simple Icons.

Formatbeispiel:

```markdown
![repo](https://img.shields.io/badge/github-repo-blue?logo=github)
![logo-Kolorierung](https://img.shields.io/badge/logo-javascript-blue?logo=javascript&logoColor=f5f5f5)
```

Eigene Symbole können über `logo=data:image/svg+xml;base64,...` übergeben werden; die URL wird jedoch sehr lang und ist schwer zu pflegen, daher außer bei besonderem Bedarf nicht empfohlen.

## 5. Weitere Abfrageparameter

| Parameter | Wirkung | Beispiel |
| --- | --- | --- |
| `label` | Überschreibt den Standardtext links (Leerzeichen müssen kodiert werden) | `?label=healthiness` |
| `labelColor` | Hintergrundfarbe links | `?labelColor=abcdef` |
| `color` | Hintergrundfarbe rechts | `?color=fedcba` |
| `cacheSeconds` | HTTP-Cache-Dauer (Sekunden); Werte unter dem Standardwert werden ignoriert | `?cacheSeconds=3600` |
| `link` | Legt getrennte Sprungziele für linke und rechte Hälfte fest | Wirkt nur im Tag `<object>`, bei Markdown-Bildern unwirksam |

## 6. Dynamische Badges

Dynamische Badges beziehen Daten in Echtzeit über einen externen Dienst von Shields.io; die Werte müssen nicht manuell aktualisiert werden. Häufige Typen:

| Kategorie | URL-Muster | Zweck |
| --- | --- | --- |
| Build-Status | `https://img.shields.io/github/actions/workflow/status/<owner>/<repo>/<workflow>` | CI-Status |
| Version | `https://img.shields.io/npm/v/<package>` | Neueste npm-Version |
| Lizenz | `https://img.shields.io/npm/l/<package>` | Paketlizenz |
| Sternanzahl | `https://img.shields.io/github/stars/<owner>/<repo>` | Beliebtheit |
| Issue-Anzahl | `https://img.shields.io/github/issues/<owner>/<repo>` | Offene Probleme |
| Downloadzahl | `https://img.shields.io/npm/dt/<package>` | Kumulierte Downloads |

Dynamischen Badges können Parameter wie `?style=` und `?logo=` angehängt werden; die Regeln entsprechen denen statischer Badges. Referenzprojekte kombinieren üblicherweise „dynamische Badges für echte Kennzahlen + statische Badges für eigene Statusangaben“.

## 7. Informationsauswahl und Anordnungsreihenfolge

### 7.1 Informationsauswahl

Badges sollen „überprüfbare, für Lesende nützliche“ Statusinformationen vermitteln. Empfohlen wird die Beschränkung auf folgende Kategorien:

1. Build- und Teststatus;
2. Version oder letzte Veröffentlichung;
3. Lizenz;
4. Dokumentationsstatus;
5. Community-Kanäle (Discord, Diskussionsbereich);
6. projektspezifische Statusangaben (Prototyp, in Wartung, veraltet).

Unzulässig sind: Downloadzahlen ohne Quelle, projektfremde Marketinglabels, nicht überprüfbare Bewertungen und rein dekorative Farbflächen.

### 7.2 Anordnungsreihenfolge

Empfohlen wird die Reihenfolge „Status → Version → Lizenz → Plattform/Community → eigener Status“, wobei die Wichtigkeit von links nach rechts abnimmt. Begründung: Der Build-Status entscheidet über die Adoption, die Version über die Kompatibilitätsbeurteilung und die Lizenz über die Nutzbarkeit; beides sind entscheidungsrelevante Vorabinformationen.

### 7.3 Mengenbegrenzung

- Übliche Projekte: 4–6 Badges.
- Ressourcensammlungen oder Ökosystemprojekte: bis zu 8–10 Badges.
- Alle Badges stehen nach Projektname und Ein-Satz-Positionierung sowie vor dem Haupttext, in einer eigenen Zeile oder einem zentrierten Container; sie dürfen nicht im Haupttext verstreut werden.

### 7.4 Statisches Lieferstatus-Badge

Die Standardumsetzung von Punkt 6 in Abschnitt 7.1, „projektspezifische Statusangaben“, ist das statische Lieferstatus-Badge; der Wert wird von den Projektverantwortlichen manuell aktualisiert und eignet sich für Lieferfortschritt und Wartungsstatus ohne externe Datenquelle:

```text
![Status](https://img.shields.io/badge/status-4%20of%204%20delivered-brightgreen?style=flat-square)
```

1. Die Standardstruktur lautet `badge/<标签>-<消息>-<颜色>`, der Stil ist einheitlich `?style=flat-square`; das Beispiel bedeutet „alle 4 Lieferobjekte geliefert“.
2. Leerzeichen im Nachrichtentext werden als `%20`, Bindestriche als `--` und Unterstriche als `__` geschrieben; Zeilenumbrüche und andere nicht maskierte Sonderzeichen sind unzulässig.
3. Farbkonvention: `brightgreen` bedeutet abgeschlossen, `yellow` in Arbeit, `red` blockiert, `lightgrey` nicht begonnen.
4. Bei Wertänderungen müssen Badge und Haupttext synchron aktualisiert werden; das Badge darf nicht dauerhaft hinter dem tatsächlichen Status zurückbleiben. Ist die Synchronität nicht gewährleistet, ist ein dynamisches Badge zu verwenden.
5. Der `alt`-Text nennt die tatsächliche Bedeutung, etwa `![Lieferstatus]`; eine Verlinkung auf die Lieferobjektliste oder den zugehörigen Indexabschnitt ist möglich.

## 8. Barrierefreiheit und Farbschema-Anpassung

- Der `alt`-Text jedes Badges muss die tatsächliche Bedeutung nennen, beispielsweise `![Build-Status]` statt `![badge]`.
- Bei dunklem und hellem Farbschema kann die Bildquelle des Badges über `<picture>` gewechselt werden; mit `for-the-badge` und `labelColor=000` bleibt der Kontrast in beiden Schemata stabil.
- Badges müssen anklickbar zum jeweiligen Datenursprung führen (Build-Status zur CI, Version zur Paketverwaltungsseite, Lizenz zur LICENSE-Datei).

## Verwandte Dateien

- Abschnittszuordnung und Reihenfolge siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Visuelle Hierarchie und Platzierung siehe [README-Spezifikation für visuelles Layout](./readme-visual-layout-specification.md)
- Differenzierte Badge-Empfehlungen je Projekttyp siehe [README-Leitfaden zur Kategorieanpassung](./readme-category-adaptation-guide.md)
- Direkt übernehmbare vollständige Badge-Zeile siehe [README-Standardvorlage](./readme-standard-template.md)
- Erhebungsmethodik und Messstichproben siehe [README-Vorlagen-Recherchebericht](./readme-template-research-report.md)
