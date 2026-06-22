from flask import Flask, render_template, redirect, url_for, session, flash
from db import db
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm
from models import LehrerProfil, User, Fach, LehrerFach
from flask import request
from datetime import date, time

app = Flask(__name__)

app.secret_key = 'nachhilfe-geheim-123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nachhilfe.db'       # Datenbank-Konfiguration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)                                # Datenbank mit Flask verbinden

@app.route('/')                                 # wenn jemand die Startseite aufruft (/), führe die Funktion darunter aus
def startseite():                               # das ist die Python-Funktion für die Startseite
    return render_template('startseite.html')   # Flask sucht die Datei startseite.html im templates/ Ordner und schickt sie an den Browser

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.passwort, form.passwort.data):
            session['user_id'] = user.id
            session['rolle'] = user.rolle
            session['user_name'] = user.vorname

            if user.rolle == "schueler":
                return redirect(url_for('student_dashboard'))
            elif user.rolle == "lehrer":
                return redirect(url_for('teacher_dashboard'))

        flash("E-Mail oder Passwort ist falsch.")

    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
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
    return render_template('teacher_search.html', lehrer_liste=lehrer_liste)

@app.route('/lehrerprofil/<int:id>')
def teacher_profile(id):
    lehrer = LehrerProfil.query.get(id)
    return render_template('teacher_profile.html', lehrer=lehrer)

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



@app.route('/schueler-dashboard')
def student_dashboard():

    student_name = session.get('user_name', 'Schüler')

    return render_template(
        'student_dashboard.html',
        student_name=student_name
    )

@app.route('/lehrer-dashboard')
def teacher_dashboard():

    teacher_name = session.get('user_name', 'Lehrer')

    return render_template(
        'teacher_dashboard.html',
        teacher_name=teacher_name
    )

@app.route('/meine-buchungen')
def my_bookings():
    return render_template('my_bookings.html')

@app.route('/meine-anfragen')
def my_requests():
    return render_template('my_requests.html')

@app.route('/profil')
def profile():
    user_data = {
        "vorname": session.get("user_name", "Nutzer"),
        "nachname": "",
        "email": "beispiel@test.de",
        "rolle": session.get("rolle", "schueler"),
        "telefon": "Noch nicht angegeben"
    }
    return render_template(
        'profile.html',
        user=user_data
    )

@app.route('/termine')
def teacher_appointments():
    return render_template('teacher_appointments.html')

@app.route('/anfragen')
def teacher_requests():
    return render_template('teacher_requests.html')

@app.route('/nutzungsbedingungen')
def nutzungsbedingungen():
    return render_template('nutzungsbedingungen.html')

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
    
