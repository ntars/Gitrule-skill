# Spezifikationsauswahlleitfaden

> Problem, das diese Datei löst: Liefert auf Basis von Projekttyp, Teamgröße und Veröffentlichungsphase die Grundlage für den Zuschnitt der Spezifikationen und stellt eine minimal nutzbare Kombination sowie eine vollständig konforme Kombination bereit, damit „bedarfsgerechte Anwendung“ klare Beurteilungsmaßstäbe besitzt und nicht von individueller Einschätzung abhängt.

Gegenstand des Zuschnitts in dieser Datei ist das gesamte Spezifikationspaket; zu den typbedingten Unterschieden auf Ebene der README-Abschnitte siehe [README-Kategorieanpassungsleitfaden](./readme-category-adaptation-guide.md), zur vollständigen Zuordnung der Phasen siehe [Lebenszyklus-Zuordnungstabelle](./lifecycle-mapping-table.md).

## 1. Auswahlgrundsätze

1. **Verbindliche Vorgaben sind nicht zuschneidbar**: [Harte Regeln](./hard-rules.md) und [Verbotene Praktiken](./prohibited-practices.md) gelten in jedem Projekt und in jeder Phase vollständig.
2. **Phasen-Qualitätstore bestimmen die Untergrenze**: Vor dem Eintritt in eine Phase muss das für diese Phase in der [Lebenszyklus-Zuordnungstabelle](./lifecycle-mapping-table.md) angegebene Austritts-Qualitätstor bestanden sein; die zugehörigen Kernspezifikationen dürfen nicht entfallen.
3. **Typbedingte Unterschiede beeinflussen nur die Tiefe**: Der Projekttyp bestimmt, welche Spezifikationen betont und welche Details vereinfacht werden, und begründet keinen Verzicht auf Qualitätstore.
4. **Herabstufung ist ausdrücklich zu erklären**: Private temporäre Skript-Repositories dürfen ausschließlich die P0-Qualitätstore ausführen; dies ist jedoch in den Liefergegenständen als „herabgestufter Modus“ zu kennzeichnen und die nicht ausgeführten Punkte sind aufzulisten.

## 2. Zuschnittsdimensionen

| Dimension | Ausprägung | Wesentliche Auswirkung |
| --- | --- | --- |
| Projekttyp | Bibliothek / SDK, Anwendung, Befehlszeilenwerkzeug, Framework, Ressourcensammlung | Bestimmt die zu stärkenden Spezifikationen und die vereinfachbaren Details |
| Teamgröße | Einzelperson, kleines Team, Organisation | Bestimmt die Notwendigkeit von Governance- und Kollaborationsspezifikationen |
| Veröffentlichungsphase | Prototypenvalidierung, erste öffentliche Freigabe, stabile Wartung | Bestimmt den Zeitpunkt der Einführung von Compliance- und Betriebsspezifikationen |

Bei Überlagerung der drei Dimensionen gilt die Prioritätsreihenfolge „Verbindliche Vorgaben → Phasen-Qualitätstore → Veröffentlichungsphase → Projekttyp → Teamgröße“; ein Zuschnitt in einer Dimension niedrigerer Priorität darf die Anforderungen einer Dimension höherer Priorität nicht abschwächen.

## 3. Zuschnitt nach Projekttyp

| Projekttyp | Zu stärken | Vereinfachbar | Erforderliche Liefergegenstände |
| --- | --- | --- | --- |
| Bibliothek / SDK | [API-Designspezifikation](./api-design-specification.md), [API-Dokumentationsspezifikation](./api-documentation-specification.md), [Versionsverwaltungsspezifikation](./version-management-specification.md), [Änderungsprotokoll-Spezifikation](./changelog-specification.md) | Bereitstellung und Rollback, Observability (nur bei Verteilung von Artefakten), visuelle Spezifikationen für Screenshots | README, API-Dokumentation, LICENSE, CHANGELOG |
| Anwendung | [README-Visuallayout-Spezifikation](./readme-visual-layout-specification.md), [Barrierefreiheitsspezifikation](./accessibility-specification.md), [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md), [Observability-Spezifikation](./observability-specification.md), [Fehlerbehebungsspezifikation](./troubleshooting-specification.md) | API-Dokumentation, Datenbankdesign (bei Nutzung verwalteter Dienste) | README, Screenshots, Bereitstellungsanleitung, SECURITY |
| Befehlszeilenwerkzeug | [Commit-Nachrichten-Spezifikation](./commit-message-specification.md), [Leitfaden zu Features und Engineering-Abwägungen](./features-and-engineering-tradeoffs-guide.md), [README-Kategorieanpassungsleitfaden](./readme-category-adaptation-guide.md), [Barrierefreiheitsspezifikation](./accessibility-specification.md) (Terminalausgabe) | Datenbankdesign, Bereitstellung und Rollback (bei überwiegender Paketverteilung) | README, Anwendungsbeispiele, Demo-Animation, LICENSE |
| Framework | [Dokumentationsmatrix](./document-matrix.md), [API-Dokumentationsspezifikation](./api-documentation-specification.md), [Contributing-Guide-Spezifikation](./contribution-guide-specification.md), [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md), [Observability-Spezifikation](./observability-specification.md) | Datenbankdesign (ohne integrierte Speicherung) | README, Dokumentationseinstieg, Contributing-Guide, Verhaltenskodex |
| Ressourcensammlung | [Dokumentationsmatrix](./document-matrix.md), [Contributing-Guide-Vorlage](./contribution-guide-template.md), [Mehrsprachigkeitsspezifikation](./multilingual-specification.md), [Allgemeine Schreibspezifikation](./general-writing-specification.md) | Tests, Bereitstellung, API, Datenbank, Observability | README, Kategorienverzeichnis, Contributing-Guide, LICENSE |

