# app/__init__.py

from flask import Flask
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Import routes
from app import routes
