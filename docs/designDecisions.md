---
title: Evidence / Raw Material
nav_order: 2
---

# Design Decisions

Diese Seite dokumentiert wichtige Designentscheidungen, die während der Entwicklung der Nachhilfe-Plattform getroffen wurden.

Jede Entscheidung beschreibt das zugrunde liegende Problem, mögliche Alternativen, die getroffene Entscheidung sowie die Begründung.

---

## Mohd Alkhtib
### Design Decision 1: Zentrale CSS-Datei

#### Problem Statement
Für die Webanwendung mussten mehrere HTML-Seiten gestaltet werden, darunter die Startseite, Login, Registrierung, Lehrersuche, Lehrerprofil sowie die Dashboards für Schüler/innen und Lehrkräfte.

Die Frage war, ob für jede Seite eine eigene CSS-Datei erstellt werden soll oder ob eine gemeinsame CSS-Datei für das gesamte Projekt verwendet wird.

#### Decision
Wir haben uns für eine zentrale CSS-Datei (style.css) entschieden.

Da viele Seiten gemeinsame Elemente wie Header, Navigation, Buttons, Formulare und Container verwenden, konnten diese Stile zentral definiert und wiederverwendet werden.

Dadurch mussten identische CSS-Regeln nicht mehrfach in verschiedenen Dateien gepflegt werden.

Die Entscheidung wurde von Mohd Alkhtib vorgeschlagen und anschließend im Team abgestimmt.

#### Regarded Options

| Option | Vorteile | Nachteile |
|---|---|---|
| Eine CSS-Datei pro Seite | Bessere Trennung der einzelnen Seitendesigns | Viele doppelte CSS-Regeln, höherer Pflegeaufwand |
| Eine zentrale CSS-Datei | Wiederverwendung gemeinsamer Komponenten, einfachere Wartung, konsistentes Design | Datei wird mit zunehmender Projektgröße größer |


#### Begründung
Da viele Seiten dieselbe Navigation und ähnliche Layout-Komponenten verwenden, wäre bei mehreren CSS-Dateien derselbe Code mehrfach vorhanden gewesen.

Mit einer zentralen CSS-Datei konnten gemeinsame Stile nur einmal definiert werden. Änderungen an der Navigation oder am allgemeinen Design mussten dadurch nur an einer Stelle vorgenommen werden.

Für den Umfang unseres Projekts war eine einzelne CSS-Datei die einfachere und wartungsfreundlichere Lösung.

### Design Decision 2: Gestaltung des Vernetzungsplans

#### Problem Statement
Für die Nachhilfe-Plattform musste ein Vernetzungsplan erstellt werden, der die Navigation der Anwendung verständlich darstellt.

Die Herausforderung war, eine passende Balance zwischen Vollständigkeit und Übersichtlichkeit zu finden. Der Plan sollte die wichtigsten Seiten, Benutzerrollen und Navigationswege zeigen, ohne zu kompliziert oder unübersichtlich zu wirken.

#### Decision
Es wurden mehrere Versionen des Vernetzungsplans erstellt und miteinander verglichen.

Die erste Version mit dem Titel „Webseitenstruktur & Vernetzungsplan“ war sehr detailliert. Sie enthielt viele Informationen, Rollen, Funktionen und technische Hinweise. Dadurch war sie zwar vollständig, aber für unsere Dokumentation zu komplex und schwer überschaubar. 
<img src="evidence/images/V1.jpg" alt="ersteVersion" width="350">

Die zweite Version ohne Titel war einfacher aufgebaut. Diese Version war jedoch inhaltlich nicht überzeugend, da die Struktur nicht klar genug waren. (in der "evidence.md" dokumentiert)

Am Ende haben wir uns für die dritte Version mit dem Titel „Vernetzungsplan“ entschieden. Diese Version zeigt die wichtigsten Seiten und Verbindungen klarer und einfacher. Sie hat unsere weitere Arbeit erleichtert, weil wir dadurch besser verstanden haben, welche Seiten benötigt werden und wie Nutzer/innen durch die Anwendung navigieren. (in der "index.md" dokumentiert)

Die Entscheidung wurde von Mohd Alkhtib vorbereitet und anschließend mit dem Team abgestimmt.

#### Regarded Options

| Option | Vorteile | Nachteile |
|----------|----------|----------|
| Sehr detaillierter Vernetzungsplan („Webseitenstruktur & Vernetzungsplan“) | Viele Informationen, Rollen und Funktionen enthalten | Zu komplex, schwer überschaubar, für unsere Projektphase zu umfangreich |
| Vereinfachte farbige Version ohne Titel | Einfachere Darstellung, verschiedene Bereiche farblich getrennt | Farben und Struktur waren nicht klar genug, wirkte nicht vollständig durchdacht |
| Finale Version „Vernetzungsplan“ | Klar, übersichtlich, zeigt die wichtigsten Seiten und Wege, erleichtert die weitere Arbeit | Weniger Detailtiefe als die erste Version |

#### Begründung
Die finale Version wurde gewählt, weil sie am besten zu unserem Projektstand passt. Sie zeigt die wichtigsten Bereiche der Plattform, ohne den Leser mit zu vielen Details zu überfordern.

