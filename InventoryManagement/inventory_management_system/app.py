from flask import Flask, jsonify, render_template
from app.routes import bp
from app.db import SnowflakeDB

def create_app():
    app = Flask(__name__)

    # Configuration for Snowflake
    snowflake_config = {
        'user': 'Nithin',
        'password': 'Nithin@2024',
        'account': 'bdhriyc-ke24872',
        'database': 'INVENTORY',
        'schema': 'PUBLIC'
    }

    # Initialize SnowflakeDB instances
    db = SnowflakeDB(snowflake_config)
    app.config['SnowflakeDB'] = db

    # Register blueprints
    app.register_blueprint(bp)
    @app.route('/', methods=['GET'])
    def check_status():
        return jsonify({"status": "ok", "message": "API is running"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
