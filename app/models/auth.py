from app import db
from flask_login import UserMixin
from datetime import date


class Auth(db.Model, UserMixin):
    __tablename__ = 'auth'
    
    userid = db.Column(db.Integer,
                       primary_key=True,
                       autoincrement=True)
    user = db.Column(db.String(50),
                     unique=True,
                     nullable=False)
    email = db.Column(db.String(50),
                      unique=True)
    password = db.Column(db.String(100),
                         nullable=False)
    created_ = db.Column(db.Date(),
                         default=date.today)

    def __repr__(self):
        ret_string = "User" \
                     "(user-{0}," \
                     "email={1}, " \
                     "created_={2})"\
            .format(self.user, self.email, self.created_)
        
        return ret_string