Projekte des Typs Ressourcensammlung enthalten üblicherweise keinen ausführbaren Code; [Testspezifikation](./testing-specification.md) und [CI-Workflow-Spezifikation](./ci-workflow-specification.md) können als nicht anwendbar gekennzeichnet werden. [Allgemeine Schreibspezifikation](./general-writing-specification.md) und [Barrierefreiheitsspezifikation](./accessibility-specification.md) sind jedoch weiterhin einzuhalten, damit Linktexte und Listenstrukturen nutzbar bleiben.

## 4. Zuschnitt nach Teamgröße

| Teamgröße | Zusätzlich erforderliche Spezifikationen | Entfallbare Spezifikationen |
| --- | --- | --- |
| Einzelperson | [Harte Regeln](./hard-rules.md), [Projektbenennungsspezifikation](./project-naming-specification.md), [README-Standardvorlage](./readme-standard-template.md), [LICENSE-Spezifikation](./license-specification.md) | Verhaltenskodex, Code-Eigentum, Iterationsretrospektive, Qualitätsmetriken (können bis vor der ersten öffentlichen Freigabe nachgeholt werden) |
| Kleines Team | Zusätzlich zur Einzelperson [Code-Eigentumsspezifikation](./code-ownership-specification.md), [Contributing-Guide-Spezifikation](./contribution-guide-specification.md), [CI-Workflow-Spezifikation](./ci-workflow-specification.md), [Qualitätstor](./quality-gate.md) | Incident-Reaktion, Observability (können nach dem Go-live des Dienstes nachgeholt werden) |
| Organisation | Vollständig anwendbar; zusätzlich sind [NOTICE-Spezifikation](./notice-specification.md), [SECURITY-Vorlage](./security-template.md), [Haftungsausschluss](./disclaimer.md), [Incident-Reaktionsspezifikation](./incident-response-specification.md), [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md), [Spezifikation für die Anforderungs-Verfolgungsmatrix](./requirements-traceability-matrix-specification.md) umzusetzen | Keine |

Bei wachsender Teamgröße sind Governance-Spezifikationen vor der externen Sichtbarkeit des Repositorys nachzuholen und dürfen nicht erst nach der ersten Veröffentlichung ergänzt werden.

## 5. Zuschnitt nach Veröffentlichungsphase

| Veröffentlichungsphase | Einzuführen | Aufschiebbar | Erklärungspflicht |
| --- | --- | --- | --- |
| Prototypenvalidierung | [Harte Regeln](./hard-rules.md), [Projektbenennungsspezifikation](./project-naming-specification.md), [README-Standardvorlage](./readme-standard-template.md), [Allgemeine Schreibspezifikation](./general-writing-specification.md) | Qualitätstor, Observability, Incident-Reaktion, Rechtsdokumente | „Herabgestufter Modus“ ist zu kennzeichnen und aufgeschobene Punkte sind aufzulisten |
| Erste öffentliche Freigabe | Zusätzlich zum Prototyp [Qualitätstor](./quality-gate.md), [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md), [LICENSE-Spezifikation](./license-specification.md), [Haftungsausschluss-Vorlage](./disclaimer-template.md), [Contributing-Guide-Vorlage](./contribution-guide-template.md), [Verhaltenskodex-Vorlage](./code-of-conduct-template.md), [SECURITY-Vorlage](./security-template.md), [Badge-Spezifikation](./badge-specification.md) | Migrationsleitfaden, Iterationsretrospektive (können nach der ersten Versionsiteration nachgeholt werden) | P0-Qualitätstor-Punkte dürfen nicht entfallen |
| Stabile Wartung | Zusätzlich zur ersten öffentlichen Freigabe [Änderungsprotokoll-Spezifikation](./changelog-specification.md), [Versionsverwaltungsspezifikation](./version-management-specification.md), [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md), [Observability-Spezifikation](./observability-specification.md), [Incident-Reaktionsspezifikation](./incident-response-specification.md), [Fehlerbehebungsspezifikation](./troubleshooting-specification.md), [Iterationsretrospektiven-Spezifikation](./iteration-retrospective-specification.md), [Spezifikation für die Anforderungs-Verfolgungsmatrix](./requirements-traceability-matrix-specification.md) | Keine | Brechende Änderungen erfordern einen Migrationspfad und eine Ankündigung |

