from app import app
from flask import render_template, redirect, url_for
from flask import make_response, jsonify
from flask.views import View, MethodView

# Logging related imports
from app.log import LogConfigurator


LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)


# View 1. /home/    GET
# View 2. /add/     POST
# View 3. /Update/  PUT
# View 4. /delete/  DELETE
