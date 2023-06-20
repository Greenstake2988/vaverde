from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, SelectField, TextAreaField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp
from ..models import Role, User, FormaPago

class GastoForm(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired()])
    concepto = StringField("Concepto", validators=[DataRequired()])
    forma_pago = SelectField("Forma de pago", choices=[(choice.value.upper(), choice.value) for choice in FormaPago] , validators=[DataRequired()])
    importe = FloatField("Importe", validators=[DataRequired()])
    folio_factura = StringField("Numero de Factura", validators=[DataRequired()])
    submit = SubmitField('Guardar')

    def reset_form(self):
        self.concepto.data = ""
        self.folio_factura.data = ""

class EditProfileForm(FlaskForm):
    name = StringField('Nombre Real', validators=[Length(0,64)])
    location = StringField('Ubicacion', validators=[Length(0,64)])
    about_me = TextAreaField('Acerca de mí')
    submit = SubmitField('Guardar')

class EditProfileAdminForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1,64),
                                                    Regexp('^[A-Za-z][A-Za-z0-9.*$]', 0,
                                                           'Usernames solo pueden contener letras, numeros, puntos o guiones bajos') ])
    confirmed = BooleanField('Confirmado')
    role = SelectField('Role', coerce=int)
    name = StringField('Nombre Real', validators=[Length(0,64)])
    location = StringField('Ubicacion', validators=[Length(0,64)])
    about_me = TextAreaField('Sobre mi') 
    submit = SubmitField('Guardar')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                    User.query.filter_by(email=field.data).first():
            raise ValidationError('El email esta registrado.')
    
    def validate_username(self, field):
        if field.data != self.user.username and \
                    User.query.filter_by(username=field.data).first():
            raise ValidationError('El username ya esta registrado.')