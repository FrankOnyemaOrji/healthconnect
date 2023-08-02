<<<<<<< HEAD
from .. import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    phone_number = db.Column(db.String(150), nullable=False)
    insurance_id = db.Column(db.String(150), nullable=False, unique=True)
    appointments = db.relationship('Appointment')

    def __repr__(self):
        return f'{self.full_name} {self.email} {self.insurance_id}'


class Appointment(db.Model):
    __tablename__ = 'appointment'
    id = db.Column(db.Integer, primary_key=True)
    appointment_date = db.Column(db.String(150), nullable=False)
    student_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    student = db.relationship('User', foreign_keys=[student_user_id])

    def __repr__(self):
        return f'{self.appointment_date} {self.student_user_id}'
=======
#!/usr/bin/env python3
""" 
This file contains the models for the database.
"""
from ..app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    insurance_number = db.Column(db.String(80), nullable=False, unique=True, foreign_key=True)
    appointment = db.relationship('Appointment', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.id} {self.email} {self.firstname} {self.lastname}>'
    

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    date_available = db.Column(db.DateTime, nullable=False)
    time_slots = db.Column(db.DateTime, nullable=False)
    hospital_name = db.Column(db.Integer, db.ForeignKey('hospitals.id'))

    def __repr__(self):
        return f'<Appointment {self.id} {self.date_available} {self.time_slots}>'
>>>>>>> f8390e96f63b0eab84cc7219a4ce8173a4ddcb97
