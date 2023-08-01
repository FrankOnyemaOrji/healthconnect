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
