from flask import Blueprint, request, make_response
from app.db import SnowflakeDB
from app.utils import error_response

# Creating Blueprint for the routes
bp = Blueprint('routes', __name__)

# Configuration for Snowflake
snowflake_config = {
    'user': 'Nithin',
    'password': 'Nithin@2
