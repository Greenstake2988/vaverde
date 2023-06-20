from flask import render_template, flash, redirect, url_for
from .. import db
from ..models import Gasto, User, Role
from . import main
from .forms import GastoForm, EditProfileForm, EditProfileAdminForm
from flask_login import login_required, current_user
from ..decorators import admin_required

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/user/<string:username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

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

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Tu perfil ah sido Actualizado.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)

@main.route('/edit-profile/<int:id>', methods=['GET','POST'])
@login_required
@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        db.session.commit()
        flash('El perfil ah sido actualizado.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)
    