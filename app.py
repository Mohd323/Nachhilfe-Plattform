from flask import Flask, render_template, redirect, url_for, session, flash
from db import db
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from models import LehrerProfil, User, Fach, LehrerFach
from flask import request
from datetime import date, time
from werkzeug.utils import secure_filename
import os
import re
from functools import wraps

app = Flask(__name__)

app.secret_key = 'nachhilfe-geheim-123'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nachhilfe.db'       # Datenbank-Konfiguration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)                                # Datenbank mit Flask verbinden

def admin_required(funktion):
    @wraps(funktion)
    def geschuetzte_funktion(*args, **kwargs):

        if 'user_id' not in session:
            flash("Bitte zuerst einloggen.")
            return redirect(url_for('login'))

        if session.get('rolle') != 'admin':
            flash("Diese Seite ist nur für Administratoren.")
            return redirect(url_for('startseite'))

        return funktion(*args, **kwargs)

    return geschuetzte_funktion

@app.route('/')                                 # wenn jemand die Startseite aufruft (/), führe die Funktion darunter aus
def startseite():                               # das ist die Python-Funktion für die Startseite
    return render_template('startseite.html')   # Flask sucht die Datei startseite.html im templates/ Ordner und schickt sie an den Browser

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        
        user = User.query.filter_by(email=form.email.data).first()
       
        if user and user.ist_gesperrt:
            flash("Dieses Konto wurde gesperrt.")
            return redirect(url_for('login'))

        if user and check_password_hash(user.passwort, form.passwort.data):
            session['user_id'] = user.id
            session['rolle'] = user.rolle
            session['user_name'] = user.vorname

            if user.rolle == "schueler":
                return redirect(url_for('student_dashboard'))
            elif user.rolle == "lehrer":
                return redirect(url_for('teacher_dashboard'))
            elif user.rolle == "admin":
                return redirect(url_for('admin_dashboard'))

        flash("E-Mail oder Passwort ist falsch.")

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        nachweis = request.files.get('nachweis')
        if not nachweis:
             flash("Bitte lade ein Verifizierungsdokument hoch.")
             return redirect(url_for('register'))
        
        dateiname = secure_filename(nachweis.filename)

        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        speicherpfad = os.path.join(
            app.config['UPLOAD_FOLDER'],
            dateiname
        )

        nachweis.save(speicherpfad)

        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("Diese E-Mail ist bereits registriert.")
            return redirect(url_for('register'))

        new_user = User(
            vorname=form.vorname.data,
            nachname=form.nachname.data,
            email=form.email.data,
            passwort=generate_password_hash(form.passwort.data),
            rolle=form.rolle.data,
        )

        db.session.add(new_user)
        db.session.commit()

        if new_user.rolle == "schueler":
            profil = SchülerProfil(
                user_id=new_user.id,
                ausweis_dokument_url=speicherpfad
            )
            db.session.add(profil)

        else:
            profil = LehrerProfil(
                user_id=new_user.id,
                lehrer_typ="tutor",
                unterrichtsart="online",
                stundenpreis=0.0
            )
            db.session.add(profil)
            db.session.flush()  # Erzeugt profil.id, ohne schon endgültig zu speichern

            dokument = Verifizierungsdokument(
                lehrer_profil_id=profil.id,
                dokument_typ="Nachweis",
                datei_url=speicherpfad
            )
            db.session.add(dokument)

        db.session.commit()

        flash("Registrierung erfolgreich. Bitte einloggen.")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/logout')
def logout():
    session.clear()
    flash("Du wurdest ausgeloggt.")
    return redirect(url_for('login'))

@app.route('/impressum')
def impressum():
    return render_template('impressum.html')

@app.route('/datenschutz')
def datenschutz():
    return render_template('datenschutz.html')

