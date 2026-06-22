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
####  Design Decision 1: 

---