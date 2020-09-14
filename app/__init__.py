# Flask Related Imports
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Config Imports
from configs.load_configs import CONN_STRING

# Log Configuration import
from log import LogConfigurator

# Core Python related imports
from os.path import join, abspath, dirname, curdir


LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)
logger.info("Initializing Password Manager")


template_dir = join(curdir, 'app/templates')

app = Flask(__name__, template_folder=template_dir)
app.config['SQLALCHEMY_DATABASE_URI'] = CONN_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.secret_key = '177d30a6751dd7f5bd81babbe8ce3aa2'


db = SQLAlchemy(app)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Models Initiation Import.
from app.models import initialize_db


initialize_db()


# To import URL/Routes & it's corresponding views.
from app import routes
