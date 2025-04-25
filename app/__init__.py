from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY']='c2ebfa0eb82b22723909d6a5940fca15ff7533928d69947b92192843be4e1e63'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///enock.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
