from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class ContactForm(FlaskForm):
    """
    Register form for new users
    """
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email()])
    arrival_date = StringField(validators=[DataRequired()])
    departure_date = StringField(validators=[DataRequired()])
    send_message = SubmitField("SEND MESSAGE")