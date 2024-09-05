from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import LoginManager

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:12345678@localhost:3306/myblog_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
# app.config['SECRET_KEY']='ec9439cfc6c79ae2029594d'
# db = SQLAlchemy(app)
# login_manager = LoginManager()

from routes import user_routes
from routes import admin_routes
from routes import login_routes

