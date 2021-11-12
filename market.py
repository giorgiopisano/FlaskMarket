from flask import Flask, render_template
app = Flask(__name__)

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
