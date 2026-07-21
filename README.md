# Nachhilfe-Plattform

Webbasierte Plattform zur Vermittlung von privater Nachhilfe zwischen Schüler/innen und privaten Lehrer/innen.

## Team 9:
+ Mohd Alkhtib  
+ Benyamin Hasan  
+ Abdullah Aldarwish  
+ Emrah Rabotic  

## Projektüberblick
Viele Schüler/innen haben Schwierigkeiten, passende und vertrauenswürdige Nachhilfelehrer/innen zu finden. Unsere Plattform löst dieses Problem, indem sie Schüler/innen und Lehrkräfte direkt miteinander verbindet.

Die Anwendung unterstützt den gesamten Ablauf – von der Registrierung über die Lehrersuche bis hin zur Buchung und Bewertung von Nachhilfestunden. Zusätzlich sorgen Verifizierungsdokumente, ein Meldesystem und eine Administratorfunktion für mehr Sicherheit und Vertrauen.

### Schüler/innen können:
- registrieren und anmelden
- Lehrer suchen
- Lehrerprofile ansehen
- Buchungsanfragen senden
- Buchungen verwalten
- Bewertungen abgeben
- Lehrerprofile melden

### Lehrer/innen können:
- registrieren und anmelden
- Verifizierungsdokument hochladen
- Nachhilfeangebote erstellen oder bearbeiten
- Buchungsanfragen annehmen oder ablehnen
- bestätigte Termine einsehen
- Bewertungen erhalten

### Administrator/innen können:
- Verifizierungsdokumente prüfen
- Dokumente akzeptieren oder ablehnen
- gemeldete Profile prüfen
- Meldungen verwalten
- Nutzerkonten sperren oder entsperren

## Plattform-Konzept
Die Anwendung basiert auf einer **zweiseitigen Plattform**:
+ **Seite 1:** Schüler/innen (Nachfrage)
+ **Seite 2:** Lehrer/innen (Angebot)

## Dokumentation

Die ausführliche Projektdokumentation wird über GitHub Pages veröffentlicht.

+ Die Hauptdokumentation befindet sich auf der Startseite (index.md).
+ Zusätzlich dokumentieren wir unsere Vorgehensweise, Entscheidungen, Feedbacks und Nachweise in der Seite Evidence (evidence.md).
+ Die Evidence-Seite kann über die Hauptdokumentation aufgerufen werden und zeigt die Entwicklung unseres Projekts von der ersten Idee bis zum aktuellen Stand.

## Verwendete Technologien

- Python
- Flask
- Jinja2
- SQLite
- SQLAlchemy
- HTML
- CSS
- Git
- GitHub

## Installation und Start

1. Repository klonen
2. Virtuelle Umgebung erstellen: `python -m venv .venv`
3. Virtuelle Umgebung aktivieren: 
    - Windows: `.venv\Scripts\activate`
    - Mac/Linux: `source venv/bin/activate`
4. Abhängigkeiten installieren: `pip install -r requirements.txt`
5. Testdaten erstellen: `python seed_data.py`
6. Anwendung starten: `python app.py`
7. Browser öffnen: http://127.0.0.1:5000

Hinweis für Schritt 5:

Falls bereits eine `nachhilfe.db` vorhanden ist, sollten die Testdaten nicht erneut erstellt werden.

Sollen die Testdaten dennoch neu erstellt werden, muss die vorhandene Datei `nachhilfe.db` zuerst gelöscht werden.

## Happy Path - Schüler/in

1. Registrierung und Upload eines Verifizierungsdokuments
2. Login
3. Lehrer suchen
4. Suche filtern
5. Lehrerprofil ansehen
6. Buchungsanfrage senden
7. Lehrer akzeptiert die Anfrage
8. Nachhilfestunde bewerten

## Happy Path - Lehrer/in

1. Registrierung und Upload eines Verifizierungsdokuments
2. Login
3. Nachhilfeangebot erstellen oder bearbeiten
4. Buchungsanfragen erhalten
5. Anfrage annehmen oder ablehnen
6. Bestätigte Termine verwalten
7. Bewertungen erhalten

## Happy Path – Administrator/in

1. Anmeldung mit dem Administratorkonto
2. Verifizierungsdokumente prüfen
3. Dokumente akzeptieren oder ablehnen
4. Meldungen prüfen
5. Nutzerkonten bei Bedarf sperren oder entsperren

## Testkonten

### Administrator
E-Mail: admin@test.de
Passwort: admin123

### Lehrer:
E-Mail: ali@test.de
Passwort: test123

### Schüler:
E-Mail: anna@test.de
Passwort: test123


## JSON API

Die Anwendung stellt eine einfache JSON-Schnittstelle bereit.

Verfügbare API-Endpunkte:
- http://127.0.0.1:5000/api/users → gibt alle registrierten Nutzer als JSON zurück

## Aktueller Stand
Die Final Submission enthält unter anderem folgende Funktionen:

- Registrierung und Login
- Lehrer-Suche mit Filtern und Sortierung
- Lehrerprofile
- Buchungssystem
- Bewertungssystem
- Schüler- und Lehrer-Dashboard
- Administrator-Dashboard
- Upload und Prüfung von Verifizierungsdokumenten
- Meldesystem
- Sperren und Entsperren von Nutzerkonten
- Profilverwaltung
- JSON API
