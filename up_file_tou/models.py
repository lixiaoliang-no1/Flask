from db_operate import db
from flask_login import UserMixin

class Userlogin(UserMixin):
    pass

class User_tou(db.Model):

    userid = db.Column(db.Integer,primary_key=True,autoincrement= True)
    address = db.Column(db.String(70))

    __tablename__ = 'user_tou'

