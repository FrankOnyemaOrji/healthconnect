from flask import Blueprint, render_template, redirect, url_for
import requests
from flask import request, flash
from flask_login import login_required, current_user
from . import db

from .models.base_model import Appointment

views = Blueprint('views', __name__)


@views.route('/')
def index():  # put application's code here
    return render_template('index.html')


@views.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html")


@views.route('/resource')
def resource():
    # Render the HTML template with the health topics
    return render_template("resources.html")


def is_appointment_date_available(appointment_date):
    appointment_date_available = Appointment.query.filter_by(appointment_date=appointment_date).first()
    for appointment_date_slot in appointment_date_available:
        if appointment_date_available == appointment_date:
            flash('Appointment date is not available.', category='error')
            return False
        else:
            return True


def is_appointment_time_available(appointment_time):
    appointment_time_available = Appointment.query.filter_by(appointment_time=appointment_time).first()
    for appointment_time_slot in appointment_time_available:
        if appointment_time_available == appointment_time:
            flash('Appointment time is not available.', category='error')
            return False
        else:
            return True


@views.route('/appointment', methods=['GET', 'POST'])
@login_required
def appointment():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        note = request.form.get('note')
        phone_number = request.form.get('phone_number')
        appointment_date = request.form.get('appointment_date')
        appointment_time = request.form.get('appointment_time')
        hospital_name = request.form.get('hospital_name')

        if not full_name:
            flash('Full name is required.', category='error')
        elif not hospital_name:
            flash('Hospital name is required.', category='error')
        elif not note:
            flash('Note is required.', category='error')
        elif not phone_number:
            flash('Phone number is required.', category='error')
        elif not appointment_date:
            if not is_appointment_date_available(appointment_date):
                return redirect(url_for('views.appointment'))
        elif not appointment_time:
            if not is_appointment_time_available(appointment_time):
                return redirect(url_for('views.appointment'))

        appointment_id = Appointment(full_name=full_name, note=note, phone_number=phone_number,
                                     appointment_date=appointment_date, appointment_time=appointment_time,hospital_name=hospital_name,
                                     student=current_user)
        db.session.add(appointment_id)
        db.session.commit()
        flash('Appointment created successfully.')
        return redirect(url_for('views.dashboard'))
    return render_template('appointment.html', user=current_user)


@views.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@views.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
