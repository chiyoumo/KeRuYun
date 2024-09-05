from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username=StringField(label="用户名",valications=[DataRequired()])
    password=PasswordField(label="密码",valiations=[DataRequired()])
    submit=SubmitField(label="登陆")