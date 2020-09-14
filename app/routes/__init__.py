from app import app
from app.routes.api import UserAPI
from app.routes.home_ui import HomePage
from app.routes.login_routes import SignUp


# Architecture Plan 1: /api/
app.add_url_rule("/api/", view_func=UserAPI.as_view("user_api"))

# Architecture Plan 2: /home/ & Template View
app.add_url_rule("/home/", view_func=HomePage.as_view("home_view"))

# Architectures Plan 3: Login Routes URL Views
app.add_url_rule("/signup/", view_func=SignUp.as_view("signup"))
app.add_url_rule("/login/", view_func=SignUp.as_view("login"))
app.add_url_rule("/logout/", view_func=SignUp.as_view("logout"))
#TODO: Add URL rule for password-change