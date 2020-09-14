from flask import make_response, jsonify, request
from flask.views import MethodView
from flask_login import current_user

# Model imports
from app.models import Auth, Storage

# Logging related imports
from app.log import LogConfigurator

# SQL Alchemy related imports
from sqlalchemy.exc import ProgrammingError


# Logger Configuration
LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)

# TODO: Adding Blueprint to api.py


class UserAPI(MethodView):
    """
    User API: API View Logic to return status or values.
    UserAPI implements 3 methods/verbs
        1. GET
        2. POST
        3. PUSH
    """
    
    methods = ['GET', 'POST', 'PUT']

    # View No. 1 /api/ GET
    def get(self):
        
        logger.info("Method {0} GET".format(self.__class__.__name__))
        
        try:
            query = Storage.query.all()
            if len(query) == 0:
                raise ValueError("Value Error")
            
            ret_obj = jsonify(query)
            
            return make_response(ret_obj, 200)
        
        except ValueError:
            
            return make_response('No Entries', 204)
        

    # View No. 2 /api/ POST
    def post(self):
        logger.info("Method {0} POST".format(self.__class__.__name__))
        object = request.get_json()
        url_ = object['domain']
        user = object['user']
        
        # TODO: Bcrypt Generate Password Hash
        # pwd = bcrypt.generate_password_hash(object['pwd']).decode()
        pwd = object['password']
        
        try:
            if current_user:
                uid = Auth.query\
                    .filter(Auth.user == current_user).first()
                uid = uid.userid
                
        except ProgrammingError:
            
            return make_response("User Not found", 401)
            
        store = Storage(uid=uid,
                        domain=url_,
                        user_for_domain=user,
                        password=pwd)
        
        store.save()

    # View No. 3 /api/ PUT
    def put(self):
        
        logger.info("Method {0} PUT".format(self.__class__.__name__))
        object = request.get_json()
        
        user, url_ = object['user'], object['domain']
        pwd = object['password']
        
        # TODO: Define Flask-Bcrypt
        # h_pwd = bcrypt.generate_password_hash(pwd).decode()
        
        try:
            uid = Auth.query.filter(Auth.user == current_user).first()
            uid = uid.userid
            
            query = Storage.query.filter(uid=uid,
                                         domain=url_,
                                         user_for_domain=uid)
            
            if query is not None:
                query = query.first()
                query.Password = pwd
                query.save()
                
                return make_response("Saved Successfully", 202)
            
        except ProgrammingError:
            return make_response("User or Object Doesn't exist", 404)
