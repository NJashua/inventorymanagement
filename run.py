from app import create_app, inventory_management, db
from flask import jsonify

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.register_blueprint(inventory_management)
    db.init_app(app)
    return app

app = create_app()

@app.route('/', methods=['GET'])
def check_status():
    return jsonify({"status": "ok", "message": "API is running"}), 200

if __name__ == '__main__':
    app.run()

