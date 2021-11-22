from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '738cb8a75480487c1e83b2da'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes