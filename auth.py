from flask import Blueprint, render_template, request, flash, redirect, url_for
from views import db
from model.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
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


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('index'))


@auth.route('/register', methods=['GET', 'POST'])
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
