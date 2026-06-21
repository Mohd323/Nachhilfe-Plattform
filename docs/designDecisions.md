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