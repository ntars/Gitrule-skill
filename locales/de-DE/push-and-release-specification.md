# Push- und Veröffentlichungsspezifikation

> Problem, das diese Datei löst: Definiert die Aktionslisten vor/während/nach dem Push, Regeln für Tags und Veröffentlichungen, den Ablauf der Incident-Behandlung sowie eine vollständige GitHub-Push-Anleitung und eine Matrix zur Behandlung von Fehlschlägen.

## 1. Vor dem Push

1. `git status` ist sauber, es existieren keine nicht verfolgten sensiblen Dateien.
2. `git log` enthält kein WIP, kein `fix bug`, keine Preisgabe personenbezogener Daten.
3. Es ist bestätigt, dass `.gitignore` wirkt und Artefakte sowie Abhängigkeiten nicht verfolgt werden.
4. Build, Test und Lint sind lokal erfolgreich.
5. Eine vollständige Secret-Suche wird ausgeführt (einschließlich historischer Commits).
6. Die Dokumentationsmatrix ist vollständig (siehe [Dokumentationsmatrix](./document-matrix.md)).

## 2. Push-Aktionen

7. Persönlichen Branch pushen: `git push -u origin feat/xxx`.
8. Der Hauptzweig wird ausschließlich über PRs beschritten, niemals direkt gepusht.
9. `push --force` ist verboten; zum Umschreiben des eigenen Branches ist `--force-with-lease` zu verwenden.
10. Rebase/Amend auf bereits gepushten öffentlichen Branches ist verboten.
11. Einzeldateien >50 MB werden zunächst über LFS geführt und dann gepusht.
12. Vor dem ersten Push ist die Sichtbarkeit des Repositorys zu bestätigen: standardmäßig private, public erst bei tatsächlichem Bedarf.

## 3. Tag und Veröffentlichung

13. Tag-Format `vMAJOR.MINOR.PATCH`, zwingend annotated: `git tag -a v1.0.0 -m "release: 1.0.0"`.
14. Ein Tag wird erst gesetzt, wenn CI grün und die Release Notes fertig sind.
15. Brechende Änderungen erfordern `feat!:` oder `BREAKING CHANGE:` und im CHANGELOG die Angabe des Migrationswegs.

## 4. Phase 6 · Nach dem Push (Post-Push)

- annotated Tag setzen;
- Release Notes schreiben;
- Verfügbarkeit von Badges und Links prüfen;
- CI-Grün bestätigen;
- Korrektheit der Angaben im About-Bereich bestätigen (description / topics / Links / social preview).

## 5. Incident-Behandlung

16. **Secret wurde gepusht**: sofort rotieren → mit `git filter-repo` bereinigen → Force-Push auf geschützte Branches über den Administratorablauf → Ankündigung.
17. **Große Datei versehentlich gepusht**: LFS-Migration oder Umschreiben der Historie; das bloße Löschen der Datei ist unzulässig.

## 6. Spezifikation für die GitHub-Push-Anleitung

Die Anleitung muss die folgenden sieben Teile enthalten; Befehle sind in vollständig ausführbarer Fassung anzugeben.

### 6.1 Vorherige Absicherung

1. Vor dem Push sind das lokale Repository und das Remote-Repository vollständig zu sichern; empfohlen ist `git clone --mirror` zur Erstellung einer Spiegelungssicherung.
2. Es ist zu bestätigen, dass das Remote-Repository keine Mitwirkenden hat oder dass die Mitwirkenden über die Pausierung von Pushes informiert wurden.
3. Es ist zu bestätigen, dass für den Zielbranch kein Force-Push-Schutz aktiviert ist.

### 6.2 Lokale Aufbereitung

```bash
git status
git diff --name-status HEAD
git ls-files
```

Die drei Ausgaben sind abzugleichen, um sicherzustellen, dass die zu committenden Änderungen mit dem lokalen Verzeichnis übereinstimmen und keine temporären Dateien, Build-Artefakte oder Rückstände alter Dokumentversionen vorhanden sind. `.gitignore` muss Build-Artefakte und lokale Konfigurationsdateien abdecken.

