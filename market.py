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

    def __repr__(self):
        return f"Item {self.name}"

@app.route('/')
<<<<<<< HEAD
<<<<<<< HEAD
@app.route('/home')
=======
@app.route('/home')
>>>>>>> ca4870bdf3eaa3328e31227a920190118c592df0
=======
@app.route('/home')
>>>>>>> ea68b81afe69e115e0a48e9512fd4a91d400e9c2
def home_page():
    return render_template('home.html')

@app.route('/market')
def market_page():
    items = Item.query.all()

    return render_template('market.html', items= items)
