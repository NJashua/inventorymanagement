from flask import Blueprint, request, jsonify, current_app
import requests

bp = Blueprint('routes', __name__)

MAPBOX_API_TOKEN = 'your_mapbox_api_token'

@bp.route('/search', methods=['GET'])
def search_products():
    search_term = request.args.get('search_term')
    if not search_term:
        return jsonify({"error": "search_term is required"}), 400
    
    db = current_app.config['SnowflakeDB']
    return db.get_product_details_with_location(search_term)

@bp.route('/display_products', methods=['GET'])
def display_products():
    db = current_app.config['SnowflakeDB']
    return db.display_products_details()

@bp.route('/purchase_product', methods=['POST'])
def insert():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    db = current_app.config['SnowflakeDB']
    return db.insert_data(data)

@bp.route('/order_product', methods=['POST'])
def order_product():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    db = current_app.config['SnowflakeDB']
    return db.order_service_details(data)

@bp.route('/create_delivery_order', methods=['POST'])
def create_delivery_order():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    db = current_app.config['SnowflakeDB']
    order_response = db.order_service_details(data)
    if order_response[1] != 200:
        return jsonify({"error": "Order creation failed"}), order_response[1]

    origin = data.get('origin')
    destination = data.get('destination')
    if not origin or not destination:
        return jsonify({"error": "Origin and destination are required"}), 400

    route_response = optimize_route(origin, destination)
    if "error" in route_response:
        return jsonify(route_response), route_response.get('status_code', 500)

    return jsonify({
        **data,
        "status": "Created",
        "route": route_response
    })

@bp.route('/optimize_route', methods=['POST'])
def optimize_route_route():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    origin = data.get('origin')
    destination = data.get('destination')
    if not origin or not destination:
        return jsonify({"error": "Origin and destination are required"}), 400

    route_response = optimize_route(origin, destination)
    if "error" in route_response:
        return jsonify(route_response), route_response.get('status_code', 500)

    return jsonify(route_response)

def optimize_route(origin, destination):
    url = f"https://api.mapbox.com/directions/v5/mapbox/driving/{origin};{destination}"
    params = {
        'access_token': MAPBOX_API_TOKEN,
        'geometries': 'geojson'
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to fetch route information", "status_code": response.status_code}, response.status_code