@app.route('/suche')
def teacher_search():
    fach_filter = request.args.get('fach')
    unterrichtsart_filter = request.args.get('unterrichtsart')
    preis_filter = request.args.get('preis')
    bewertung_filter = request.args.get('bewertung')
    klassenstufe_filter = request.args.get('klassenstufe')
    verfuegbar_filter = request.args.get('verfuegbar')
    sortierung = request.args.get('sortierung')

    lehrer_liste = LehrerProfil.query.all()

    if fach_filter: 
        lehrer_liste = [
            l for l in lehrer_liste
            if any(lf.fach.name.lower() == fach_filter.lower() for lf in l.faecher)
        ]
    
    if unterrichtsart_filter:
        lehrer_liste = [
            l for l in lehrer_liste
            if l.unterrichtsart == unterrichtsart_filter
        ]
    
    if preis_filter: 
        lehrer_liste = [
            l for l in lehrer_liste
            if l.stundenpreis <= float(preis_filter)
        ]

    if bewertung_filter:
        lehrer_liste = [
            l for l in lehrer_liste
            if l.durchschnittsbewertung and float(l.durchschnittsbewertung) >= float(bewertung_filter)
        ]

    if klassenstufe_filter:
        klassenstufe_zahl = int(klassenstufe_filter)
        gefilterte_liste = []
        for l in lehrer_liste:
            for lf in l.faecher:
                if not lf.klassenstufen:
                    continue
                zahlen = [int(z) for z in re.findall(r'\d+', lf.klassenstufen)]
                if len(zahlen) >= 2 and zahlen[0] <= klassenstufe_zahl <= zahlen[-1]:
                    gefilterte_liste.append(l)
                    break
                elif len(zahlen) == 1 and zahlen[0] == klassenstufe_zahl:
                    gefilterte_liste.append(l)
                    break
        lehrer_liste = gefilterte_liste

    if verfuegbar_filter:
        lehrer_liste = [l for l in lehrer_liste if l.verfuegbar]

    if sortierung == 'bewertung':
        lehrer_liste.sort(key=lambda l: float(l.durchschnittsbewertung or 0), reverse=True)
    elif sortierung == 'preis_aufsteigend':
        lehrer_liste.sort(key=lambda l: l.stundenpreis or 0)
    elif sortierung == 'preis_absteigend':
        lehrer_liste.sort(key=lambda l: l.stundenpreis or 0, reverse=True)

    return render_template(
        'teacher_search.html',
        lehrer_liste=lehrer_liste,
        filter_werte=request.args
    )

@app.route('/lehrerprofil/<int:id>')
def teacher_profile(id):
    lehrer = LehrerProfil.query.get(id)

    bewertungen = []

    for buchung in lehrer.user.buchungen_als_lehrer:
        if buchung.bewertung:
            bewertungen.append(buchung.bewertung)

    if bewertungen:
        durchschnitt = sum(b.sterne for b in bewertungen) / len(bewertungen)
    else:
        durchschnitt = 0

    return render_template(
        'teacher_profile.html',
        lehrer=lehrer,
        bewertungen=bewertungen,
        durchschnitt=durchschnitt
    )

#Buchung
@app.route('/buchung')
def booking():
    flash("Bitte wähle zuerst einen Lehrer aus.")
    return redirect(url_for('teacher_search'))

@app.route('/buchung/<int:lehrer_id>', methods=['GET', 'POST'])
def booking_teacher(lehrer_id):

    if 'user_id' not in session:
        flash("Bitte zuerst einloggen.")
        return redirect(url_for('login'))

    if session.get('rolle') != 'schueler':
        flash("Nur Schüler/innen können eine Buchung erstellen.")
        return redirect(url_for('teacher_search'))

    lehrer = LehrerProfil.query.get(lehrer_id)

    if lehrer is None:
        flash("Lehrer wurde nicht gefunden.")
        return redirect(url_for('teacher_search'))

    if request.method == 'POST':
        fach_id = request.form.get('fach_id')
        datum = request.form.get('datum')
        uhrzeit = request.form.get('uhrzeit')
        dauer_stunden = int(request.form.get('dauer_stunden'))
        unterrichtsart = request.form.get('unterrichtsart')
        zahlungsart = request.form.get('zahlungsart')
        nachricht = request.form.get('nachricht')

        gesamtpreis = lehrer.stundenpreis * dauer_stunden

        neue_buchung = Buchung(
            schüler_id=session['user_id'],
            lehrer_id=lehrer.user_id,
            fach_id=fach_id,
            datum=date.fromisoformat(datum),
            uhrzeit=time.fromisoformat(uhrzeit),
            dauer_stunden=dauer_stunden,
            gesamtpreis=gesamtpreis,
            unterrichtsart=unterrichtsart,
            zahlungsart=zahlungsart,
            status="anfrage",
            nachricht=nachricht
        )
        db.session.add(neue_buchung)
        db.session.commit()

        flash("Buchungsanfrage wurde erfolgreich gesendet.")
        return redirect(url_for('student_dashboard'))

    return render_template(
        'booking.html',
        lehrer=lehrer
    )


