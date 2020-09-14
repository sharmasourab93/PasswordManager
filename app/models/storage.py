from app import db
from app.models import Auth


class Storage(db.Model):
    __tablename__ = 'storage'
    
    id_ = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True,
                    nullable=False)
    uid = db.Column(db.Integer,
                    db.ForeignKey(Auth.userid),
                    nullable=False
                    )
    domain = db.Column(db.String(255),
                       unique=True,
                       nullable=False)
    user_for_domain = db.Column(db.String(50),
                                nullable=True)
    Password = db.Column(db.String(1000))
