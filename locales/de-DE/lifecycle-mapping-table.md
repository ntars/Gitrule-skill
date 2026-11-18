# Lebenszyklus-Zuordnungstabelle

> Problem, das diese Datei löst: Ordnet alle Spezifikationen den acht Phasen des Projektlebenszyklus zu und gibt für jede Phase Eintrittsbedingungen, Schlüsselergebnisse, Kernspezifikationen und Austritts-Qualitätstore an, als einheitlicher Navigationseinstieg für die Anwendung der Spezifikationen „von innen nach außen, von Anfang bis Ende“.

Diese Datei beantwortet ausschließlich „welche Spezifikationen eine Phase benötigt und wann in die nächste Phase eingetreten werden kann“. Die konkreten Bestimmungen der einzelnen Spezifikationen innerhalb einer Phase richten sich weiterhin nach der jeweiligen Datei; zum Ablauf siehe [Ausführungsprozess](./execution-process.md), zum Zuschnitt nach Projekttyp siehe [Spezifikationsauswahlleitfaden](./specification-selection-guide.md).

## 1. Phasenübersicht

| Phase | Name | Kernfrage | Schlüsselergebnisse | Austritts-Qualitätstor |
| --- | --- | --- | --- | --- |
| 1 | Projektstart | Was tun, wie heißen, wie das Repository einrichten | Namensentscheidung, Repository-Metadatentabelle, Informationsliste | Namenskonformität, Pflichtangaben vollständig oder gekennzeichnet |
| 2 | Anforderungsanalyse | Welche Anforderungen, wie abnehmen | Anforderungsliste, Abnahmekriterien, Verfolgungsmatrix | Jede Anforderung mit eindeutiger Kennung und Abnahmekriterium |
| 3 | Architekturdesign | Wie zerlegen, wie Schnittstellen und Daten vereinbaren | Architekturdokument, API-Vertrag, Datenmodell | lückenlose Verfolgung von Anforderungen zum Design, Schnittstellen geprüft |
| 4 | Entwicklungsimplementierung | Wie Code und Commits konsistent schreiben | Code, Commit-Folge, CI-Workflow, API-Dokumentation | Review bestanden, CI grün, keine hochriskanten Schwachstellen in Abhängigkeiten |
| 5 | Testverifikation | Ist die veröffentlichungsfähige Qualität erreicht | Testsammlung, Abdeckungsbericht, Qualitätstor-Urteil | Build und Tests bestanden, P0 auf null |
| 6 | Bereitstellung und Go-live | Wie veröffentlichen, wie die Startseite darstellen | Tag, Release, Startseiten-Dokumentation, Rollback-Konzept | alle drei Qualitätstore grün, Rollback-Konzept verifiziert |
| 7 | Betrieb und Monitoring | Wie Probleme erkennen, wie reagieren | Monitoring-Alarme, Reaktionsablauf, Störungsdokumentation | Alarme für Schlüsselmetriken, Reaktionskanäle verfügbar |
| 8 | Iterative Wartung | Wie nachbetrachten, wie weiterentwickeln | Retrospektivenbericht, Roadmap-Aktualisierung, Migrationsleitfaden | Maßnahmen registriert, Migrationspfad für brechende Änderungen |

Die Phasen 1–5 schreiten von innen nach außen voran, die Phasen 6–8 wechseln von der Auslieferung zu Betrieb und Weiterentwicklung. Die Phasen 7 und 8 können parallel verlaufen, dürfen aber das Qualitätstor der Phase 5 nicht überspringen.

## 2. Phase eins: Projektstart

- **Phasenziel**: Projektpositionierung, konforme Benennung und Repository-Metadaten festlegen und eine für die folgenden Phasen gemeinsame Informationsbasis schaffen.
- **Eintrittsbedingung**: Die Projektidee ist entstanden, Zielnutzende und zu lösendes Problem sind darstellbar.
- **Kernspezifikationen**: [Rollen und Verantwortlichkeiten](./roles-and-responsibilities.md), [Projektstart- und Anforderungsspezifikation](./project-initiation-and-requirements-specification.md), [Projektbenennungsspezifikation](./project-naming-specification.md), [Informationserfassung und Vorlagen](./information-collection-and-templates.md), [Ausführungsprozess](./execution-process.md).
- **Schlüsselergebnisse**: drei Namenskandidaten mit Ergebnissen der Namensgleichheitsprüfung; Repository-Metadatentabelle (Beschreibung, Themen-Tags, Standard-Branch, Sichtbarkeit, Lizenz); Liste der Pflichtangaben und Liste fehlender Angaben.
- **Austritts-Qualitätstor**: Der Repository-Name erfüllt alle harten Regeln der [Projektbenennungsspezifikation](./project-naming-specification.md); der Lizenztyp ist festgelegt; die Pflichtfelder sind vollständig, fehlende Punkte sind gemäß [Informationserfassung und Vorlagen](./information-collection-and-templates.md) gekennzeichnet.

