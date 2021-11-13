from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = [
    {'id': 1, 'name': 'Strawberry Matcha', 'barcode': '893212299897', 'price': 5.00},
    {'id': 2, 'name': 'Lychee', 'barcode': '123985473165', 'price': 4.80},
    {'id': 3, 'name': 'Ube', 'barcode': '231985128446', 'price': 4.80}
    ]

    return render_template('market.html', items= items)
