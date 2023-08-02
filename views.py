from flask import Blueprint, render_template
from flask_login import login_required
from . import db


views = Blueprint('views', __name__)


@views.route('/')
def index():  # put application's code here
    return render_template('index.html')