## 3. Phase zwei: Anforderungsanalyse

- **Phasenziel**: Die Idee in abnehmbare, verfolgbare Anforderungspositionen zerlegen und daraus eine Roadmap formen.
- **Eintrittsbedingung**: Die Ergebnisse zu Benennung und Metadaten aus Phase eins sind bestätigt.
- **Kernspezifikationen**: [Projektstart- und Anforderungsspezifikation](./project-initiation-and-requirements-specification.md), [Spezifikation für die Anforderungs-Verfolgungsmatrix](./requirements-traceability-matrix-specification.md), [Roadmap-Spezifikation](./roadmap-specification.md), [Informationserfassung und Vorlagen](./information-collection-and-templates.md).
- **Schlüsselergebnisse**: Anforderungsliste mit eindeutigen Kennungen; Abnahmekriterien für jede Anforderung; Erstfassung der Anforderungs-Verfolgungsmatrix; nach Priorität geordnete Roadmap.
- **Austritts-Qualitätstor**: Jede Anforderung besitzt eine eindeutige Kennung und beurteilbare Abnahmekriterien; die Verfolgungsmatrix enthält die Felder der Anforderungsseite; geplante Punkte der Roadmap sind als keine Lieferzusage gekennzeichnet.

## 4. Phase drei: Architekturdesign

- **Phasenziel**: Modulgrenzen, Schnittstellenverträge und Datenmodell festlegen, damit Anforderungen konkreten Designeinheiten zugeordnet werden können.
- **Eintrittsbedingung**: Anforderungsliste und Abnahmekriterien sind bestätigt.
- **Kernspezifikationen**: [Spezifikation für Architekturdesign-Dokumente](./architecture-design-document-specification.md), [API-Designspezifikation](./api-design-specification.md), [Datenbank-Designspezifikation](./database-design-specification.md), [Dokumentationsmatrix](./document-matrix.md), [Allgemeine Schreibspezifikation](./general-writing-specification.md).
- **Schlüsselergebnisse**: Architekturdesign-Dokument; API-Vertrag; Datenmodell und Migrationsstrategie; Liste der Dokumentationsmatrix.
- **Austritts-Qualitätstor**: Jede Anforderung verweist in der Verfolgungsmatrix auf mindestens eine Designeinheit; Schnittstellen und Datenmodell sind geprüft; die Verantwortlichkeiten der Dateien in der Dokumentationsmatrix überschneiden sich nicht.

## 5. Phase vier: Entwicklungsimplementierung

- **Phasenziel**: Das Design mit konsistentem Codestil, Commit-Format und Review-Ablauf umsetzen und Abhängigkeiten sowie Automatisierung beherrschbar halten.
- **Eintrittsbedingung**: Architektur und Schnittstellenverträge sind im Review bestätigt.
- **Kernspezifikationen**: [Codestil-Spezifikation](./code-style-specification.md), [Git-Workflow- und Branching-Spezifikation](./git-workflow-and-branching-specification.md), [Commit-Nachrichten-Spezifikation](./commit-message-specification.md), [Code-Review-Spezifikation](./code-review-specification.md), [Abhängigkeitsverwaltungsspezifikation](./dependency-management-specification.md), [Code-Eigentumsspezifikation](./code-ownership-specification.md), [API-Dokumentationsspezifikation](./api-documentation-specification.md), [CI-Workflow-Spezifikation](./ci-workflow-specification.md).
- **Schlüsselergebnisse**: Codestil-konformer Code; Commit-Folge gemäß Conventional Commits; CI-Workflow; mit der Implementierung synchron gehaltene API-Dokumentation.
- **Austritts-Qualitätstor**: Commit-Nachrichten und Branch-Namen entsprechen der Spezifikation; der Code ist geprüft und das Eigentums-Routing korrekt; der CI-Workflow ist erfolgreich; in Abhängigkeiten bestehen keine unbehandelten hochriskanten Schwachstellen.

## 6. Phase fünf: Testverifikation

