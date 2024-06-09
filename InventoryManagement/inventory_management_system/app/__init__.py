from flask import Flask
from app.routes import bp
from app import db

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True  # Enable debug mode
    app.register_blueprint(bp)  # Register the blueprint
    db.init_app(app)  # Initialize the database with the app
    return app
