from flask import Blueprint,render_template,request,redirect,url_for,flash,Response,make_response
from app1.models import User
from .models import  User_tou,db
from werkzeug.utils import secure_filename
import os
import json
from flask_login import login_required,current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,FileField
from wtforms.validators import DataRequired
import  hashlib

up = Blueprint('up', __name__, template_folder='templates',static_folder='/up_file_tou/images')

class NameForm(FlaskForm):  #表单
    file =FileField('选择上传的图片',validators= [DataRequired()])
    submit = SubmitField('提交')


# 文件上传
@up.route('/')
@login_required
def show_up_file():
    form = NameForm()
    res = User_tou.query.filter_by(userid=current_user.get_id()).first()
    address = res.address
    return  render_template('up_file.html',form =form,address =address)

# 访问头像
@up.route("/images/<name>")
@login_required
def show_tou(name):

    path = os.path.dirname(__file__)+ '\\images\\'+name
    image_data = open(path ,'rb').read()
    resp = make_response(image_data)
    resp.headers['Content-Type'] = 'image/png'

    return  resp
#---------------------------------------------------------------

@up.route('/',methods=['GET', 'POST'])
@login_required
def up_file():
    form = NameForm()
    if form.validate_on_submit() :
        BASE_DIR = os.path.dirname(__file__)
        dir = os.path.join(BASE_DIR, 'images\\')
        file = request.files.get('file')

        # secure_filename：检测中文是否合法
        filename = secure_filename(file.filename)
        types = ['png','bmp','gif','jpg']
        if filename.split('.')[-1] in types :
            userid = current_user.get_id()
            result = User.query.filter_by(userid=userid).first()
            name = result.username

            data = name + str(userid)
            md5_str = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
            file.save(os.path.join(BASE_DIR, 'images\\'+md5_str+'.png'))
            flash('上传成功！！')

            address = '/up_file_tou/images/'+ md5_str+'.png'
            res = User_tou.query.filter_by(userid = userid).first()
            if res is  None :
                sql = User_tou(userid= userid,address = address)
                db.session.add(sql)
                db.session.commit()
            else:
                res.address = address
                db.session.add(res)
                db.session.commit()
            return redirect(url_for('main.user_message'))
        else :
            flash('上传文件不符合要求！')
            return redirect(url_for('up.show_up_file'))
    return render_template('up_file.html',form =form)
