from app import app
from flask import render_template, redirect, url_for
from flask import make_response, jsonify
from flask.views import View, MethodView

# Logging related imports
from app.log import LogConfigurator


LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)


# View 1 /api/ GET
# View 2 /api/ POST
# View 3 /api/ PUT
