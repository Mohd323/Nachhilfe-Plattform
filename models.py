from db import db

#Benutzer
class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String(100), nullable=False)
    nachname = db.Column(db.String(100), nullable=False)
    rolle = db.Column(db.String(20), nullable=False)                   #Schüler / lehrer
    telefon = db.Column(db.String(30), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    passwort = db.Column(db.String(255), nullable=False)


#Schülerprofil
class SchülerProfil(db.Model):
    __tablename__ = "schüler_profile"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    klasse = db.Column(db.String(50))
    ausweis_dokument_url = db.Column(db.Text, nullable=True)
    verifizierungs_status = db.Column(db.String(30), nullable=False, default="ausstehend")


# Lehrerprofil
class LehrerProfil(db.Model):
    __tablename__ = "lehrer_profile"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    lehrer_typ = db.Column(db.String(30), nullable=False)                        #student / lehrer / tutor
    beschreibung = db.Column(db.Text)
    erfahrung_jahre = db.Column(db.Integer, nullable=True)
    unterrichtsart = db.Column(db.String(30), nullable=False)                    #online / vor_ort / beides
    stundenpreis = db.Column(db.Float)
    durchschnittsbewertung = db.Column(db.Numeric(3, 2), nullable=True, default=0)
    bewertungsanzahl = db.Column(db.Integer, nullable=False, default=0)
    verfuegbar = db.Column(db.Boolean, nullable=False, default=True)
    ort = db.Column(db.String(200), nullable=True)
    verifizierungs_status = db.Column(db.String(30), nullable=False, default="ausstehend")

