from app import app
from flask.views import View
from flask import render_template, redirect, url_for
from flask import request, make_response

# Forms Related import.
from forms import RegistrationForm, LoginForm

# Models related import
from app.models import Auth, Storage

# Login/auth Related imports
from flask_login import login_user, current_user, logout_user
# from flask_login import login_required

# Logging related imports
from app.log import LogConfigurator


# Logging Configuration
LogConfigurator.setup_logging()
logger = LogConfigurator.get_logger(__name__)


class SignUp(View):
    
    template_name = 'login/signup.html'
    form = RegistrationForm()
    methods = ["POST", "GET"]
    
    def dispatch_request(self):
        if request.method == 'GET':
            form = RegistrationForm()
            
            return render_template(self.template_name,
                                   title='SignUp',
                                   form=self.form)
        elif request.method == 'POST':
            
            object = request.POST
            
            username, email = object['username'], object['email']
            password = object['password']
            # password = bcrypt.generate_password_hash(password)
            # .decode()
            conf_pwd = object['confirm_password']
            # conf_pwd = bcrypt.generate_password_hash(password)
            # .decode()
            # Hash Password using bcrypt
            
            if password == conf_pwd:
                
                try:
                    query = Auth(Password=password,
                                 username=username,
                                 email=email,
                                 password=password)
                    query.save()
                    
                except:
                    # TODO: Exception Handling.
                    return make_response("Error", 500)
                
            
class Login(View):
    
    template_name = 'login/login.html'
    form = LoginForm()
    methods = ["POST", "GET"]
    
    def dispatch_request(self):
        if request.method == 'GET':
            return render_template(self.template_name,
                                   title='Login',
                                   form=self.form)
        
        elif request.method == 'POST':
            obj = request.POST
            user = obj['email']
            password = obj['password']
            
            #TODO Check hashed password in bcrypt
            try:
                query = Auth.query.filter(email=user).first()
            
                #hpwd = bcrypt.
                # check_password_hash(query.password,
                #                     query['password'])
                
                if query.password == password:
                    # TODO: handle Login and redirect.
                    login_user(user)
                    return render_template("app/home.html")
                
            except:
                # TODO: Query Exception Handling.
                # Redirect or Handle User unavailability.
                context = {'exists': "User doesn't exist. Signup"}
                return render_template(url_for('signup'), context)


class Logout(View):
    template_name = "login/logout.html"
    user = current_user
    
    def dispatch_request(self):
        logout_user()
        logger.info("User {0} has been logged out."
                    .format(self.user))
        
        return render_template(self.template_name)