#Dashboard
@app.route('/schueler-dashboard')
def student_dashboard():
    if 'user_id' not in session:
        flash("Bitte zuerst einloggen.")
        return redirect(url_for('login'))

    if session.get('rolle') != 'schueler':
        flash("Diese Seite ist nur für Schüler/innen.")
        return redirect(url_for('login'))

    student = User.query.get(session['user_id'])

    buchungen = Buchung.query.filter_by(schüler_id=student.id).all()

    offene_buchungen = [b for b in buchungen if b.status == "anfrage"]
    bestaetigte_buchungen = [b for b in buchungen if b.status == "bestaetigt"]

    return render_template(
        'student_dashboard.html',
        student_name=student.vorname,
        buchungen_anzahl=len(buchungen),
        offene_buchungen_anzahl=len(offene_buchungen),
        bestaetigte_buchungen_anzahl=len(bestaetigte_buchungen),
        letzte_buchungen=buchungen[-3:]
    )


@app.route('/lehrer-dashboard')
def teacher_dashboard():
    if 'user_id' not in session:
        flash("Bitte zuerst einloggen.")
        return redirect(url_for('login'))

    if session.get('rolle') != 'lehrer':
        flash("Diese Seite ist nur für Lehrer/innen.")
        return redirect(url_for('login'))

    teacher = User.query.get(session['user_id'])

    buchungen = Buchung.query.filter_by(lehrer_id=teacher.id).all()

    offene_anfragen = [b for b in buchungen if b.status == "anfrage"]
    bestaetigte_termine = [b for b in buchungen if b.status == "bestaetigt"]
    abgelehnte_anfragen = [b for b in buchungen if b.status == "abgelehnt"]

    return render_template(
        'teacher_dashboard.html',
        teacher_name=teacher.vorname,
        anfragen_anzahl=len(offene_anfragen),
        termine_anzahl=len(bestaetigte_termine),
        abgelehnte_anzahl=len(abgelehnte_anfragen),
        letzte_anfragen=offene_anfragen[-3:]
    )
    

@app.route('/lehrerprofil-erstellen', methods=['GET', 'POST'])
def lehrerprofil_erstellen():
    if 'user_id' not in session or session.get('rolle') != 'lehrer':
        flash("Bitte als Lehrer einloggen.")
        return redirect(url_for('login'))

    user_id = session['user_id']
    bestehendes_profil = LehrerProfil.query.filter_by(user_id=user_id).first()

    if bestehendes_profil:
        flash("Du hast bereits ein Lehrerprofil.")
        return redirect(url_for('teacher_dashboard'))

    if request.method == 'POST':
        lehrer_typ = request.form.get('lehrer_typ')
        beschreibung = request.form.get('beschreibung')
        unterrichtsart = request.form.get('unterrichtsart')
        stundenpreis = float(request.form.get('stundenpreis'))
        ort = request.form.get('ort')
        fach_id = request.form.get('fach_id')

        neues_profil = LehrerProfil(
            user_id=user_id,
            lehrer_typ=lehrer_typ,
            beschreibung=beschreibung,
            unterrichtsart=unterrichtsart,
            stundenpreis=stundenpreis,
            ort=ort
        )
        db.session.add(neues_profil)
        db.session.commit()

        neue_verknuepfung = LehrerFach(
            lehrer_profil_id=neues_profil.id,
            fach_id=fach_id
        )
        db.session.add(neue_verknuepfung)
        db.session.commit()

        flash("Dein Lehrerprofil wurde erfolgreich erstellt!")
        return redirect(url_for('teacher_dashboard'))

    alle_faecher = Fach.query.all()
    return render_template('lehrerprofil_erstellen.html', faecher=alle_faecher)

