# 导入渲染模块，蓝图模块，数据传输模块，路由分配模块
from flask import render_template, Blueprint, request, url_for,flash,redirect
# 导入创建的模型，用来完成下面定义功能时对数据库的操作
from .models import User,db,Userlogin
from up_file_tou.models import User_tou
from werkzeug.security import generate_password_hash, check_password_hash # 密码安全
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField
from wtforms.validators import DataRequired
import time,re
from main.models import User_massage
# 创建蓝图。蓝图必须有前两个参数，为“蓝图名”，“当前运行文件名”。后两个是设置蓝图文件夹（蓝图文件夹即为app1文件夹）
# 在访问私有网页文件夹templates的位置目录，以及私有静态文件的位置目录
app1 = Blueprint('app1', __name__, template_folder='templates')

class NameForm(FlaskForm):  #表单
    name = StringField('输入你的名字',validators= [DataRequired()])
    first_pass = PasswordField('输入密码',validators= [DataRequired()])
    second_pass = PasswordField('再次输入密码',validators= [DataRequired()])
    submit = SubmitField('Submit')

class NameForm1(FlaskForm):  #表单
    name = StringField('输入你的名字',validators= [DataRequired()])
    first_pass = PasswordField('输入密码',validators= [DataRequired()])
    submit = SubmitField('Submit')

class NameForm2(FlaskForm):  #表单
    name = StringField('输入管理员账号',validators= [DataRequired()])
    first_pass = PasswordField('输入管理员密码',validators= [DataRequired()])
    submit = SubmitField('Submit')


# 定义函数渲染网页
@app1.route('/register/')
def show_register():
    form = NameForm()
    return render_template('register.html',form = form)

@app1.route('/login/')
def show_login():
    form = NameForm1()
    return render_template('login.html',form = form)

@app1.route('/admin_login/')
def show_admin_login():
    form = NameForm2()
    return render_template('admin_login.html',form = form)


# 定义函数实现注册功能
@app1.route('/register/', methods=['GET', 'POST'])
def account_register():
    form = NameForm()
    if form.validate_on_submit() :
        if request.method == 'POST':
            username = request.values.get('name')
            password = request.values.get('first_pass')
            password1 = request.values.get('second_pass')
            if username and password1 and password :
                if password == password1 :
                    if User.query.filter_by(username = username).first() :
                        flash('存在相同用户名')
                    else:
                        password = generate_password_hash(password)
                        sql = User(username = username,password =password)
                        db.session.add(sql)
                        db.session.commit()
                        # 同步信息表
                        result = User.query.filter_by(username = username).first()
                        sql = User_massage(userid = result.userid)
                        db.session.add(sql)
                        db.session.commit()
                        # 同步头像
                        sql1 = User_tou(userid= result.userid,address="/up_file_tou/images/mmmmmmmmmmmm.jpg")
                        db.session.add(sql1)
                        db.session.commit()
                        flash('注册成功！！可以进行登入。')
                        time.sleep(2)
                        return  redirect(url_for('app1.show_login'))
                else:
                    flash('密码不相同！！')
            else:
                flash('表单不能为空')
        else:
            flash('请求错误！！')
        return redirect(url_for('app1.show_register'))
    return render_template('register.html',form = form)


from flask_login import login_user,logout_user
from app import login_manager

# 通过用户名，获取用户记录，如果不存在，则返回None
def query_user(username):
    user = User.query.filter_by(username = username).first()
    if user is not None :
         return user
    else :
        return None

# 如果用户名存在则构建一个新的用户类对象，并使用用户名作为ID
# 如果不存在，必须返回None
@login_manager.user_loader
def load_user(userid):
    id = User.query.filter_by(userid=userid).first()
    if id is not None:
        curr_user = Userlogin()
        curr_user.id = userid
        return curr_user
    else :
        return None

# 函数实现登入功能
@app1.route('/login/', methods=['GET', 'POST'])
def account_login():
    form = NameForm1()
    if form.validate_on_submit() :
        username = request.values.get('name')
        password = request.values.get('first_pass')
        if re.search('admin',username) :
            flash('非法字符！！')
            return redirect(url_for('app1.show_login'))
        result = query_user(username)
        if result and check_password_hash(result.password,password) :
            flash('登入成功') # 添加功能 -----------
            curr_user =Userlogin()
            curr_user.id = result.userid
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user, remember=True)  # 此处调用load_user
            return redirect(url_for('main.index'))
        else:
            flash('输入有误')
        return redirect(url_for('app1.show_login'))
    return render_template('login.html', form=form)


# 管理员登入
@app1.route('/admin_login/', methods=['GET', 'POST'])
def admin_log_in():
    form = NameForm1()
    if form.validate_on_submit() :
        username = request.values.get('name')
        password = request.values.get('first_pass')
        result = query_user(username)
        is_admin = result.is_admin
        if result and check_password_hash(result.password,password)  and is_admin:

            flash('登入成功') # 添加功能 -----------
            curr_user =Userlogin()
            curr_user.id = result.userid
            # 通过Flask-Login的login_user方法登录用户
            login_user(curr_user, remember=True)  # 此处调用load_user
            return redirect(url_for('main.index'))
        else:
            flash('输入有误')
        return redirect(url_for('app1.show_login'))
    return render_template('admin_login.html', form=form)



@app1.route('/logout/')
def show_logout() :
    logout_user()
    flash('注销成功！')
    return redirect(url_for('app1.show_login'))
