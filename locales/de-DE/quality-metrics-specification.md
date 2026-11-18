# Spezifikation der Qualitätskennzahlen

> Problem, das diese Datei löst: Sie definiert nachverfolgbare Qualitätskennzahlen und deren Messgrundlagen, damit die Projektqualität nicht anhand belegloser Zahlen bewertet wird.

## 1. Prinzipien der Kennzahlen

1. Kennzahlen müssen messbar und reproduzierbar sein; Erhebungsmethode und statistische Grundlage sind anzugeben.
2. Kennzahlen dienen der Verbesserung, nicht einem einfachen Ranking oder dem Erzeugen von Druck.
3. Jede Kennzahl ist mit Zielwert und aktuellem Wert zu versehen und regelmäßig zu überprüfen.

## 2. Empfohlene Kennzahlen

| Kategorie | Kennzahl | Erläuterung der Messgrundlage |
| --- | --- | --- |
| Tests | Testabdeckung | Anteil der abgedeckten Codezeilen, mit Angabe des Messwerkzeugs |
| Tests | Testbestehensrate | Bestandene Testfälle / Gesamtzahl der Testfälle |
| Build | Build-Erfolgsrate | Erfolgreiche Builds / Gesamtzahl der Builds |
| Defekte | Defektdichte | Anzahl der in einem Codeumfang gefundenen Defekte |
| Defekte | Durchschnittliche Behebungsdauer | Durchschnittliche Zeit von Entdeckung bis abgeschlossener Behebung |
| Performance | Antwortzeit | Eindeutiges Szenario und Perzentil (etwa P95) |
| Abhängigkeiten | Anzahl hochriskierter Schwachstellen | Anzahl nicht behobener hochriskierter Schwachstellen in Abhängigkeiten |

## 3. Verbindliche Regeln

1. Performance-Kennzahlen müssen Testumgebung und Methode angeben; Zahlen ohne Bedingungen sind verboten (entsprechend der [Allgemeinen Schreib-Spezifikation](./general-writing-specification.md)).
2. Die Erhebung der Kennzahldaten muss automatisiert erfolgen, um Verzerrungen durch manuelle Zählung zu reduzieren.
3. Bei auffälligen Kennzahlen muss eine Nachverfolgung dokumentiert und in die [Roadmap-Spezifikation](./roadmap-specification.md) oder die Problemverfolgung aufgenommen werden.

## Verwandte Dateien

- Qualitätstor siehe [Qualitätstor](./quality-gate.md)
- Testanforderungen siehe [Test-Spezifikation](./testing-specification.md)
- Schreibweise des Performance-Kapitels siehe [README-Abschnitts-Spezifikation](./readme-sections-specification.md)
