from flask import Flask, render_template, redirect, url_for, session 

app = Flask(__name__)

app.secret_key = 'nachhilfe-geheim-123'

@app.route('/')                                 # wenn jemand die Startseite aufruft (/), führe die Funktion darunter aus
def startseite():                               # das ist die Python-Funktion für die Startseite
    return render_template('startseite.html')   # Flask sucht die Datei startseite.html im templates/ Ordner und schickt sie an den Browser

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

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
    return render_template('booking.html')

@app.route('/schueler-dashboard')
def student_dashboard():
    return render_template('student_dashboard.html')

@app.route('/lehrer-dashboard')
def teacher_dashboard():
    return render_template('teacher_dashboard.html')

@app.route('/meine-buchungen')
def my_bookings():
    return render_template('my_bookings.html')

@app.route('/meine-anfragen')
def my_requests():
    return render_template('my_requests.html')

@app.route('/profil')
def profile():
    return render_template('profile.html')

@app.route('/termine')
def teacher_appointments():
    return render_template('teacher_appointments.html')

@app.route('/anfragen')
def teacher_requests():
    return render_template('teacher_requests.html')

if __name__ == '__main__':                      # startet die App nur wenn du sie direkt ausführst
    app.run(debug=True)                         # startet den Webserver, debug=True zeigt Fehlermeldungen direkt im Browser