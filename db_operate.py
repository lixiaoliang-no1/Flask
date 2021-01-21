# 导入SQLAlchemy，可操作数据库以及连接数据库
from flask_sqlalchemy import SQLAlchemy
# 导入app工程文件
from app import app

app.config['SECRET_KEY'] = 's_e_c_r_e_t_k_e_y'

# 连接数据库（格式：'mysql+pymysql://用户名:密码@端口号/数据库名'）
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://用户名:密码@数据库地址:3306/app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 数据库连接(生成一个数据库操作对象)
db = SQLAlchemy(app)


