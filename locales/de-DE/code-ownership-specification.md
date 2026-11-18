# Code-Eigentums-Spezifikation

> Problem, das diese Datei löst: Sie definiert Syntax, Eigentumszuweisung und Review-Routing-Regeln der Datei `.github/CODEOWNERS`, damit jede Änderung automatisch dem zuständigen Reviewer zugewiesen wird.

## 1. Designprinzipien

1. **Eindeutige Zuordnung von Pfad zu Person**: Jede Regel benennt, wer für einen Pfad verantwortlich ist, um fehlende oder doppelte Reviews zu vermeiden.
2. **Minimal notwendige Owners**: Die Anzahl der Owners eines Pfades bleibt auf 1–3 Personen beschränkt; zu viele führen zu verwässerter Verantwortung.
3. **Standardübernahme**: Ein globaler Standard-Owner wird festgelegt und deckt Pfade ab, die von keiner expliziten Regel erfasst werden.
4. **Synchronisation mit der Teamstruktur**: Bei Mitgliederwechseln ist die Datei zeitnah zu aktualisieren, damit inaktive Konten Reviews nicht blockieren.

## 2. Dateiposition und Syntax

### 2.1 Pfad

Die Datei `CODEOWNERS` kann an einer der folgenden Positionen liegen; es gilt die erste gefundene Position in Prioritätsreihenfolge:

1. Repository-Wurzelverzeichnis `CODEOWNERS`;
2. `docs/CODEOWNERS`;
3. `.github/CODEOWNERS` (empfohlen).

### 2.2 Syntaxregeln

```text
# Kommentar beginnt mit #
<Pfadmuster>  <Owner>  [<Owner>...]
```

- Eine Regel pro Zeile, dem Pfadmuster folgt ein oder mehrere Owner.
- Das Owner-Format lautet `@Benutzername` oder `@Organisation/Team`.
- Owner in Form einer E-Mail-Adresse müssen mit einem GitHub-Konto verknüpft sein.
- Pfade sind groß- und kleinschreibungsabhängig und unterstützen die Platzhalter `*` und `**`.

### 2.3 Beispiel

```text
# Standard-Owner
*                       @org/maintainers

# Zuweisung nach Verzeichnis
/src/core/              @org/core-team
/src/api/               @org/api-team @alice
/docs/                  @org/docs-team

# Zuweisung nach Dateityp
*.md                    @org/docs-team
/.github/workflows/      @org/devops-team
```

## 3. Übereinstimmungsregeln

1. Nur die letzte passende Regel greift, es erfolgt keine Kumulierung; allgemeine Regeln müssen daher vorn, spezielle Regeln hinten stehen.
2. Eine Verzeichnisregel erfasst das Verzeichnis und seine Unterverzeichnisse, sofern sie nicht mit `/` beginnt und damit den Wurzelpfad einschränkt.
3. Die Regelreihenfolge bestimmt die Priorität und muss von breit nach eng angeordnet sein.
4. Pfade ohne passende Regel werden vom Standard-Owner verantwortet.

## 4. Strategie der Eigentumszuweisung

| Dimension | Zuweisungsgrundlage |
| --- | --- |
| Verzeichnis | Zuweisung nach Modul- oder Subsystemgrenzen |
| Dateityp | Dokumentation, Konfiguration und Tests können typbezogen einheitlich zugewiesen werden |
| Kritische Pfade | Sicherheit, Veröffentlichung und CI-Konfiguration liegen ausschließlich bei den Kernmaintainern |
| Neue Mitglieder | Zunächst als nicht erforderliche Reviewer beteiligt, nach Einarbeitung als reguläre Owners |

## 5. Verknüpfung mit dem Review-Prozess

1. Bei der Erstellung eines PRs fordert GitHub automatisch die Owners der passenden Pfade zum Review an.
2. Erforderliche Reviews werden über Regeln zum Branch-Schutz konfiguriert, siehe [Git-Workflow- und Branching-Spezifikation](./git-workflow-and-branching-specification.md).
3. Owners müssen innerhalb der vereinbarten Frist reagieren; bei Überschreitung übernimmt der Standard-Owner.
4. Änderungen an den Owners erfordern eine gleichzeitige Aktualisierung der Datei, damit inaktive Konten den Prozess nicht blockieren (siehe [Code-Review-Spezifikation](./code-review-specification.md)).

## 6. Pflegeanforderungen

1. Nach jeder Änderung der Organisationsstruktur oder der Teamzuständigkeiten ist eine erneute Prüfung durchzuführen.
2. Bei Repository-Übergabe oder Ausscheiden von Mitgliedern sind die entsprechenden Owners unverzüglich zu entfernen.
3. Änderungen an der Datei erfordern ein Review durch mindestens einen bestehenden Owner, um eine unkontrollierte Ausweitung der Rechte zu verhindern.
4. Owners dürfen nicht auf inaktive Konten oder Bot-Konten verweisen (ausgenommen sind ausschließlich Automatisierungskonten).

## 7. Verbotene Praktiken

1. Der Einsatz zu breiter Platzhalterregeln, die alle Personen zu Owners machen, ist verboten.
2. Sensible Pfade (Veröffentlichung, Geheimniskonfiguration) dürfen nicht Mitgliedern ohne Review-Kompetenz zugewiesen werden.
3. Das Eintragen privater Kontaktdaten in die Datei ist verboten.
4. Die dauerhafte Beibehaltung der Owner-Rolle ausgeschiedener Mitglieder ist verboten.

## Verwandte Dateien

- Abgrenzung der Dateizuständigkeiten: [Dokumentationsmatrix](./document-matrix.md)
- Review-Standards und Zuständigkeiten: [Code-Review-Spezifikation](./code-review-specification.md)
- Branch-Schutz: [Git-Workflow- und Branching-Spezifikation](./git-workflow-and-branching-specification.md)
- Automatisierte Prüfungen gehören zu Dimension D9, siehe [Prüfungsdimensionsmatrix](./review-dimension-matrix.md)
