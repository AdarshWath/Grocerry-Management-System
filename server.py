from flask import Flask, request, jsonify
import product_dao
from mysql_connection import get_sql_connection

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/hello')
def hello():
    return "Hello, how are you?"

@app.route('/getProducts', methods = ['GET'])
def get_products():
    products = product_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

def hello():
    return "Hello, how are you?"

if __name__ == "__main__":
    print("Starting python Flask Server for Grocery Store Management System")
    app.run(port = 5000)