from app import app
from db import db
from models import User, SchülerProfil, LehrerProfil, Fach, LehrerFach, Buchung, Bewertung
from datetime import date, time
from werkzeug.security import generate_password_hash

with app.app_context():

    # 2 Schüler erstellen
    schueler1 = User(vorname="Max", nachname="Mustermann", rolle="schueler", email="max@test.de", passwort=generate_password_hash("test123"))   # Python Objekt erstellen mit den Werten, die in die Tabelle User sollen
    schueler2 = User(vorname="Anna", nachname="Schmidt", rolle="schueler", email="anna@test.de", passwort=generate_password_hash("test123"))

    # 2 Lehrer erstellen
    lehrer1 = User(vorname="Ali", nachname="Tyson", rolle="lehrer", email="ali@test.de", passwort=generate_password_hash("test123"))
    lehrer2 = User(vorname="Cristiano", nachname="Ronaldo", rolle="lehrer", email="cristiano@test.de", passwort=generate_password_hash("test123"))

    db.session.add_all([schueler1, schueler2, lehrer1, lehrer2])    # ich sage damit der Datenbank "merk dir diese 4 neuen Einträge"
    db.session.commit()                                             # speichert die Einträge wirklich in nachhilfe.db, ohne commit() passiert nichts
                                                                    # wir brauchen die IDs von schueler1, lehrer1 usw. für die nächsten Tabellen (SchülerProfil braucht (user_id). 
                                                                    # erst nach commit() bekommen die Objekte ihre echte ID aus der Datenbank.

                                                                    
    # Profile für die Schüler
    profil_schueler1 = SchülerProfil(user_id=schueler1.id, klasse="10a")
    profil_schueler2 = SchülerProfil(user_id=schueler2.id, klasse="11b")

    # Profile für die Lehrer
    profil_lehrer1 = LehrerProfil(user_id=lehrer1.id, lehrer_typ="lehrer", beschreibung="Erfahrene Mathelehrer", unterrichtsart="online", stundenpreis=25.0, ort="Berlin")
    profil_lehrer2 = LehrerProfil(user_id=lehrer2.id, lehrer_typ="student", beschreibung="Student, gibt Nachhilfe in Physik", unterrichtsart="beides", stundenpreis=18.0, ort="Berlin")

    db.session.add_all([profil_schueler1, profil_schueler2, profil_lehrer1, profil_lehrer2])
    db.session.commit() 
                                                                # user_id=schueler1.id - nach dem commit() hat schueler1 jetzt eine echte ID aus der Datenbank. 
                                                                # Diese ID benutzten wir um das Profil mit dem richtigen User zu verknüpfen
                                                                # Das ist der FK in Aktion - SchülerProfil "weiß" durch user_id zu welchem User er gehört.


    # 3 Fächer erstellen
    mathe = Fach(name="Mathe")
    physik = Fach(name="Physik")
    chemie = Fach(name="Chemie")

    db.session.add_all([mathe, physik, chemie])
    db.session.commit()

    # Verküpfung: welcher Lehrer unterrichtet welches Fach
    lehrer1_fach = LehrerFach(lehrer_profil_id=profil_lehrer1.id, fach_id=mathe.id, klassenstufen="9-12")
    lehrer2_fach = LehrerFach(lehrer_profil_id=profil_lehrer2.id, fach_id=physik.id, klassenstufen="9-13")

    db.session.add_all([lehrer1_fach, lehrer2_fach])
    db.session.commit()
                                                            # Fach(name="Mathe") - einfacher Eintrag, kein FK nötig
                                                            # LehrerFach ist eine Verknüpfungstabelle - sie verbindet einen Lehrer mit einem Fach
                                                            # lehrer_profil_id=profil_lehrer1.id heißt "Lehrer 1s Profil" und fach_id=mathe.id heißt "unterrichtet Mathe"

    # 2 Buchungen
    buchung1 = Buchung(
        schüler_id=schueler1.id,
        lehrer_id=lehrer1.id,
        fach_id=mathe.id,
        datum=date(2026, 6, 25),
        uhrzeit=time(14, 0),
        dauer_stunden=2,
        gesamtpreis=50.0,
        unterrichtsart="online",
        zahlungsart="paypal",
        status="bestaetigt",
        nachricht="Bitte Algebra wiederholen",
    )

    buchung2 = Buchung(
        schüler_id=schueler2.id,
        lehrer_id=lehrer2.id,
        fach_id=physik.id,
        datum=date(2026, 6, 27),
        uhrzeit=time(16, 0),
        dauer_stunden=1,
        gesamtpreis=18.0,
        unterrichtsart="vor_ort",
        zahlungsart="ueberweisung",
        status="anfrage",
        nachricht="Erstes Mal Nachhilfe",
    )

    db.session.add_all([buchung1, buchung2])
    db.session.commit()
                                                



    # 1 Bewertung
    bewertung1 = Bewertung(
        buchung_id=buchung1.id,
        bewerter_id=schueler1.id,
        bewertet_id=lehrer1.id,
        sterne=5,
        kommentar="Super erklärt, hat mir sehr geholfen!"
    )

    db.session.add(bewertung1)                      # bei nur einem Eintrag benutzt man add() statt add_all()
    db.session.commit()

  # 2 weitere Schüler
    schueler3 = User(vorname="Lena", nachname="Hoffmann", rolle="schueler", email="lena@test.de", passwort=generate_password_hash("test123"))
    schueler4 = User(vorname="David", nachname="Schulz", rolle="schueler", email="david@test.de", passwort=generate_password_hash("test123"))

    # 2 weitere Lehrer
    lehrer3 = User(vorname="Sara", nachname="Klein", rolle="lehrer", email="sara@test.de", passwort=generate_password_hash("test123"))
    lehrer4 = User(vorname="Tom", nachname="Fischer", rolle="lehrer", email="tom2@test.de", passwort=generate_password_hash("test123"))

    db.session.add_all([schueler3, schueler4, lehrer3, lehrer4])
    db.session.commit()

    # Profile für die neuen Schüler
    profil_schueler3 = SchülerProfil(user_id=schueler3.id, klasse="12a")
    profil_schueler4 = SchülerProfil(user_id=schueler4.id, klasse="10c")

    # Profile für die neuen Lehrer
    profil_lehrer3 = LehrerProfil(user_id=lehrer3.id, lehrer_typ="lehrer", beschreibung="Chemielehrerin mit langjähriger Erfahrung", unterrichtsart="vor_ort", stundenpreis=22.0, ort="Berlin")
    profil_lehrer4 = LehrerProfil(user_id=lehrer4.id, lehrer_typ="tutor", beschreibung="Tutor für Mathe und Physik", unterrichtsart="online", stundenpreis=20.0, ort="Berlin")

    db.session.add_all([profil_schueler3, profil_schueler4, profil_lehrer3, profil_lehrer4])
    db.session.commit()

    # Fach-Verknüpfungen für die neuen Lehrer
    lehrer3_fach = LehrerFach(lehrer_profil_id=profil_lehrer3.id, fach_id=chemie.id, klassenstufen="9-13")
    lehrer4_fach_mathe = LehrerFach(lehrer_profil_id=profil_lehrer4.id, fach_id=mathe.id, klassenstufen="9-12")
    lehrer4_fach_physik = LehrerFach(lehrer_profil_id=profil_lehrer4.id, fach_id=physik.id, klassenstufen="9-12")

    db.session.add_all([lehrer3_fach, lehrer4_fach_mathe, lehrer4_fach_physik])
    db.session.commit()

    print("Testdaten erfolgreich erstellt!")      # zeigt mir am ende eine Bestätigung im Terminal


