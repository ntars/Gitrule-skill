# Datenbankdesign-Spezifikation

> Problem, das diese Datei löst: Sie definiert Regeln für Tabellenstruktur, Felder, Indizes und Migrationen von Datenbanken, um Datenkonsistenz, Evolvierbarkeit und Nachvollziehbarkeit zu gewährleisten.

## 1. Namenskonventionen

1. Tabellen- und Feldnamen verwenden einen einheitlichen Namensstil mit eindeutiger Bedeutung.
2. Primärschlüssel, Fremdschlüssel und Indizes folgen einheitlichen Präfixregeln.
3. Für reservierte Wörter und Abkürzungen bestehen eindeutige Vereinbarungen, um Mehrdeutigkeiten zu vermeiden.

## 2. Felddesign

1. Jedes Feld muss Typ, Nullbarkeit, Standardwert und Bedeutung eindeutig angeben.
2. Zeitfelder verwenden eine einheitliche Zeitzone und Präzision.
3. Präzisionssensible Felder wie Geldbeträge verwenden Festkommatypen, keine Gleitkommatypen.
4. Statusfelder verwenden eindeutige Enumerationen mit Angabe der Bedeutung der Werte.

## 3. Indizes und Constraints

1. Indizes werden anhand der Abfrageszenarien entworfen; Überindizierung ist zu vermeiden.
2. Die Integrität wird über Constraints sichergestellt und nicht der Prüfung in der Anwendungsschicht überlassen.
3. Fremdschlüssel und Kaskadenregeln müssen explizit deklariert werden.

## 4. Migrationsverwaltung

1. Strukturänderungen werden über Migrationsskripte verwaltet; die Skripte werden versioniert und im Repository eingecheckt.
2. Migrationen müssen rückrollbar sein; bei destruktiven Änderungen ist ein Datenmigrationsplan bereitzustellen.
3. Migrationsskripte sind in der Testumgebung zu validieren und erst danach in der Produktion anzuwenden (siehe [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md)).

## 5. Sicherheit

1. Sensible Daten werden verschlüsselt oder pseudonymisiert gespeichert (siehe [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)).
2. Datenbank-Verbindungszeichenfolgen dürfen nicht im Repository eingecheckt werden (entspricht der harten Regel H3).

## Verwandte Dateien

- Rote Linien für sensible Informationen: [Sicherheits- und Datenschutz-Spezifikation](./security-and-privacy-specification.md)
- Änderungsmanagement: [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md)
- Einordnung in die Architektur: [Architekturdesign-Dokumentations-Spezifikation](./architecture-design-document-specification.md)
