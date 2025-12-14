from flask import Flask, request, jsonify, send_from_directory
import json
import os

from sql_connection import get_sql_connection
import products_dao
import orders_dao
import uom_dao

# Create Flask app and tell it where UI lives
app = Flask(
    __name__,
    static_folder="../ui",
    static_url_path="/ui"
)

# Database connection
connection = get_sql_connection()

# ---------------- HOME (UI) ----------------
@app.route("/")
def home():
    return send_from_directory(app.static_folder, "index.html")


# ---------------- API ROUTES ----------------

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({'product_id': product_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({'order_id': order_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({'product_id': return_id})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# ---------------- MAIN ----------------
if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(host="0.0.0.0", port=5000, debug=True)
