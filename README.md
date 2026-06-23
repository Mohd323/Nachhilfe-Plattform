# Nachhilfe-Plattform

Webbasierte Plattform zur Vermittlung von privater Nachhilfe zwischen Schüler/innen und privaten Lehrer/innen.

## Team 9:
+ Mohd Alkhtib  
+ Benyamin Hasan  
+ Abdullah Aldarwish  
+ Emrah Rabotic  

## Projektüberblick
Viele Schüler/innen haben Schwierigkeiten, passende Nachhilfelehrer/innen zu finden. Unsere Plattform löst dieses Problem, indem sie Schüler/innen und Lehrer/innen direkt miteinander verbindet.

### Schüler/innen können:
+ nach Lehrern suchen  
+ Profile ansehen  
+ Nachhilfe anfragen  

### Lehrer/innen können:
+ ihre Dienste anbieten  
+ Anfragen erhalten und verwalten  

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

## Happy Path - Schüler/in

1. Registrierung als Schüler/in und Upload des Schülerausweises
2. Login in das System
3. Suche nach einem passenden Nachhilfelehrer
4. Buchungsanfrage senden
5. Lehrer akzeptiert die Anfrage
7. Bewertung des Lehrers abgeben

## Happy Path - Lehrer/in

1. Registrierung als Lehrer/in und Upload eines Nachweisdokuments
2. Login in das System
3. Nachhilfeangebot erstellen oder bearbeiten
4. Buchungsanfrage erhalten
5. Anfrage annehmen oder ablehnen
6. Termin durchführen
7. Bewertungen von Schüler/innen erhalten

## JSON API

Die Anwendung stellt eine einfache JSON-Schnittstelle bereit.

Verfügbare API-Endpunkte:
- http://127.0.0.1:5000/api/users → gibt alle registrierten Nutzer als JSON zurück
