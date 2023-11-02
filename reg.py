from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    name = StringField("Name: ", validators=[DataRequired()])
    email = EmailField("Email: ", validators=[DataRequired()])
    password = StringField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Enter")