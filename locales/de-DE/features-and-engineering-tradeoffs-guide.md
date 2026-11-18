# Schreibweise für Funktionen und technische Abwägungen

> Problem, das diese Datei löst: Definiert die Schreibweise der beiden README-Kapitel „Kernfunktionen“ und „Designdetails und technische Abwägungen“ und gibt jeweils die fünfteilige Struktur der Funktionen sowie die zehn zwingend abzudeckenden Kategorien technischer Abwägungen vor.

## 1. Schreibweise der Kernfunktionen

Jede Funktion wird in der folgenden fünfteiligen Struktur beschrieben; fehlt ein Teil, darf sie nicht als Funktion aufgeführt werden.

1. **Funktionsname**: höchstens 15 Zeichen, nominale Formulierung verwenden.
2. **Nutzen**: das konkret gelöste Problem sowie die Folgen, wenn es nicht gelöst wird.
3. **Umsetzung**: eingesetzte Technik, Mechanismus oder Algorithmus, unter Angabe der maßgeblichen Datei oder Funktion.
4. **Abgrenzung**: Vergleichsdimension gegenüber gängigen Lösungen; muss eine objektiv beurteilbare Dimension sein.
5. **Belege**: Testdaten, Benchmark-Ergebnisse, Codestelle, Konfigurationsoption oder reproduzierbare Schritte.

Einschränkungen:
1. Belege müssen reproduzierbar sein; Funktionen ohne mögliche Belege sind mit „【ausstehend: Nachweisverfahren】“ zu kennzeichnen; qualitative Beschreibungen sind kein Ersatz.
2. Leistungsbezogene Belege müssen Testumgebung und Testverfahren angeben.
3. Vergleichsobjekte müssen namentlich benannte Lösungen sein; unscharfe Verweise wie „herkömmliche Lösungen“ oder „andere Werkzeuge“ sind unzulässig.

## 2. Schreibweise von Designdetails und technischen Abwägungen

Jeder Punkt wird in der dreiteiligen Struktur „Szenario → Vorgehen → Grund“ beschrieben und erläutert, warum so und nicht anders entworfen wurde.

Zwingend abzudeckende Kategorien:
1. Anomale Eingaben und Randfälle (Nullwerte, Überlänge, unzulässige Zeichen, Extremwerte)
2. Timeout-, Wiederholungs-, Backoff-, Circuit-Breaker- und Degradationsstrategien
3. Cache-Ebenen, Invalidierungsstrategien, Schutz gegen Cache-Penetration und Cache-Avalanche
4. Nebenläufigkeitskontrolle, Sperrgranularität, Datenkonsistenz und Idempotenz
5. Speicher- und Ablageoptimierung (Stapelverarbeitung, Streaming-Lesen und -Schreiben, Komprimierung)
6. Sicherheitsmaßnahmen (Authentifizierung, Ratenbegrenzung, Eingabevalidierung, Maskierung sensibler Daten)
7. Interaktionsdetails (Schutz vor Fehlbedienung, doppelte Bestätigung, Rückgängigmachbarkeit, Lade- und Leerzustand)
8. Begründung der Standardparameterwerte
9. Strategien für Rückwärtskompatibilität und plattformübergreifende Anpassung
10. Umgang mit schwachem Netz und Offline-Betrieb, Zustandswiederherstellung

## Verwandte Dateien

- Entspricht Kapitel 4 und 5 der README, siehe [README-Abschnittsspezifikation](./readme-sections-specification.md)
- Die Schreibweise von Leistungsdaten muss die Genauigkeitsanforderungen einhalten, siehe [Allgemeine Schreibspezifikation](./general-writing-specification.md)
- Funktionsbelege und Abdeckung der Abwägungen gehören zu den Qualitätstoren G4/G5, siehe [Qualitätstor](./quality-gate.md)
