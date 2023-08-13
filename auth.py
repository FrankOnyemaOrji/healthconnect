from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from models.base_model import User
from create_app import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully.')
                login_user(user)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again.')
                return redirect(url_for('auth.login'))
        else:
            flash('Email does not exist.')
            return redirect(url_for('auth.login'))
    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.')
    return redirect(url_for('views.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        password = request.form.get('password')
        insurance_id = request.form.get('insurance_id')
        phone_number = request.form.get('phone_number')

        insurance_id_exists = User.query.filter_by(insurance_id=insurance_id).first()
        email_exists = User.query.filter_by(email=email).first()

        password_hash = generate_password_hash(password)

        if insurance_id_exists:
            flash('Insurance ID already exists.')
        elif email_exists:
            flash('Email already exists.')
        else:
            new_user = User(email=email, full_name=f'{firstname} {lastname}', password=password_hash,
                            insurance_id=insurance_id, phone_number=phone_number)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('Account created successfully.')
            return redirect(url_for('views.index'))

    return render_template('register.html', user=current_user)