@app.route('/meine-buchungen')
def my_bookings():
    if 'user_id' not in session or session.get('rolle') != 'schueler':
        flash("Bitte als Schüler einloggen.")
        return redirect(url_for('login'))
    
    schueler_id = session['user_id']
    buchungen = Buchung.query.filter_by(schüler_id=schueler_id).all()

    return render_template('my_bookings.html', buchungen=buchungen)

@app.route('/bewertung/<int:buchung_id>', methods=['GET', 'POST'])
def bewertung_abgeben(buchung_id):
    if 'user_id' not in session or session.get('rolle') != 'schueler':
        flash("Bitte als Schüler einloggen.")
        return redirect(url_for('login'))

    buchung = Buchung.query.get(buchung_id)

    if buchung is None:
        flash("Buchung wurde nicht gefunden.")
        return redirect(url_for('my_bookings'))

    bereits_bewertet = Bewertung.query.filter_by(buchung_id=buchung_id).first()
    if bereits_bewertet:
        flash("Diese Buchung wurde bereits bewertet.")
        return redirect(url_for('my_bookings'))

    if request.method == 'POST':
        sterne = int(request.form.get('sterne'))
        kommentar = request.form.get('kommentar')

        neue_bewertung = Bewertung(
            buchung_id=buchung.id,
            bewerter_id=session['user_id'],
            bewertet_id=buchung.lehrer_id,
            sterne=sterne,
            kommentar=kommentar
        )
        db.session.add(neue_bewertung)
        db.session.commit()

        flash("Vielen Dank für deine Bewertung!")
        return redirect(url_for('my_bookings'))

    return render_template('bewertung.html', buchung=buchung)

@app.route('/meine-anfragen')
def my_requests():
    return render_template('my_requests.html')

# profil
@app.route('/profil')
def profile():
    if 'user_id' not in session:
        flash("Bitte zuerst einloggen.")
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if user is None:
        flash("Nutzer wurde nicht gefunden.")
        return redirect(url_for('login'))

    return render_template(
        'profile.html',
        user=user
    )

