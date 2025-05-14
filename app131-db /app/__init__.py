from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

# Create app
myapp_obj = Flask(__name__, static_folder='../static')
basedir = os.path.abspath(os.path.dirname(__file__))

# Config setup
myapp_obj.config.from_mapping(
    SECRET_KEY='you-will-never-guess',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'app.db'),
)

# Initialize extensions
db = SQLAlchemy(myapp_obj)

login_manager = LoginManager()
login_manager.init_app(myapp_obj)
login_manager.login_view = 'login'

# Import AFTER defining login_manager
from app.models import User

# This is REQUIRED for Flask-Login to work
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# This should come LAST
from app import routes, models
