from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config['SECRET_KEY'] = 'mau789'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fridgeries.db'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'showprijava'
login_manager.login_message_category = 'info'

from fridgeries import routes