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
if __name__ == '__main__':                      # startet die App nur wenn du sie direkt ausführst
    app.run(debug=True)                         # startet den Webserver, debug=True zeigt Fehlermeldungen direkt im Browser
    