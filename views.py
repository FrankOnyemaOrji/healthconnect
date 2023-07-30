import app as app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
DB_NAME = "database.db"
base_dir = os.path.abspath(os.path.dirname(__file__))


# uri = os.environ.get('DATABASE_URL')
# if uri.startswith('postgres://'):
#     uri = uri.replace('postgres://', 'postgresql://', 1)


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # uri or 'sqlite:///' + os.path.join(base_dir, DB_NAME)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from auth import auth

    app.register_blueprint(auth, url_prefix='/')

    import app
    from model.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        db.create_all()

    return app


# @app.before_first_request
def create_database(app):
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