@app.route('/profil/bearbeiten', methods=['GET', 'POST'])
def profile_edit():
    if 'user_id' not in session:
        flash("Bitte zuerst einloggen.")
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if user is None:
        flash("Nutzer wurde nicht gefunden.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        neue_email = request.form.get('email')
        neue_telefonnummer = request.form.get('telefon')

        aktuelles_passwort = request.form.get('aktuelles_passwort')
        neues_passwort = request.form.get('neues_passwort')

        if neue_email:
            user.email = neue_email

        user.telefon = neue_telefonnummer

        # Passwort ändern
        if neues_passwort:

            if not check_password_hash(user.passwort, aktuelles_passwort):
                flash("Aktuelles Passwort ist falsch.")
                return redirect(url_for('profile_edit'))

            user.passwort = generate_password_hash(neues_passwort)

        db.session.commit()

        flash("Profil wurde erfolgreich aktualisiert.")
        return redirect(url_for('profile'))

    return render_template('profile_edit.html', user=user)
    

@app.route('/termine')
def teacher_appointments():
    if 'user_id' not in session or session.get('rolle') != 'lehrer':
        flash("Bitte als Lehrer einloggen.")
        return redirect(url_for('login'))

    lehrer_user_id = session['user_id']

    termine = Buchung.query.filter_by(
        lehrer_id=lehrer_user_id,
        status="bestaetigt"
    ).all()

    return render_template('teacher_appointments.html', termine=termine)

@app.route('/anfragen')
def teacher_requests():
    if 'user_id' not in session or session.get('rolle') != 'lehrer':
        flash("Bitte als Lehrer einloggen.")
        return redirect(url_for('login'))

    lehrer_user_id = session['user_id']
    anfragen = Buchung.query.filter_by(lehrer_id=lehrer_user_id, status="anfrage").all()

    return render_template('teacher_requests.html', anfragen=anfragen) 

@app.route('/anfragen/<int:buchung_id>/<aktion>')
def bearbeite_anfrage(buchung_id, aktion):
    if 'user_id' not in session or session.get('rolle') != 'lehrer':
        flash("Bitte als Lehrer einloggen.")
        return redirect(url_for('login'))

    buchung = Buchung.query.get(buchung_id)

    if buchung is None:
        flash("Buchung wurde nicht gefunden.")
        return redirect(url_for('teacher_requests'))

    if aktion == 'akzeptieren':
        buchung.status = 'bestaetigt'
        flash("Buchung wurde akzeptiert.")
    elif aktion == 'ablehnen':
        buchung.status = 'abgelehnt'
        flash("Buchung wurde abgelehnt.")

    db.session.commit()
    return redirect(url_for('teacher_requests'))

@app.route('/nachhilfe-anbieten', methods=['GET', 'POST'])
def nachhilfe_anbieten():
    if 'user_id' not in session:
        flash("Bitte zuerst einloggen.")
        return redirect(url_for('login'))

    if session.get('rolle') != 'lehrer':
        flash("Nur Lehrer/innen können Nachhilfe anbieten.")
        return redirect(url_for('student_dashboard'))

    user_id = session['user_id']

    lehrer_profil = LehrerProfil.query.filter_by(user_id=user_id).first()

    if request.method == 'POST':
        lehrer_typ = request.form.get('lehrer_typ')
        fach_name = request.form.get('fach')
        klassenstufen = request.form.get('klassenstufen')
        beschreibung = request.form.get('beschreibung')
        unterrichtsart = request.form.get('unterrichtsart')
        stundenpreis = float(request.form.get('stundenpreis'))
        ort = request.form.get('ort')

         # Neues Profil anlegen
        if lehrer_profil is None:

            lehrer_profil = LehrerProfil(
                user_id=user_id,
                lehrer_typ=lehrer_typ,
                beschreibung=beschreibung,
                unterrichtsart=unterrichtsart,
                stundenpreis=stundenpreis,
                ort=ort,
                verfuegbar=True
            )

            db.session.add(lehrer_profil)
            db.session.commit()

        # Vorhandenes Profil aktualisieren
        else:

            lehrer_profil.lehrer_typ = lehrer_typ
            lehrer_profil.beschreibung = beschreibung
            lehrer_profil.unterrichtsart = unterrichtsart
            lehrer_profil.stundenpreis = stundenpreis
            lehrer_profil.ort = ort

            db.session.commit()

        # Fach suchen oder anlegen
        fach = Fach.query.filter_by(name=fach_name).first()

        if fach is None:
            fach = Fach(name=fach_name)

            db.session.add(fach)
            db.session.commit()

        # Vorhandene Fach-Zuordnung prüfen
        vorhandenes_fach = LehrerFach.query.filter_by(
            lehrer_profil_id=lehrer_profil.id
        ).first()

        # Neues Fach speichern
        if vorhandenes_fach is None:

            neues_fach = LehrerFach(
                lehrer_profil_id=lehrer_profil.id,
                fach_id=fach.id,
                klassenstufen=klassenstufen
            )

            db.session.add(neues_fach)

        # Fach aktualisieren
        else:

            vorhandenes_fach.fach_id = fach.id
            vorhandenes_fach.klassenstufen = klassenstufen

        db.session.commit()

        flash("Dein Nachhilfeangebot wurde gespeichert.")
        return redirect(url_for('teacher_dashboard'))

    return render_template(
        'nachhilfe_anbieten.html',
        lehrer_profil=lehrer_profil
    )

@app.route('/nutzungsbedingungen')
def nutzungsbedingungen():
    return render_template('nutzungsbedingungen.html')

#ADMIN
@app.route('/admin')
@admin_required
def admin_dashboard():

    offene_dokumente = Verifizierungsdokument.query.filter_by(
        status="ausstehend"
    ).count()

    offene_meldungen = Meldung.query.filter_by(
        status="offen"
    ).count()

    nutzer_anzahl = User.query.count()

    return render_template(
        'admin_dashboard.html',
        offene_dokumente=offene_dokumente,
        offene_meldungen=offene_meldungen,
        nutzer_anzahl=nutzer_anzahl
    )


@app.route('/admin/dokumente')
@admin_required
def admin_dokumente():

    dokumente = Verifizierungsdokument.query.order_by(
        Verifizierungsdokument.hochgeladen_am.desc()
    ).all()

    return render_template(
        'admin_dokumente.html',
        dokumente=dokumente
    )


@app.route('/admin/dokument/<int:dokument_id>/<aktion>', methods=['POST'])
@admin_required
def admin_dokument_bearbeiten(dokument_id, aktion):

    dokument = Verifizierungsdokument.query.get(dokument_id)

    if dokument is None:
        flash("Dokument wurde nicht gefunden.")
        return redirect(url_for('admin_dokumente'))

    if aktion == "akzeptieren":
        dokument.status = "verifiziert"

        lehrer_profil = LehrerProfil.query.get(
            dokument.lehrer_profil_id
        )

        if lehrer_profil:
            lehrer_profil.verifizierungs_status = "verifiziert"

        flash("Das Dokument wurde akzeptiert.")

    elif aktion == "ablehnen":

        dokument.status = "abgelehnt"

        lehrer_profil = LehrerProfil.query.get(
            dokument.lehrer_profil_id
        )

        if lehrer_profil:
            lehrer_profil.verifizierungs_status = "abgelehnt"

        flash("Das Dokument wurde abgelehnt.")

    else:
        flash("Ungültige Aktion.")

    db.session.commit()

    return redirect(url_for('admin_dokumente'))


@app.route('/admin/meldungen')
@admin_required
def admin_meldungen():

    meldungen = Meldung.query.order_by(
        Meldung.erstellt_am.desc()
    ).all()

    return render_template(
        'admin_meldungen.html',
        meldungen=meldungen
    )


@app.route('/admin/meldung/<int:meldung_id>', methods=['POST'])
@admin_required
def admin_meldung_erledigen(meldung_id):

    meldung = Meldung.query.get(meldung_id)

    if meldung is None:
        flash("Meldung wurde nicht gefunden.")
        return redirect(url_for('admin_meldungen'))

    meldung.status = "erledigt"

    db.session.commit()

    flash("Meldung wurde als erledigt markiert.")

    return redirect(url_for('admin_meldungen'))


@app.route('/admin/nutzer/<int:user_id>/sperren', methods=['POST'])
@admin_required
def admin_nutzer_sperren(user_id):

    nutzer = User.query.get(user_id)

    if nutzer is None:
        flash("Nutzer wurde nicht gefunden.")
        return redirect(url_for('admin_meldungen'))

    if nutzer.rolle == "admin":
        flash("Ein Administrator kann nicht gesperrt werden.")
        return redirect(url_for('admin_meldungen'))

    nutzer.ist_gesperrt = True

    db.session.commit()

    flash(
        f"{nutzer.vorname} {nutzer.nachname} wurde gesperrt."
    )

    return redirect(url_for('admin_meldungen'))


        @app.route('/admin/nutzer/<int:user_id>/entsperren', methods=['POST'])
        @admin_required
        def admin_nutzer_entsperren(user_id):
        
            nutzer = User.query.get(user_id)
        
            if nutzer is None:
                flash("Nutzer wurde nicht gefunden.")
                return redirect(url_for('admin_meldungen'))
        
            nutzer.ist_gesperrt = False
            db.session.commit()
        
            flash(
                f"{nutzer.vorname} {nutzer.nachname} wurde entsperrt."
            )
        
            return redirect(url_for('admin_meldungen'))


with app.app_context():                         # Tabellen automatisch erstellen
    db.create_all()

# JSON APIs
@app.route("/api/users")
def api_users():
    users = User.query.all()

    return {
        "users": [
            {
                "id": user.id,
                "vorname": user.vorname,
                "nachname": user.nachname,
                "email": user.email,
                "rolle": user.rolle,
                "telefon": user.telefon
            }
            for user in users
        ]
    }



if __name__ == '__main__':                      # startet die App nur wenn du sie direkt ausführst
    app.run(debug=True)                         # startet den Webserver, debug=True zeigt Fehlermeldungen direkt im Browser
    
