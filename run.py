from app import inventory_management
from flask import jsonify
from app import db

app = inventory_management()
@app.route('/', methods=['GET'])
def check_status():
    return jsonify({"status": "ok", "message": "API is running"}), 200

if __name__ == '__main__':
    app.run(debug=True)