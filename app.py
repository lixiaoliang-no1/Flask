from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap  # html xss 模板


app = Flask(__name__,template_folder='static/templates')
#app.debug=True

app.config['SECRET_KEY'] = 's_e_c_r_e_t_k_e_y'
bootstrap = Bootstrap(app)

# 绘画控制
from flask_login import LoginManager ,login_required,current_user# 登入
login_manager = LoginManager(app)
login_manager.login_view = 'app1.show_login'
login_manager.login_message = '请登入！！' # 默认的错误消息是
login_manager.login_message_category = 'info' # 设置闪现的错误消息的类别

from app1.models import User
from main.models import User_massage
from up_file_tou.models import  User_tou
from app1.views import app1
# 注册该蓝图  登入注册蓝图
app.register_blueprint(app1, url_prefix='/member/')

from main.view import main
app.register_blueprint(main, url_prefix='/main/')

from up_file_tou.views import up
app.register_blueprint(up, url_prefix='/up_file_tou/')
@app.route('/')
@login_required
def index():
    return redirect(url_for('main.index'))
