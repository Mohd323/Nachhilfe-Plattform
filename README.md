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
2. Virtuelle Umgebung erstellen: python -m venv .venv
3. Virtuelle Umgebung aktivieren: .venv\Script\activate
4. Abhängigkeiten installieren: pip isntall -r requirements.txt
5. Testdaten erstellen: python seed_data.py
6. Anwendung starten: python app.py
7. Browser öffnen: https://127.0.0.1:5000

## Happy Path testen

1. Registrierung als Schüler/in durchführen
2. Mit dem erstellten Konto einloggen
3. Lehrer-Suche öffnen
4. Nach Fach oder Preis filtern
5. Lehrerprofil ansehen
6. Buchungsseite aufrufen
7. Dashboard und Profilseite testen

## JSON API

Die Anwendung stellt eine einfache JSON-Schnittstelle bereit.

Verfügbare API-Endpunkte:
- http://127.0.0.1:5000/api/users → gibt alle registrierten Nutzer als JSON zurück
