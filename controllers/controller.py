from app import app
from flask import render_template
from models.order_list import orders

@app.route('/orders')
def orders_index():
    return render_template('index.html', title='Home', orders=orders)

    # return render_template('index.html', title='Home', tasks=tasks)

@app.route('/orders/1')
def orders_1_index():
    return render_template("orders.html", title="First Order", orders=orders)