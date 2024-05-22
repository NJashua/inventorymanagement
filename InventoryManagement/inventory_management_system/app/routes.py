from flask import Blueprint, request
from app.db import SnowflakeDB

# Create Blueprint for the routes
bp = Blueprint('routes', __name__)

# Configuration for Snowflake
snowflake_config = {
    'user': 'Nithin',
    'password': 'Nithin@2024',
    'account': 'bdhriyc-ke24872',
    'database': 'INVENTORY',
    'schema': 'PUBLIC'
}

# Initialize SnowflakeDB instance
db = SnowflakeDB(snowflake_config)

@bp.route('/search/<search_term>', methods=['GET'])
def search_products(search_term):
    return db.get_product_details_with_location(search_term)

@bp.route('/display_products', methods=['GET'])
def display_products():
    return db.display_products_details()

@bp.route('/purchase_product', methods=['POST'])
def insert():
    data = request.get_json()
    return db.insert_data(data)
@bp.route('/order_product', methods = ['POST', 'GET'])
def order_product():
   data = request.get_json()
   return db.order_service_details(data)

# @bp.route('/search_with_location/<search_term>', methods=['GET'])
# def search_product_with_location(search_term):
#     return db.search_product_with_location(search_term)