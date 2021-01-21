from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,current_user
from main.models import User_massage,db,Public_text,User_write_text
from app1.models import User
from up_file_tou.models import User_tou
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,TextAreaField
from wtforms.validators import DataRequired
import re,time,datetime


main = Blueprint('main', __name__, template_folder='templates')

class NameForm(FlaskForm):  #表单
    real_name = StringField('输入你的真实姓名',validators= [DataRequired()] )
    sex = StringField('输入你的性别',validators= [DataRequired()])
    phone = StringField('输入你的电话号',validators= [DataRequired()])
    email= StringField('输入你的邮箱',validators= [DataRequired()])
    location = StringField('输入你的家庭地址',validators= [DataRequired()])
    submit = SubmitField('Submit')

class NameForm1(FlaskForm): # 公共留言板

    text = TextAreaField('输入留言的内容',validators= [DataRequired()])
    submit = SubmitField('提交')

class NameForm_Write_text(FlaskForm):
    title = StringField('文章标题',validators= [DataRequired()])
    text = TextAreaField('输入文章内容(暂不支持高级功能)', validators=[DataRequired()])
    submit = SubmitField('提交')

# 展示 主页面

@main.route('/')
@login_required  # 路由保护 只有登入之后才可访问
def index():
    result = User.query.filter_by(userid=current_user.get_id()).first()
    name = result.username
    res = User_tou.query.filter_by(userid=current_user.get_id()).first()
    address = res.address
    return  render_template('index.html',name = name ,address = address)

# 展示 个人信息页面
@main.route('/user_massage')
@login_required
def user_message():
    result = User_massage.query.filter_by(userid = current_user.get_id() ).first()
    userid = result.userid
    real_name = result.real_name
    sex = result.sex
    location = result.location
    phone = result.phone
    email = result.email
    res = User_tou.query.filter_by(userid = current_user.get_id()).first()
    address = res.address

    return render_template('user_message.html',userid = userid,real_name = real_name,sex=sex,
                           location=location,phone=phone,email=email,address = address)

# 展示 修改个人信息页面
@main.route('/edit_user_massage')
@login_required
def edit_user_massage():
    res = User_massage.query.filter_by(userid=current_user.get_id()).first()
    form = NameForm(real_name = res.real_name,sex=res.sex,location=res.location,phone=res.phone,email=res.email)
    return  render_template('edit_user_massage.html',form =form)

# 展示 公共留言板
@main.route('/public_text')
@login_required
def show_public_text():
    result = User.query.filter_by(userid=current_user.get_id()).first()
    name = result.username

    result = Public_text.query.all()
    result_tou = User_tou.query.all()
    form = NameForm1()
    return render_template('public_text.html',form = form,name = name ,result = result,result_tou =result_tou)

# 展示 写文章
@main.route('/write_text',methods=['GET'])
@login_required
def show_write_text():
    if request.values.get('id') :
        id = request.values.get('id')
        res = User_write_text.query.filter_by(userid=current_user.get_id(),id = id).first()
        if res :
            form = NameForm_Write_text(title=res.title,text=res.text)
        else:
            return render_template('500.html')
    else:
        form = NameForm_Write_text()
    res = User_tou.query.filter_by(userid=current_user.get_id()).first()
    address = res.address
    return render_template('write_self_text.html',form=form,address = res.address)

# 中转
@main.route("/zhong_zhuan/<name>",methods=['GET'])
@login_required
def show_zhong_zhuan(name):
    if name :
        #action =request.values.get('action')
        print(name)
        if name == '1' :
            return render_template('zhong_zhuan.html',message="删除成功!!")
        if name == '2' :
            return render_template('zhong_zhuan.html',message="提交成功!!")
        if name == '3' :
            return render_template('zhong_zhuan.html',message="修改成功!!")
        return render_template('500.html')
    return render_template('zhong_zhuan.html')

#展示  管理文章
@main.route('/show_self_write')
@login_required
def show_self_write():
    result = User_write_text.query.filter_by(userid=current_user.get_id()).all()
    return render_template('show_self_write.html',result = result)