- **Phasenziel**: Mit reproduzierbaren Tests und Qualitätstor-Urteilen bestätigen, dass die Liefergegenstände die für die Veröffentlichung erforderliche Qualitätsbasis erreichen.
- **Eintrittsbedingung**: Die funktionale Implementierung ist abgeschlossen, der CI-Workflow ist ausführbar.
- **Kernspezifikationen**: [Testspezifikation](./testing-specification.md), [Qualitätstor](./quality-gate.md), [Spezifikation für Qualitätsmetriken](./quality-metrics-specification.md), [Barrierefreiheitsspezifikation](./accessibility-specification.md), [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md).
- **Schlüsselergebnisse**: Testsammlung und Abdeckungsbericht; punktuelles Urteil je Qualitätstor; Prüfnachweise zu Sicherheit und Barrierefreiheit.
- **Austritts-Qualitätstor**: Build, Tests und statische Analyse sind erfolgreich; alle P0-Punkte der Gates A, B, C sind auf null gebracht; P1-Punkte sind als To-do registriert oder abgeschlossen.

## 7. Phase sechs: Bereitstellung und Go-live

- **Phasenziel**: Die Version nach einem kontrollierten Ablauf veröffentlichen und Startseiten-Dokumentation sowie nutzerseitig sichtbare Liefergegenstände abschließen.
- **Eintrittsbedingung**: Das Qualitätstor der Phase fünf ist bestanden, es bestehen keine nicht auf null gebrachten P0-Punkte.
- **Kernspezifikationen**: [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md), [Versionsverwaltungsspezifikation](./version-management-specification.md), [Änderungsprotokoll-Spezifikation](./changelog-specification.md), [Bereitstellungs- und Rollback-Spezifikation](./deployment-and-rollback-specification.md), [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md), [CI-Workflow-Spezifikation](./ci-workflow-specification.md), [Issue- und PR-Vorlagenspezifikation](./issue-and-pr-template-specification.md); Startseiten-Dokumentation siehe [README-Standardvorlage](./readme-standard-template.md), [README-Abschnittsspezifikation](./readme-sections-specification.md), [README-Visuallayout-Spezifikation](./readme-visual-layout-specification.md), [Badge-Spezifikation](./badge-specification.md), [README-Kategorieanpassungsleitfaden](./readme-category-adaptation-guide.md).
- **Schlüsselergebnisse**: Semantische Version und annotierte Tags; Release Notes und Änderungsprotokoll; Startseiten-README und Community-Vorlagen; Bereitstellungsprotokoll und Rollback-Konzept.
- **Austritts-Qualitätstor**: Alle drei Qualitätstore sind grün; das Tag ist annotiert und entspricht SemVer; das Rollback-Konzept ist verifiziert; die Startseiten-Dokumentation enthält keine lokalen absoluten Pfade und keine Platzhalterrückstände.

## 8. Phase sieben: Betrieb und Monitoring

- **Phasenziel**: Observability-Fähigkeiten und Reaktionsmechanismen aufbauen, damit Online-Probleme erkannt, lokalisiert und behandelt werden können.
- **Eintrittsbedingung**: Die Version ist veröffentlicht, der Dienst oder das Artefakt ist verfügbar.
- **Kernspezifikationen**: [Observability-Spezifikation](./observability-specification.md), [Incident-Reaktionsspezifikation](./incident-response-specification.md), [Fehlerbehebungsspezifikation](./troubleshooting-specification.md), [Sicherheits- und Datenschutzspezifikation](./security-and-privacy-specification.md), [SECURITY-Vorlage](./security-template.md), [Haftungsausschluss](./disclaimer.md), [Haftungsausschluss-Vorlage](./disclaimer-template.md).
- **Schlüsselergebnisse**: Schlüsselmetriken und Alarmregeln; Incident-Einstufung und Reaktionsablauf; Dokumentation zu häufigen Problemen und Fehlerbehebung; Kanal zur Entgegennahme von Schwachstellen.
- **Austritts-Qualitätstor**: Für alle Schlüsselmetriken sind Alarme konfiguriert; der Kanal für Schwachstellenmeldungen ist verfügbar und verifiziert; der Incident-Reaktionsablauf wurde mindestens einmal als Übung oder Tischübung durchlaufen.

## 9. Phase acht: Iterative Wartung

- **Phasenziel**: Die gelieferte Iteration nachbetrachten, den Entwicklungspfad steuern und die kontinuierliche Ausrichtung von Anforderungen, Design und Tests aufrechterhalten.
- **Eintrittsbedingung**: Mindestens eine Veröffentlichung oder ein Iterationszyklus ist abgeschlossen.
- **Kernspezifikationen**: [Iterationsretrospektiven-Spezifikation](./iteration-retrospective-specification.md), [Roadmap-Spezifikation](./roadmap-specification.md), [Spezifikation für die Anforderungs-Verfolgungsmatrix](./requirements-traceability-matrix-specification.md), [Änderungsprotokoll-Spezifikation](./changelog-specification.md), [Migrationsleitfaden-Spezifikation](./migration-guide-specification.md), [Versionsverwaltungsspezifikation](./version-management-specification.md), [Open-Source-Förderungsspezifikation](./open-source-promotion-specification.md).
- **Schlüsselergebnisse**: Retrospektivenbericht und Maßnahmen; aktualisierte Roadmap und Verfolgungsmatrix; Migrationsleitfaden für brechende Änderungen; Versionsänderungsprotokoll.
- **Austritts-Qualitätstor**: Für die Maßnahmen der letzten Runde sind Verantwortliche und Fristen registriert; brechende Änderungen haben einen Migrationspfad und eine Ankündigung; die Verfolgungsmatrix weist keine Brüche auf.

