from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
DB_NAME = "database.db"

base_dir = os.path.dirname(os.path.realpath(__file__))


# uri = os.environ.get('DATABASE_URL')
# if uri.startswith('postgres://'):
#     uri = uri.replace('postgres://', 'postgresql://', 1)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(base_dir, DB_NAME)}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models.base_model import User, Appointment

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not os.path.exists(os.path.join(base_dir, DB_NAME)):
        db.create_all(app=app)
        print('Created Database!')
