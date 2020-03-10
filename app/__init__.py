from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Create app objects
app = Flask(__name__)
app.config.from_object(Config)

# Create the login manager
login = LoginManager(app)
login.login_view = 'login'

# Create database objects
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models