## 6. Kombinationsvarianten

### 6.1 Minimal nutzbare Kombination

Geeignet für persönliche Prototypen oder private Validierungs-Repositories, insgesamt 10 Dokumente:

| Zweck | Spezifikation |
| --- | --- |
| Vorgaben | [Harte Regeln](./hard-rules.md), [Verbotene Praktiken](./prohibited-practices.md) |
| Projektstart | [Projektstart- und Anforderungsspezifikation](./project-initiation-and-requirements-specification.md), [Projektbenennungsspezifikation](./project-naming-specification.md) |
| Startseite | [README-Standardvorlage](./readme-standard-template.md), [Allgemeine Schreibspezifikation](./general-writing-specification.md) |
| Engineering | [Codestil-Spezifikation](./code-style-specification.md), [Commit-Nachrichten-Spezifikation](./commit-message-specification.md), [Testspezifikation](./testing-specification.md) |
| Veröffentlichung | [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md), [LICENSE-Spezifikation](./license-specification.md) |

Bei Verwendung dieser Kombination ist in den Liefergegenständen der herabgestufte Modus zu erklären und vor der ersten öffentlichen Freigabe die vollständige Kombination gemäß Abschnitt 6.3 nachzuholen.

### 6.2 Standard-Kombination für die öffentliche Freigabe

Aufbauend auf der minimal nutzbaren Kombination sind die Grundlagen zu Qualität, Compliance, Governance und Betrieb zu ergänzen: hinzu kommen [Qualitätstor](./quality-gate.md), [README-Abschnittsspezifikation](./readme-sections-specification.md), [README-Visuallayout-Spezifikation](./readme-visual-layout-specification.md), [Badge-Spezifikation](./badge-specification.md), [Dokumentationsmatrix](./document-matrix.md), [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md), [Haftungsausschluss-Vorlage](./disclaimer-template.md), [SECURITY-Vorlage](./security-template.md), [Contributing-Guide-Vorlage](./contribution-guide-template.md), [Verhaltenskodex-Vorlage](./code-of-conduct-template.md), [Änderungsprotokoll-Spezifikation](./changelog-specification.md), [Versionsverwaltungsspezifikation](./version-management-specification.md), [Barrierefreiheitsspezifikation](./accessibility-specification.md), [CI-Workflow-Spezifikation](./ci-workflow-specification.md), [Issue- und PR-Vorlagenspezifikation](./issue-and-pr-template-specification.md), [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md).

Diese Kombination erfüllt alle Freigabebedingungen der Gates A, B, C für öffentliche Repositorys und ist der empfohlene Ausgangspunkt für die meisten Projekte.

### 6.3 Vollständig konforme Kombination

Wendet alle Spezifikationen an und ist für Projekte auf Organisationsebene, für Projekte, die in regulierten Umgebungen verteilt werden, oder für Projekte mit programmatischem Zugang über Experten / Skills / MCP / Befehlszeile vorgesehen. Die Dokumentenanzahl richtet sich nach dem [chinesischen Index](./README.md); bei der Aktivierung sind die Phasen-Qualitätstore der [Lebenszyklus-Zuordnungstabelle](./lifecycle-mapping-table.md) Punkt für Punkt zu prüfen.

## 7. Konfliktbehandlung

1. Bei Konflikten innerhalb derselben Dimension gelten die Anforderungen der späteren Veröffentlichungsphase; Vereinfachungen der Prototypenphase dürfen nicht in die öffentliche Freigabephase fortgeführt werden.
2. Bei Konflikten zwischen verschiedenen Dimensionen ist nach der Priorität aus Abschnitt 2 zu verfahren; verbindliche Vorgaben und Phasen-Qualitätstore dürfen durch keine Dimension überlagert werden.
3. Erfordern besondere Umstände eines Projekts eine Abweichung von diesem Leitfaden, sind die abweichende Spezifikation, die Begründung und die Ausgleichsmaßnahmen in den Liefergegenständen zu dokumentieren und einem Review zu unterziehen.
4. Der herabgestufte Modus darf nicht für öffentliche Repositorys verwendet werden und nicht als Grundlage für den Verzicht auf Lizenz- oder Sicherheits-Qualitätstore dienen.

## Verwandte Dateien

- Zur vollständigen Zuordnung von Phasen und Spezifikationen siehe [Lebenszyklus-Zuordnungstabelle](./lifecycle-mapping-table.md)
- Zum typbedingten Zuschnitt der README-Abschnitte siehe [README-Kategorieanpassungsleitfaden](./readme-category-adaptation-guide.md)
- Zu den nicht zuschneidbaren Vorgaben siehe [Harte Regeln](./hard-rules.md), [Verbotene Praktiken](./prohibited-practices.md)
- Zu den Freigabebedingungen der Qualitätstore siehe [Qualitätstor](./quality-gate.md)
