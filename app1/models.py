# 导入db_operate文件中的db数据库，DBO（封装的数据库操作函数，觉得不需要也可不导DBO）
from db_operate import db
from flask_login import UserMixin

class Userlogin(UserMixin):
    pass

# 创建简单的用户账号，密码模型。
class User(db.Model):
    userid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(128),nullable=False)
    is_admin = db.Column(db.Integer,nullable=True)
    # 表格更名
    __tablename__ = 'user'
    # 初始化每个实例。（若在第6步导入DBO文件，可不用写以下初始化语句，DBO类方法中已封装。）
    def __init__(self, username, password):
        self.username = username
        self.password = password