import uuid
import snowflake.connector
from flask import Flask, jsonify, request

app = Flask(__name__)

snowflake_config = {
    'user': 'Nithin',
    'password': 'Nithin@2024',
    'account': 'bdhriyc-ke24872',
    'database': 'INVENTORY',
    'schema': 'PUBLIC'
}

class SnowflakeDB:
    def __init__(self, config):
        self.config = config

    def get_connection(self):
        connection = snowflake.connector.connect(**self.config)
        return connection

    def order_service_details(self, data):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()

            order_id = str(uuid.uuid4())
            product_name = data.get('product_name')
            number_shipped = data.get('number_shipped')
            order_date = data.get('order_date')

            if not order_id or not product_name or not number_shipped or not order_date:
                return jsonify({"error": "Missing required fields"}), 400

            cursor.execute("SELECT QUANTITY_AVAILABLE FROM PRODUCT WHERE PRODUCT_NAME = %s", (product_name,))
            product = cursor.fetchone()

            if not product:
                return jsonify({"error": f"Product {product_name} not found"}), 404

            current_quantity = product[0]

            if current_quantity < number_shipped:
                return jsonify({'error': f'Not enough quantity for product {product_name}'}), 404

            new_quantity = current_quantity - number_shipped

            cursor.execute(""" UPDATE PRODUCT SET QUANTITY_AVAILABLE = %s WHERE PRODUCT_NAME = %s """, (new_quantity, product_name))

            cursor.execute(""" INSERT INTO ORDERS (ORDERID, PRODUCTNAME, NUMBERSHIPPED, ORDERDATE) 
                                VALUES (%s, %s, %s, %s)""", (order_id, product_name, number_shipped, order_date))

            connection.commit()
            return jsonify({'Message': 'Order placed product quantity added successfully'})
        except snowflake.connector.Error as e:
            return jsonify({"error": str(e)}), 500
        finally:
            cursor.close()
            connection.close()

    def display_products_details(self):
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM PRODUCT")
            products = cursor.fetchall()
            column_names = [desc[0] for desc in cursor.description]
            products_list = [dict(zip(column_names, product)) for product in products]
            return jsonify(products_list)
        except snowflake.connector.Error as e:
            return jsonify({'error': str(e)})
        finally:
            cursor.close()
            conn.close()


@app.route('/order_service', methods=['POST'])
def order_service():
    snowflake_db = SnowflakeDB(snowflake_config)
    data = request.get_json()
    return snowflake_db.order_service_details(data)


@app.route('/display_products', methods=['GET'])
def display_products():
    snowflake_db = SnowflakeDB(snowflake_config)
    return snowflake_db.display_products_details()


if __name__ == '__main__':
    app.run(debug=True)
