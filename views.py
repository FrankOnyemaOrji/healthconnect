from flask import Blueprint, render_template, redirect, url_for
import requests
from flask import request, flash
from flask_login import login_required
from . import db

from .models.base_model import Appointment

views = Blueprint('views', __name__)


@views.route('/')
def index():  # put application's code here
    return render_template('index.html')


@views.route('/dashboard')
@login_required
def dashboard():
    pass


@views.route('/resources')
@login_required
def resources():
    pass


@views.route('/resource')
def resource():
    # Get the health topics from the MyHealth-finder API
    response = requests.get("https://api.myhealthfinder.gov/v2/topics")
    topics = response.json()

    # Render the HTML template with the health topics
    return render_template("resources.html", topics=topics)


# Appointment Routes
hospital_name = [
    'Ubuzima Polyclinic',
    'Ubuzima Polyclinic',
    'Polyclinic saint Jean',
    'Polyfam',
    'UR-CMHS BD'
    'Polyclinique medico sociale'
    'olyclinique la medicale Musanze'
    'Polyclinique la medicale Kigali'
    'Polyclinique la medicale Rubavu'
    "Polyclinique de l'etoile"
    'Polyclinic du plateau'
    'Croix du sud hospital'
    'Peace Pololyclinic'
    'Polyclinic du carrefour'
    'Inkurunziza Orthopedic Hospital'
    'Glamerc Polyclinic'
    'Polyclinique La medicale Huye'
    'Wiwo Specialized Hospital'
    'Beatrice Polyclinic'
    'MBC HOSPITAL'
    'Salus Polyclinic'
]

time_slots = [
    '6:00 AM',
    '6:30 AM',
    '7:00 AM',
    '7:30 AM',
    '8:00 AM',
    '8:30 AM',
    '9:00 AM',
    '9:30 AM',
    '10:00 AM',
    '10:30 AM',
    '11:00 AM',
    '11:30 AM',
    '12:00 PM',
    '12:30 PM',
    '1:00 PM',
    '1:30 PM',
    '2:00 PM',
    '2:30 PM',
    '3:00 PM',
    '3:30 PM',
    '4:00 PM',
    '4:30 PM',
    '5:00 PM',
    '5:30 PM',
    '6:00 PM',
    '6:30 PM',
    '7:00 PM',
    '7:30 PM',
    '8:00 PM',
    '8:30 PM',
    '9:00 PM',
    '9:30 PM',
    '10:00 PM',
    '10:30 PM',
    '11:00 PM',
]

date_available = [
    '2023-08-01',
    '2023-08-02',
    '2023-08-03',
    '2023-08-04',
    '2023-08-05',
    '2023-08-06',
    '2023-08-07',
    '2023-08-08',
    '2023-08-09',
    '2023-08-10',
    '2023-08-11',
    '2023-08-12',
    '2023-08-13',
    '2023-08-14',
    '2023-08-15',
    '2023-08-16',
    '2023-08-17',
    '2023-08-18',
    '2023-08-19',
    '2023-08-20',
    '2023-08-21',
    '2023-08-22',
    '2023-08-23',
    '2023-08-24',
    '2023-08-25',
    '2023-08-26',
    '2023-08-27',
    '2023-08-28',
    '2023-08-29',
    '2023-08-30',
    '2023-08-31',
]


def is_slot_available(time_slot):
    appointments = Appointment.query.filter_by(date_available=date_available, time_slots=time_slots).first()
    if appointments:
        return False
    return True


@views.route('/appointment', methods=['GET', 'POST'])
@login_required
def appointment():
    if request.method == 'POST':
        hospitalName = request.form.get('hospital_name')
        dateAvailable = request.form.get('date_available')
        timeSlots = request.form.get('time_slots')

        if is_slot_available(time_slots):
            flash('Slot already booked. Please try another one.')
            return redirect(url_for('appointment'))

        if hospitalName == 'Select Hospital':
            flash('Please select a hospital.')
            return redirect(url_for('appointment'))

        if dateAvailable == 'Select Date':
            flash('Please select a date.')
            return redirect(url_for('appointment'))

        if timeSlots == 'Select Time':
            flash('Please select a time.')
            return redirect(url_for('appointment'))

        new_appointment = Appointment(hospital_name=hospitalName, date_available=dateAvailable, timeSlots=time_slots)
        db.session.add(new_appointment)
        db.session.commit()

        flash('Appointment created successfully.')
        return redirect(url_for('dashboard.html'))

    return render_template('dashboard.html')


@views.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@views.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
