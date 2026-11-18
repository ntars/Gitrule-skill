# Projektnamens-Spezifikation

> Problem, das diese Datei löst: Definiert die harten Regeln zu Zeichen, Groß-/Kleinschreibung, Worttrennung, Länge und Semantik des Repository-Namens sowie Namensformel, konventionelle Suffixe, Rechercheablauf und begleitende Metadatenanforderungen.

## 1. Harte Regeln

| Regel | Anforderung | Gegenbeispiel |
|---|---|---|
| Zeichensatz | Nur `a-z`, `0-9`, `-` | `My_Proj`, `我的项目` |
| Groß-/Kleinschreibung | Durchgehend Kleinbuchstaben | `MyProject` |
| Worttrennung | kebab-case, verbunden mit `-` | `myproject`, `my_project` |
| Länge | 2–25 Zeichen | überlange zusammengesetzte Namen |
| Endung | Substantiv oder morphologisches Suffix | Endung auf `-project`, `-test` |
| Version | Keine Versionsnummer, kein Jahr, kein Datum | `tool-v2`, `app2024` |
| Informationsfreie Wörter | `my`/`demo`/`test`/`new`/`tmp` verboten | `my-new-demo` |
| Eindeutigkeit | Je eine Recherche auf GitHub / npm / PyPI | Namensgleichheit mit bekannter Bibliothek |
| Semantik | Der Name allein lässt „was er tut“ erkennen | `xyz`, `abc123` |

## 2. Namensformel (eines von vier)

```text
<技术>-<对象>          vue-virtual-table      go-ratelimit
<对象>-<形态>          note-cli   image-api   config-loader
<动词>-<对象>          parse-markdown   sync-dotfiles
<领域>-<子领域>        web-ui-kit   data-pipeline
```

## 3. Konventionelle Suffixe

`-cli` Kommandozeile / `-sdk` Client-Bibliothek / `-api` `-server` Serverseite / `-template` `-boilerplate` Gerüst / `-loader` `-parser` Middleware / `-kit` Komponentensammlung / `-notes` `-guide` Dokumentation / `dotfiles` Konfigurations-Repository / `awesome-xxx` Ressourcensammlung.

## 4. Namensablauf

1. In einem Satz festhalten, „wem das Projekt welches Problem löst“.
2. Aus diesem Satz das Kernsubstantiv + die Form entnehmen und eine der Formeln aus Abschnitt 2 anwenden.
3. Drei Kandidaten erzeugen und für jeden eine Recherche auf Namensgleichheit durchführen.
4. Denjenigen wählen, der ohne Blick in die README am besten verständlich ist.
5. Der chinesische Name gehört nicht in den Repository-Namen, sondern hinter den Titel in der ersten Zeile der README.

## 5. Begleitende Metadaten

### 5.1 Repository-Kurzbeschreibung (description)

- Gleiche Herkunft wie der Repository-Name, Satzmuster: `<was es tut> for <für wen>`.
- Zusammengeführtes zweisprachiges Format: `Landessprache | Englisch`, zuerst die Landessprachfassung, dann ein halbbreiter senkrechter Strich (beidseitig je ein Leerzeichen), dann die englische Fassung. Beispiel für ein chinesisches Projekt:

```text
轻量级 Go 命令行 JSON 处理工具 | A lightweight Go CLI for JSON processing
```

- Länge: Landessprachfassung und englische Fassung je höchstens 120 Zeichen, zusammen höchstens 350 Zeichen (GitHub-Obergrenze).
- Vorgehen bei Überschreitung der zweisprachigen Gesamtlänge: vorrangig die englische Fassung kürzen statt die Landessprachfassung – die Informationsdichte des Chinesischen ist höher, Kürzen des Chinesischen kostet mehr Information; beim Kürzen zuerst Attributwörter und redundante Bestimmungen streichen, dann synonyme Formulierungen zusammenführen und schließlich die vollständige Subjekt-Prädikat-Struktur beider Sprachfassungen erhalten.
- Ohne Zeilenumbruch, ohne Markdown-Syntax und ohne Emoji; der Stil des Schlusszeichens ist in beiden Sprachen gleich (einheitlich mit oder einheitlich ohne Punkt).

### 5.2 Themen (topics)

- Alle 20 ausfüllen (GitHub-Obergrenze), vollständige Abdeckung, keine Leerstellen.
- Durchgehend Englisch, Chinesisch oder andere Sprachen sind unzulässig; durchgehend Kleinbuchstaben, verbunden mit `-`, ohne Leerzeichen und Sonderzeichen.
- Die fünf Kategorien Sprache, Domäne, Form, Ökosystem und Szenario vollständig abdecken; zusätzlich können allgemeine Begriffe wie documentation, open-source ergänzt werden.
- Bereits bei der Erstellung des Repositorys setzen, nicht leer lassen; nach Umbenennung oder Neupositionierung des Repositorys einmal erneut prüfen.

## Verwandte Dateien

- Namenskonformität gehört zur harten Regel H1, siehe [Harte Regeln](./hard-rules.md)
- Metadaten-Review gehört zur Dimension D10, siehe [Review-Dimensionsmatrix](./review-dimension-matrix.md)
- Trägerdokument ist `docs/naming.md`, siehe [Dokumentmatrix](./document-matrix.md)
