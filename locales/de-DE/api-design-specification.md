# API-Design-Spezifikation

> Problem, das diese Datei löst: Sie definiert Konsistenzprinzipien und Vereinbarungen für das Schnittstellendesign, damit APIs benutzbar, vorhersagbar und evolvierbar bleiben.

## 1. Designprinzipien

1. Konsistente Benennung: Gleichartige Ressourcen und Operationen verwenden einheitliche Benennungsregeln.
2. Vorhersagbarkeit: Operationen mit gleicher Semantik besitzen dieselbe Struktur.
3. Explizit vor implizit: Standardwerte, Pflichtfelder und Fehlerverhalten müssen eindeutig sein.
4. Abwärtskompatibilität: Änderungen bleiben vorrangig kompatibel; destruktive Änderungen müssen versioniert werden (siehe [Versionsverwaltungs-Spezifikation](./version-management-specification.md)).

## 2. Zwingend enthaltene Vereinbarungen

1. **Benennung**: Regeln für die Benennung von Ressourcen, Methoden und Feldern.
2. **Parameter**: Typ, Pflichtangabe, Standardwert, Wertebereich.
3. **Fehler**: Einheitliche Fehlerstruktur, Fehlercodes, HTTP-Status oder gleichwertige Mechanismen.
4. **Paginierung und Filterung**: Vereinbarungen zu Paginierung, Sortierung und Filterung bei großen Datenmengen.
5. **Idempotenz**: Idempotenzgarantie für schreibende Operationen.
6. **Ratenbegrenzung und Kontingente**: Frequenzbegrenzungen und Antwort bei Überschreitung.
7. **Version**: Versionierungsstrategie und Evolutionsweg der API.

## 3. Verbindliche Regeln

1. Fehlerantworten müssen einen lokalisierbaren Fehlercode und eine Erläuterung enthalten und dürfen keine internen Implementierungsdetails preisgeben.
2. Destruktive Änderungen erfordern eine Versionserhöhung und eine Migrationsphase (siehe [Änderungsprotokoll-Spezifikation](./changelog-specification.md)).
3. Schnittstellen benötigen eine zugehörige Dokumentation mit vollständigen Feldern (siehe [API-Dokumentations-Spezifikation](./api-documentation-specification.md)).

## Verwandte Dateien

- Schreibweise der API-Referenzdokumentation: [API-Dokumentations-Spezifikation](./api-documentation-specification.md)
- Sicherheitsbezogene Aspekte: [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)
- Fehlerbehandlung als Engineering-Abwägung: [Leitfaden zu Features und Engineering-Abwägungen](./features-and-engineering-tradeoffs-guide.md)
