from db_operate import db
from flask_login import UserMixin

class Userlogin(UserMixin):
    pass

class User_massage(db.Model):
    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    real_name = db.Column(db.String(30))
    sex = db.Column(db.String(10))
    location = db.Column(db.String(50))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(30))

    __tablename__ = 'user_massage'


class Private_text(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    from_userid = db.Column(db.Integer)
    to_userid = db.Column(db.Integer)
    time = db.Column(db.Integer)
    massage = db.Column(db.Text)

    __tablename__ = 'private_text'



class Public_text(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    from_userid = db.Column(db.Integer)
    from_name = db.Column(db.String(30))
    time = db.Column(db.String(30))
    massage = db.Column(db.Text)

    __tablename__ = 'public_text'


class User_write_text(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.Integer)
    text = db.Column(db.Text)
    time = db.Column(db.String(30))
    title = db.Column(db.String(30))

    __tablename__ = 'user_write_text'