from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Mantenme Logeado')
    submit = SubmitField('Logearse')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    username= StringField('Nombre de Usuario', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Nombres de usuario solo pueden contener letras, numeros , puntos o '
               'guiones bajos.')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Las contraseñas deben coincidir.')])
    password2 = PasswordField('Confirmar contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrarse')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
          raise ValidationError('El correo electronico ya esta en uso.')
    
    def validate_username(sel, field):
        if User.query.filter_by(username=field.data).first():
          raise ValidationError('El nombre de usuario ya esta en uso.')
