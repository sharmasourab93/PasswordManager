from app import app
from flask import render_template, redirect, url_for
from flask import make_response, jsonify

# Forms Related import.
from forms import RegistrationForm, LoginForm

# Login/auth Related imports
from flask_login import login_user, current_user, logout_user
# from flask_login import login_required

# Logging related imports
from app.log import LogConfigurator

LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)


@app.route("signup/", methods=['POST'])
def signup():
    form = RegistrationForm()
    return render_template('login/signup.html', title='SignUp', form=form)


@app.route("login/", methods=['POST'])
def login():
    form = LoginForm()
    return render_template('login/login.html', title='Login', form=form)


@app.route("logout/")
def logout():
    user = current_user
    logout_user()
    logger.info("User {0} has been logged out.".format(user))
    
    return render_template('login/logout.html')