# 展示 个人主页
@main.route("/<name>")
@login_required
def show_ge_ren(name):
    result = User.query.filter_by(username = name).first()
    if result is not None :
        try:
            userid = result.userid
            res = User_tou.query.filter_by(userid = userid).first()
            address = res.address
            res = User_massage.query.filter_by(userid = userid).first()
            real_name = res.real_name
            sex = res.sex
            location = res.location
            email = res.email
            phone = res.phone
            # res 文章查询集合
            res = User_write_text.query.filter_by(userid = userid).all()
        except:
            return render_template('404.html')
        else:
            return  render_template('show_ge_ren.html',userid= userid,address =address,real_name = real_name,
                                sex =sex,location = location,email = email,phone = phone ,result= res,name =name)
    else:
        return  render_template('404.html')


# 展示 文章
@main.route("/show_text/<name>")
@login_required
def show_text(name):
    print(int(name))
    try:
        res = User_write_text.query.filter_by(id = int(name)).first()
    except:
        return render_template("404.html")
    else:
        return render_template("show_text.html" , title1 = res.title,time = res.time, text =res.text)

# ++++++++++++++++++++++++++++++++++++++++++++++++  划分线 +++++++++++++++++++++++++++++++++++++

# 删除文章
@main.route('/delete_self_write',methods=['GET'])
@login_required
def delete_write_text():
    if request.values.get('id'):
        id = request.values.get('id')
        res = User_write_text.query.filter_by(userid=current_user.get_id(), id=id).first()
        if res :
            db.session.delete(res)
            db.session.commit()
            return redirect(url_for('main.show_zhong_zhuan',_external=True,name=1))
        else :
            return render_template('500.html')
    return render_template('500.html')

# 功能 编辑个人资料

@main.route('/edit_user_massage',methods=['GET', 'POST'])
@login_required
def edit_user():
    res = User_massage.query.filter_by(userid=current_user.get_id()).first()
    form = NameForm(real_name=res.real_name, sex=res.sex, location=res.location, phone=res.phone, email=res.email)
    if form.validate_on_submit() :
        #userid = request.values.get('userid')
        real_name = request.values.get('real_name')
        sex = request.values.get('sex')
        location = request.values.get('location')
        phone = request.values.get('phone')
        if re.search('[0-9]{11}',phone) is  None :
            flash('请输入正确的手机号')
            return redirect(url_for('main.edit_user'))
        email = request.values.get('email')
        if re.search('.+@.+',email) is  None  :
            flash('请输入正确的邮箱')
            return redirect(url_for('main.edit_user'))

        sql = User_massage.query.filter_by(userid = res.userid).first()
        sql.real_name = real_name
        sql.sex = sex
        sql.phone =phone
        sql.location =location
        sql.email = email
        db.session.add(sql)
        db.session.commit()
        return redirect(url_for('main.user_message'))

    return render_template('edit_user_massage.html',form=form )


# 功能 提交公共留言

@main.route('/public_text',methods=['GET', 'POST'])
@login_required
def submit_public_text():
    form = NameForm1()
    if form.validate_on_submit():
        massage = request.values.get('text')
        from_id = current_user.get_id()
        res =  User.query.filter_by(userid=from_id).first()
        from_name = res.username
        # 时间戳转换
        time_int = int(time.time())
        timeArray = time.localtime(time_int)
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        sql = Public_text(time = time_string ,from_userid = from_id, from_name=from_name,massage = massage)
        db.session.add(sql)
        db.session.commit()

        return redirect(url_for('main.show_public_text'))
    return redirect(url_for('main.show_public_text'))


# 功能 提交文章

@main.route('/write_text',methods=['GET', 'POST'])
@login_required
def submit_write_text():
    form =NameForm_Write_text()
    if request.values.get('submit'):
        if request.values.get('id') :
            res = User_write_text.query.filter_by(userid=current_user.get_id(), id=request.values.get('id')).first()
            res.text = request.values.get('text')
            res.title = request.values.get('title')
            db.session.add(res)
            db.session.commit()
            return redirect(url_for('main.show_zhong_zhuan',_external=True,name=3))
        title = request.values.get('title')
        userid = current_user.get_id()
        text = request.values.get('text')
        time_int = int(time.time())
        timeArray = time.localtime(time_int)
        time_string = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

        if title and text :
            sql = User_write_text(userid = userid ,time = time_string,text=text,title=title)
            db.session.add(sql)
            db.session.commit()
            flash('提交成功！！')
            return redirect(url_for('main.show_zhong_zhuan',_external=True,name=2))
        else:
            flash('不能为空！！')
            return redirect(url_for('main.show_write_text'))
    return redirect(url_for('main.show_write_text'))



