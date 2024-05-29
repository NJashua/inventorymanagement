from flask import Flask
from app.routes import bp

def inventory_management():
    app = Flask(__name__)
    app.register_blueprint(bp)
    return app
