from app import app
from db import db
from models import User
from werkzeug.security import generate_password_hash


with app.app_context():
    vorhandener_admin = User.query.filter_by(
        email="admin@nachhilfe-connect.de"
    ).first()

    if vorhandener_admin:
        print("Admin-Konto existiert bereits.")
    else:
        admin = User(
            vorname="System",
            nachname="Admin",
            email="admin@nachhilfe-connect.de",
            passwort=generate_password_hash("Admin123!"),
            rolle="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin-Konto wurde erstellt.")
