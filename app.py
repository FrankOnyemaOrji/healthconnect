
from . import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
#
# from flask import Flask, render_template, request, flash, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
# import os
# from flask_login import login_user, logout_user, login_required, current_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from models.base_model import User, Appointment
# db = SQLAlchemy()
# DB_NAME = "database.db"
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)
#
#
# # @app.before_first_request
# def create_database():
#     if not os.path.exists('website/' + DB_NAME):
#         db.create_all()
#         print('Created Database!')
#
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
#
# # Login and Registration Routes
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#
#         user = User.query.filter_by(email=email).first()
#
#         if user:
#             if user and check_password_hash(user.password, password):
#                 login_user(user)
#                 flash('Logged in successfully.')
#                 return redirect(url_for('index'))
#
#             if not user(user and check_password_hash(user.password, password)):
#                 flash('Incorrect password, try again.')
#                 return redirect(url_for('login'))
#
#         else:
#             flash('Account not found. Please sign up to continue')
#             return redirect(url_for('register'))
#
#     return render_template('login.html', user=current_user)
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     flash('Logged out successfully.')
#     return redirect(url_for('index'))
#
#
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         firstname = request.form.get('firstname')
#         lastname = request.form.get('lastname')
#         password = request.form.get('password')
#         insurance_id = request.form.get('insurance_id')
#
#         insurance_id_exists = User.query.filter_by(insurance_id=insurance_id).first()
#         if insurance_id_exists:
#             flash('Insurance ID already exists. Please try again.')
#             return redirect(url_for('register'))
#
#         email_exists = User.query.filter_by(email=email).first()
#         if email_exists:
#             flash('Email already exists. Please try again.')
#             return redirect(url_for('register'))
#
#         password_hash = generate_password_hash(password)
#
#         new_user = User(email=email, firstname=firstname, lastname=lastname, password=password_hash,
#                         insurance_id=insurance_id)
#         db.session.add(new_user)
#         db.session.commit()
#
#         flash('Account created successfully.')
#         return redirect(url_for('login'))
#
#     return render_template('register.html')
#
#
# # Appointment Routes
# hospital_name = [
#     'Ubuzima Polyclinic',
#     'Ubuzima Polyclinic',
#     'Polyclinic saint Jean',
#     'Polyfam',
#     'UR-CMHS BD'
#     'Polyclinique medico sociale'
#     'olyclinique la medicale Musanze'
#     'Polyclinique la medicale Kigali'
#     'Polyclinique la medicale Rubavu'
#     "Polyclinique de l'etoile"
#     'Polyclinic du plateau'
#     'Croix du sud hospital'
#     'Peace Pololyclinic'
#     'Polyclinic du carrefour'
#     'Inkurunziza Orthopedic Hospital'
#     'Glamerc Polyclinic'
#     'Polyclinique La medicale Huye'
#     'Wiwo Specialized Hospital'
#     'Beatrice Polyclinic'
#     'MBC HOSPITAL'
#     'Salus Polyclinic'
# ]
#
# time_slots = [
#     '6:00 AM',
#     '6:30 AM',
#     '7:00 AM',
#     '7:30 AM',
#     '8:00 AM',
#     '8:30 AM',
#     '9:00 AM',
#     '9:30 AM',
#     '10:00 AM',
#     '10:30 AM',
#     '11:00 AM',
#     '11:30 AM',
#     '12:00 PM',
#     '12:30 PM',
#     '1:00 PM',
#     '1:30 PM',
#     '2:00 PM',
#     '2:30 PM',
#     '3:00 PM',
#     '3:30 PM',
#     '4:00 PM',
#     '4:30 PM',
#     '5:00 PM',
#     '5:30 PM',
#     '6:00 PM',
#     '6:30 PM',
#     '7:00 PM',
#     '7:30 PM',
#     '8:00 PM',
#     '8:30 PM',
#     '9:00 PM',
#     '9:30 PM',
#     '10:00 PM',
#     '10:30 PM',
#     '11:00 PM',
# ]
#
# date_available = [
#     '2023-08-01',
#     '2023-08-02',
#     '2023-08-03',
#     '2023-08-04',
#     '2023-08-05',
#     '2023-08-06',
#     '2023-08-07',
#     '2023-08-08',
#     '2023-08-09',
#     '2023-08-10',
#     '2023-08-11',
#     '2023-08-12',
#     '2023-08-13',
#     '2023-08-14',
#     '2023-08-15',
#     '2023-08-16',
#     '2023-08-17',
#     '2023-08-18',
#     '2023-08-19',
#     '2023-08-20',
#     '2023-08-21',
#     '2023-08-22',
#     '2023-08-23',
#     '2023-08-24',
#     '2023-08-25',
#     '2023-08-26',
#     '2023-08-27',
#     '2023-08-28',
#     '2023-08-29',
#     '2023-08-30',
#     '2023-08-31',
# ]
#
#
# def is_slot_available(time_slot):
#     appointments = Appointment.query.filter_by(date_available=date_available, time_slots=time_slots).first()
#     if appointments:
#         return False
#     return True
#
#
# @app.route('/appointment', methods=['GET', 'POST'])
# @login_required
# def appointment():
#     if request.method == 'POST':
#         hospitalName = request.form.get('hospital_name')
#         dateAvailable = request.form.get('date_available')
#         timeSlots = request.form.get('time_slots')
#
#         if is_slot_available(time_slots):
#             flash('Slot already booked. Please try another one.')
#             return redirect(url_for('appointment'))
#
#         if hospitalName == 'Select Hospital':
#             flash('Please select a hospital.')
#             return redirect(url_for('appointment'))
#
#         if dateAvailable == 'Select Date':
#             flash('Please select a date.')
#             return redirect(url_for('appointment'))
#
#         if timeSlots == 'Select Time':
#             flash('Please select a time.')
#             return redirect(url_for('appointment'))
#
#         new_appointment = Appointment(hospital_name=hospitalName, date_available=dateAvailable, timeSlots=time_slots)
#         db.session.add(new_appointment)
#         db.session.commit()
#
#         flash('Appointment created successfully.')
#         return redirect(url_for('dashboard.html'))
#
#     return render_template('dashboard.html')
#
#
# # <!-- In book_appointment.html -->
# # <select name="slot" id="slot">
# #     {% for slot in slots %}
# #         {% if is_slot_available(slot) %}
# #             <option value="{{ slot }}">{{ slot }}</option>
# #         {% else %}
# #             <option value="{{ slot }}" disabled>{{ slot }} - Booked</option>
# #         {% endif %}
# #     {% endfor %}
# # </select>
#
#
# # @app.errorhandler(404)
# # def page_not_found(e):
# #     return render_template('404.html'), 404
# #
# #
# # @app.errorhandler(500)
# # def internal_server_error(e):
# #     return render_template('500.html'), 500
# >>>>>>> f8390e96f63b0eab84cc7219a4ce8173a4ddcb97
