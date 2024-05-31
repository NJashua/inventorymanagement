from flask import Flask, jsonify
from app import create_app, inventory_management, db

# Improved function to create the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True  # Enable debug mode
app.register_blueprint(inventory_management)  # Register the inventory management blueprint
db.init_app(app)  # Initialize the database with the app
# Create an instance of the Flask app
app = create_app()

# Define a route to check the status of the API
@app.route('/', methods=['GET'])
def check_status():
    return jsonify({"status": "ok", "message": "API is running"}), 200

# Run the application
if __name__ == '__main__':
    app.run()
