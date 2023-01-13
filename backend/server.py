from flask import Flask
from flask import jsonify


from sql_connection import get_sql_connection
import Products_dao 

connection = get_sql_connection()

app = Flask(__name__)
@app.route('/getproducts')

def hello():
    products = Products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin','*')
    return response


if __name__ == '__main__':
    print("Starting Python Flask Server for Grocery Store Management system")
    app.run(port=5000)
