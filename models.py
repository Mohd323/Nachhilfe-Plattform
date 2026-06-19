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


class Fach(db.Model):
    __tablename__ = "fach"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)


class LehrerFach(db.Model):
    __tablename__ = "lehrer_fach"

    id = db.Column(db.Integer, primary_key=True)
    lehrer_profil_id = db.Column(db.Integer, db.ForeignKey("lehrer_profil.id"), nullable=False)
    fach_id = db.Column(db.Integer, db.ForeignKey("fach.id"), nullable=False)
    klassenstufen = db.Column(db.String(50), nullable=True)
    

class Verfügbarkeit(db.Model):
    __tablename__ = "verfügbarkeit"

    id = db.Column(db.Integer, primary_key=True)
    lehrer_profil_id = db.Column(db.Integer, db.ForeignKey("lehrer_profil.id"), nullable=False)
    wochentag = db.Column(db.String(20), nullable=False)
    von_uhrzeit = db.Column(db.Time, nullable=False)
    bis_uhrzeit = db.Column(db.Time, nullable=False)


class Verifizierungsdokument(db.Model):
    __tablename__ = "verifizierungsdokument"

    id = db.Column(db.Integer, primary_key=True)
    lehrer_profil_id = db.Column(db.Integer, db.ForeignKey("lehrer_profil.id"), nullable=False)
    dokument_typ = db.Column(db.String(50), nullable=False)
    datei_url = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), nullable=False, default="ausstehend")
    hochgeladen_am = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    admin_notiz = db.Column(db.Text, nullable=True)


class Buchung(db.Model):
    __tablename__ = "buchung"

    id = db.Column(db.Integer, primary_key=True)
    schüler_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    lehrer_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    fach_id = db.Column(db.Integer, db.ForeignKey("fach.id"), nullable=False)
    datum = db.Column(db.Date, nullable=False)
    uhrzeit = db.Column(db.Time, nullable=False)
    dauer_stunden = db.Column(db.Integer, nullable=False)
    gesamtpreis = db.Column(db.Numeric(8, 2), nullable=False)
    unterrichtsart = db.Column(db.String(30), nullable=False)
    zahlungsart = db.Column(db.String(30), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="anfrage")
    nachricht = db.Column(db.Text, nullable=True)
    erstellt_am = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Bewertung(db.Model):
    __tablename__ = "bewertung"

    id = db.Column(db.Integer, primary_key=True)
    buchung_id = db.Column(db.Integer, db.ForeignKey("buchung.id"), unique=True, nullable=False)
    bewerter_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    bewertet_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    sterne = db.Column(db.Integer, nullable=False)
    kommentar = db.Column(db.Text, nullable=True)
    erstellt_am = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Meldung(db.Model):
    __tablename__ = "meldung"

    id = db.Column(db.Integer, primary_key=True)
    melder_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    gemeldeter_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    grund = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(30), nullable=False, default="offen")
    erstellt_am = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
