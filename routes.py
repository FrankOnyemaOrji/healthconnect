from flask import Blueprint
from flask import render_template, request, flash, redirect, url_for

route = Blueprint('route', __name__)


@route.route('/')
@route.route('/index')
def index():
    return 'Hello World!'
