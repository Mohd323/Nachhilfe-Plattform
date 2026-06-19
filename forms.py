from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    vorname = StringField("Vorname", validators=[DataRequired()])
    nachname = StringField("Nachname", validators=[DataRequired()])
    email = StringField("E-Mail", validators=[DataRequired(), Email()])
    passwort = PasswordField("Passwort", validators=[DataRequired(), Length(min=6)])
    rolle = SelectField(
        "Rolle",
        choices=[("schueler", "Schüler/in"), ("lehrer", "Lehrer/in")],
        validators=[DataRequired()]
    )
    submit = SubmitField("Registrieren")

class LoginForm(FlaskForm):
    email = StringField("E-Mail", validators=[DataRequired(), Email()])
    passwort = PasswordField("Passwort", validators=[DataRequired()])
    submit = SubmitField("Einloggen")