## 10. Querschnittsspezifikationen

Die folgenden Spezifikationen gehören nicht zu einer einzelnen Phase und gelten durchgehend in allen Phasen:

| Kategorie | Spezifikation | Wirkungsweise |
| --- | --- | --- |
| Verbindliche Vorgaben | [Harte Regeln](./hard-rules.md), [Verbotene Praktiken](./prohibited-practices.md) | Verstoß in einer Phase blockiert; keine Ausnahme aus Zeitgründen |
| Ablauf und Terminologie | [Rollen und Verantwortlichkeiten](./roles-and-responsibilities.md), [Ausführungsprozess](./execution-process.md), [Glossar](./glossary.md) | Einheitliche Rollenteilung, Phasenterminologie und Lieferreihenfolge |
| Community und Governance | [Contributing-Guide-Spezifikation](./contribution-guide-specification.md), [Contributing-Guide-Vorlage](./contribution-guide-template.md), [Verhaltenskodex-Spezifikation](./code-of-conduct-specification.md), [Verhaltenskodex-Vorlage](./code-of-conduct-template.md) | Vor der externen Sichtbarkeit des Repositorys abschließen, danach an die Community-Größe anpassen |
| Recht und Compliance | [Open-Source-Compliance-Spezifikation](./open-source-compliance-specification.md), [LICENSE-Spezifikation](./license-specification.md), [NOTICE-Spezifikation](./notice-specification.md), [Haftungsausschluss](./disclaimer.md), [Haftungsausschluss-Vorlage](./disclaimer-template.md) | Phase eins legt die Lizenz fest, vor Phase sechs sind alle Rechtsdokumente fertig |
| Schreiben und Mehrsprachigkeit | [Allgemeine Schreibspezifikation](./general-writing-specification.md), [Mehrsprachigkeitsspezifikation](./multilingual-specification.md), [Leitfaden zu Features und Engineering-Abwägungen](./features-and-engineering-tradeoffs-guide.md), [Dokumentationsmatrix](./document-matrix.md) | Gilt für alle Dokumentergebnisse und sichert einheitliche Formulierungen |
| Programmatischer Zugang | [Spezifikation maschinenlesbarer Metadaten](./machine-readable-metadata-specification.md), [Skill-Autorenspezifikation](./skill-authoring-specification.md), [MCP-Werkzeugspezifikation](./mcp-tool-specification.md), [Agent-Aufruf- und Prompt-Spezifikation](./agent-invocation-and-prompt-specification.md) | Bei Bedarf an Aufruf über Experten, Skills, MCP oder Befehlszeile ergänzend anwenden |

## 11. Herabstufung und Rückfall

1. Private temporäre Skript-Repositories können auf die Ausführung ausschließlich der P0-Qualitätstore herabgestuft werden; dies ist jedoch in den Liefergegenständen als „herabgestufter Modus“ zu erklären und die nicht ausgeführten Punkte sind zu benennen.
2. Ist das Austritts-Qualitätstor einer Phase nicht bestanden, darf nicht in die nächste Phase eingetreten werden; Befunde, Verantwortliche und Maßnahmen sind gemäß [Prüfbericht-Format](./audit-report-format.md) zu registrieren.
3. Werden nach Phase sechs P0-Probleme festgestellt, ist zu Phase fünf zurückzukehren und neu zu urteilen; bei Bedarf ist der Incident-Behandlungsablauf der [Push- und Veröffentlichungsspezifikation](./push-and-release-specification.md) auszuführen.

## Verwandte Dateien

- Zum Ablauf innerhalb einer Phase siehe [Ausführungsprozess](./execution-process.md)
- Zum Zuschnitt der Spezifikationen nach Projekttyp siehe [Spezifikationsauswahlleitfaden](./specification-selection-guide.md)
- Zu den Beurteilungsmaßstäben der Qualitätstore siehe [Qualitätstor](./quality-gate.md)
- Zum Format der Registrierung von Prüfbefunden siehe [Prüfbericht-Format](./audit-report-format.md)