Außerdem unterstützt sie unseren Happy Path besser: Von der Startseite über Registrierung und Login bis zu den Dashboards und den wichtigsten Funktionen wie Suche, Lehrerprofil, Buchung und rechtlichen Seiten.

Durch diese Entscheidung konnten wir klarer festlegen, welche Seiten für die Umsetzung wichtig sind und wie die Navigation in der Anwendung aufgebaut sein soll.

---

## Benyamin Hasan
###  Design Decision 1: 

---

## Abdullah Aldarwish
### Design Decision 1: Gestaltung des Datenmodells

#### Problem Statement

Für die Nachhilfe-Plattform musste ein Datenmodell erstellt werden, das die wichtigsten Bereiche der Anwendung abbildet.

Dabei musste entschieden werden, ob die Plattform mit wenigen einfachen Tabellen umgesetzt wird oder ob mehrere Tabellen mit klaren Beziehungen verwendet werden. Besonders wichtig war die Frage, wie Nutzer/innen, Schülerprofile, Lehrerprofile, Fächer, Buchungen und Bewertungen miteinander verbunden werden.

#### Decision

Wir haben uns für ein detailliertes Datenmodell mit mehreren verbundenen Tabellen entschieden.

Dazu gehören unter anderem:

- User
- SchülerProfil
- LehrerProfil
- Fach
- LehrerFach
- Buchung
- Bewertung
- Meldung
- Verifizierungsdokument

Die Entscheidung wurde von Abdullah Aldarwish vorbereitet und anschließend im Team abgestimmt.

#### Regarded Options

| Option | Vorteile | Nachteile |
|---|---|---|
| Einfaches Datenmodell mit wenigen Tabellen | Schnell umzusetzen, weniger Komplexität | Viele Informationen müssten in wenigen Tabellen gespeichert werden, schlechter erweiterbar |
| Detailliertes Datenmodell mit mehreren Tabellen | Klare Struktur, bessere Beziehungen zwischen Daten, näher an der echten Anwendung | Mehr Planungsaufwand und komplexere Umsetzung |

#### Begründung

Die detaillierte Lösung wurde gewählt, weil unsere Plattform mehrere unterschiedliche Bereiche benötigt. Schüler/innen, Lehrer/innen, Fächer, Buchungen und Bewertungen haben unterschiedliche Informationen und sollten deshalb sauber voneinander getrennt werden.

Durch die getrennten Tabellen können Daten besser miteinander verknüpft werden. Zum Beispiel kann eine Buchung eindeutig mit einem Schüler, einem Lehrer und einem Fach verbunden werden.

Für unser Projekt war diese Struktur sinnvoll, weil sie besser zum geplanten Happy Path und zu den Anforderungen der Nachhilfe-Plattform passt.

#### Nachweise

- Datenmodell in `index.md`
- Umsetzung in `models.py`
- Datenbank-Screenshot in `evidence.md`

### Design Decision 2: SQLite als Datenbank

#### Problem Statement

Für die Nachhilfe-Plattform musste entschieden werden, welche Datenbanktechnologie verwendet wird.

Die Anwendung sollte lokal auf einem Windows- oder MacOS-System ausführbar sein und ohne komplizierte Serverinstallation funktionieren. Gleichzeitig mussten Nutzer/innen, Profile, Fächer, Buchungen und Bewertungen gespeichert werden können.

#### Decision

Wir haben uns für SQLite als Datenbank entschieden.

SQLite speichert die Daten in einer lokalen Datenbankdatei und benötigt keinen zusätzlichen Datenbankserver. Dadurch konnte die Anwendung einfacher eingerichtet, getestet und für die First Submission vorbereitet werden.

Die Entscheidung wurde von Abdullah Aldarwish vorbereitet und anschließend im Team abgestimmt.

#### Regarded Options

| Option | Vorteile | Nachteile |
|---|---|---|
| SQLite | Einfach einzurichten, keine Serverinstallation nötig, gut für lokale Entwicklung geeignet | Weniger geeignet für große produktive Anwendungen |
| MySQL oder PostgreSQL | Leistungsfähiger und besser für große Anwendungen geeignet | Zusätzliche Installation und Konfiguration notwendig |
| Keine Datenbank, nur feste Dummy-Daten im Code | Sehr einfach für erste Tests | Keine echte Speicherung, passt nicht zu Login, Profilen und Buchungen |

#### Begründung

SQLite wurde gewählt, weil es für den Umfang unseres Hochschulprojekts ausreichend ist und die Anwendung dadurch leicht lokal gestartet werden kann.

Außerdem passt SQLite gut zu Flask und SQLAlchemy. Die Datenbankdatei kann direkt im Projekt verwendet werden, wodurch der Prüfer die Anwendung einfacher reproduzieren kann.

Für die First Submission war SQLite deshalb die einfachste und sinnvollste Lösung.

#### Nachweise

- Datei `instance/nachhilfe.db`
- Datenbank-Screenshot in `evidence.md`
- Datenbankkonfiguration in `app.py`

  ---

## Emrah 
###  Design Decision 1: 

---