### 6.3 Konsistenzprüfung

```bash
git fetch origin
git diff --name-status HEAD origin/{{分支名}}
```

Dieser Befehl listet die Dateiunterschiede zwischen Remote und lokal auf. Dateien, die remote vorhanden, lokal aber gelöscht sind, müssen lokal mit `git rm` entfernt und committet werden, damit die Löschung in die Versionshistorie eingeht.

### 6.4 Commit und Push

```bash
git add -A
git commit -m "docs: 重建项目文档（README、README_EN、NOTICE）"
git push --force-with-lease origin {{分支名}}
```

`--force-with-lease` statt `--force` verwenden, da der Push abgelehnt wird, wenn remote neue Commits anderer Personen vorliegen, wodurch fremde Arbeit nicht überschrieben wird. Das Löschen und Neuerstellen des Remote-Repositorys ist eine risikoreiche Operation und nur bei persönlichen Repositorys mit abgeschlossener Spiegelungssicherung zulässig; die Anleitung muss das Risiko des Datenverlusts ausdrücklich kennzeichnen.

### 6.5 Prüfung nach dem Push

```bash
git ls-remote --heads origin
gh repo view --web
```

In der Weboberfläche sind Dateiliste, README-Darstellung, Sprachumschaltlinks und NOTICE-Links punktweise auf Gültigkeit zu prüfen.

### 6.6 Matrix zur Behandlung von Fehlschlägen

| Fehlertyp | Typische Erscheinung | Behandlungsmaßnahme | Risikohinweis |
| --- | --- | --- | --- |
| Authentifizierungsfehler | `Authentication failed`, `Permission denied (publickey)` | von HTTPS auf SSH umstellen und Schlüssel konfigurieren oder nach `gh auth login` pushen | keiner |
| Netzwerkunterbrechung | `Failed to connect`, `RPC failed` | Netzwerk wechseln, Proxy konfigurieren, `git config --global http.postBuffer 524288000` ausführen | keiner |
| Dateigröße überschritten | `remote: error: File exceeds 100 MB` | große Datei aus der Commit-Historie entfernen oder Git LFS aktivieren | nach dem Umschreiben der Historie sind Mitwirkende zum erneuten Klonen aufzufordern |
| Groß-/Kleinschreibungs-Konflikt | doppelte Einträge durch abweichende Groß-/Kleinschreibung von Dateinamen | mit `git mv` korrigieren und committen | keiner |
| Historienkonflikt | `non-fast-forward`, `fetch first` | vorrangig `git pull --rebase`; bei zwingendem Überschreiben `--force-with-lease` verwenden | Überschriebene fremde Commits sind nicht wiederherstellbar |
| Branch-Schutz | `protected branch hook declined` | über den PR-Ablauf zusammenführen oder Regeln durch Administrator temporär anpassen | Anpassungen der Regeln sind zu protokollieren |
| Beschädigtes Repository | `fatal: not a git repository`, fehlende Objekte | nach erneutem Klonen die Arbeitsbereichsänderungen kopieren | Arbeitsbereich ist vorher zu sichern |

### 6.7 Rollback

Treten nach abgeschlossenem Push Probleme auf, ist mit `git revert` ein umgekehrter Commit zu erzeugen; eine erneute Force-Push-Überschreibung der bereits öffentlichen Historie ist unzulässig.

## Verwandte Dateien

- Vor dem Push sind die drei Qualitätstore der [Qualitätstor](./quality-gate.md) zu bestehen
- Rote Linien zu Secrets und großen Dateien siehe H3/H5/H12 der [Harte Regeln](./hard-rules.md)
- Die Commit-Nachrichten-Spezifikation gehört zu Dimension D7, siehe [Review-Dimensionsmatrix](./review-dimension-matrix.md)
- Verantwortlichkeit der Veröffentlichungsdokumentation `docs/release.md` siehe [Dokumentationsmatrix](./document-matrix.md)
