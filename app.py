from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from model.models import User






db = SQLAlchemy()
DB_NAME = "database.db"

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# @app.before_first_request
def create_database():
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

@app.route("/")
def index():
    return render_template('index.html')













@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if user and check_password_hash(user.password, password):
                login_user(user)
                flash('Logged in successfully.')
                return redirect(url_for('index'))

            if not user(user and check_password_hash(user.password, password)):
                flash('Incorrect password, try again.')
                return redirect(url_for('login'))

        else:
            flash('Account not found. Please sign up to continue')
            return redirect(url_for('register'))

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        insurance_id = request.form.get('insurance_id')

        insurance_id_exists = User.query.filter_by(insurance_id=insurance_id).first()
        if insurance_id_exists:
            flash('Insurance ID already exists. Please try again.')
            return redirect(url_for('register'))

        email_exists = User.query.filter_by(email=email).first()
        if email_exists:
            flash('Email already exists. Please try again.')
            return redirect(url_for('register'))

        password_hash = generate_password_hash(password)

        new_user = User(email=email, firstname=firstname, lastname=lastname, password=password_hash, insurance_id=insurance_id)
        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully.')
        return redirect(url_for('login'))

    return render_template('register.html')



