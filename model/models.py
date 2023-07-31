from views import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False, unique=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.DateTime, nullable=False)
    insurance_id = db.Column(db.Integer, db.ForeignKey('insurance.id'))
    appointment = db.relationship('Appointment', backref='user', lazy=True)

    def __repr__(self):
        return f'<User {self.insurance_id}>'
    

class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    insurance_id = db.Column(db.Integer, db.ForeignKey('insurance.id'))
    hospital_id = db.Column(db.Integer, db.ForeignKey('hospitals.id'))

    def __repr__(self):
        return f'<Appointment {self.id}>'



