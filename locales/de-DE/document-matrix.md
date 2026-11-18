# Dokumentationsmatrix

> Problem, das diese Datei löst: Definiert für jedes Lieferdokument die alleinige Verantwortlichkeit, die strikt unzulässigen Inhalte und die Aufteilungsvorgaben, um eine Verantwortlichkeit pro Datei sicherzustellen und Zusammenlegungen auszuschließen.

## 1. Dateien und Verantwortlichkeiten

| Datei | Alleinige Verantwortlichkeit | Strikt unzulässig |
|---|---|---|
| `README.md` | Startseite: was das Projekt ist, wie installiert wird, wie es läuft, wo Details nachzulesen sind | vollständige API, Beitragsablauf, Änderungsprotokoll |
| `LICENSE` | Volltext der Lizenz | jeglicher Erläuterungstext |
| `CHANGELOG.md` | nutzerseitige Versionsänderungen | interne Refactoring-Details, Entwicklungsplan |
| `CONTRIBUTING.md` | Ablauf und Vorgaben für externe Beitragende | Funktionsbeschreibung des Projekts |
| `CODE_OF_CONDUCT.md` | Verhaltenskodex | technische Inhalte |
| `SECURITY.md` | Kanal zur Meldung von Schwachstellen und Reaktionsstrategie | Liste bekannter Schwachstellen |
| `docs/api.md` | vollständige API-Referenz | Tutorials |
| `docs/architecture.md` | Architektur und Modulgrenzen | Anwendungsbeispiele |
| `docs/naming.md` | Benennungsspezifikation | andere Spezifikationen |
| `docs/release.md` | Veröffentlichungsablauf und Versionsstrategie | Änderungsaufzeichnungen |
| `.github/PULL_REQUEST_TEMPLATE.md` | Selbstprüfungsliste für PRs | Projektvorstellung |
| `.github/ISSUE_TEMPLATE/*.yml` | strukturierte Issue-Formulare | Freitext |
| `.github/workflows/*.yml` | CI/CD | Erläuterungsdokumentation |

> Hinweis: Der Spezifikationstext zu `docs/naming.md` steht in der [Projektbenennungsspezifikation](./project-naming-specification.md); der Spezifikationstext zu `docs/release.md` steht in der [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md).

## 2. Vorgaben

- Eine Einzeldatei mit mehr als 300 Zeilen muss nach `docs/` aufgeteilt werden; die README enthält nur eine Zusammenfassung + Links.
- Dateinamen werden fest in Großbuchstaben geschrieben, Pfade sind fest, eigene Verzeichnishierarchien sind unzulässig.
- Jedes Dokument beginnt mit einem Satz, der „Problem, das diese Datei löst“ angibt, und endet mit Querverweisen auf verwandte Dateien.

## Verwandte Dateien

- Zur 20-Kapitel-Struktur der README siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Zur eigenständigen NOTICE-Spezifikation siehe [NOTICE-Spezifikation](./notice-specification.md)
- Zur eigenständigen LICENSE-Spezifikation siehe [LICENSE-Spezifikation](./license-specification.md)
- Dokumentationsvollständigkeit/-qualität gehört zu den Dimensionen D11/D12, siehe [Review-Dimensionsmatrix](./review-dimension-matrix.md)
