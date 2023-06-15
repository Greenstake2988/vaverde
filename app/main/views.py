from flask import render_template, flash
from .. import db
from ..models import Gasto
from . import main
from .forms import GastoForm
from flask_login import login_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/usuario/<string:name>')
def usuario(name):
    return render_template('usuario.html', name=name)

@main.route('/gastos', methods=['GET','POST'])
@login_required
def gastos():
    form = GastoForm()
    if form.validate_on_submit():
        gasto = Gasto(fecha=form.fecha.data, concepto=form.concepto.data, forma_pago=form.forma_pago.data, importe=form.importe.data, folio_factura=form.folio_factura.data)
        db.session.add(gasto)
        try:
            db.session.commit()
            flash('Gasto Ingresado con Éxito!')
        except Exception as e:
            db.session.rollback()
            flash('Ocurrió un error al guardar el gasto.')
        form.reset_form()
        #return redirect(url_for('index'))
    return render_template("form_gasto.html", form=form)

@main.route('/gastos/<id>', methods=['GET','POST'])
def get_gasto(id):
    gasto = Gasto.query.filter_by(id=id).first()
    return render_template("gasto.html", gasto=gasto)