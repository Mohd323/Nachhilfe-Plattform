from flask import Flask, render_template, redirect, url_for, session, flash
from db import db
from models import *
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegisterForm, LoginForm

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
    return render_template('teacher_search.html')

@app.route('/lehrerprofil')
def teacher_profile():
    return render_template('teacher_profile.html')

@app.route('/buchung')
def booking():
    teacher_name = "Nachhilfelehrer"

    return render_template(
        'booking.html',
        teacher_name=teacher_name
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

if __name__ == '__main__':                      # startet die App nur wenn du sie direkt ausführst
    app.run(debug=True)                         # startet den Webserver, debug=True zeigt Fehlermeldungen direkt im Browser
    
