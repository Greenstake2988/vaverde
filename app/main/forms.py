from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FloatField, SelectField
from wtforms.validators import DataRequired
import app.models as models

class GastoForm(FlaskForm):
    fecha = DateField("Fecha", validators=[DataRequired()])
    concepto = StringField("Concepto", validators=[DataRequired()])
    forma_pago = SelectField("Forma de pago", choices=[(choice.value.upper(), choice.value) for choice in models.FormaPago] , validators=[DataRequired()])
    importe = FloatField("Importe", validators=[DataRequired()])
    folio_factura = StringField("Numero de Factura", validators=[DataRequired()])
    submit = SubmitField('Guardar')

    def reset_form(self):
        self.concepto.data = ""
        self.folio_factura.data = ""
