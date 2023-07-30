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
    insurance = db.relationship('Insurance', secondary='users', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<User {self.insurance_id}>'


class Insurance(db.Model):
    __tablename__ = 'insurance'
    id = db.Column(db.Integer, primary_key=True)
    Student_name = db.Column(db.String(80), nullable=False)
    users = db.relationship('User', backref='insurance', lazy=True)

    def __repr__(self):
        return f'<Insurance {self.Student_name}>'
