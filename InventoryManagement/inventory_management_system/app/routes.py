# # from flask import Flask, request, jsonify
# # import snowflake.connector

# # # Initialize Flask app
# # app = Flask(__name__)

# # # Snowflake connection configuration
# # snowflake_config = {
# #     'user': 'Nithin',
# #     'password': 'Nithin@2024',
# #     'account': 'bdhriyc-ke24872',
# #     'database': 'INVENTORY',
# #     'schema': 'PUBLIC'
# # }

# # # Function to establish Snowflake connection
# # def get_snowflake_connection():
# #     return snowflake.connector.connect(**snowflake_config)

# # # Route to search for products
# # @app.route('/products/search', methods=['GET'])
# # def search_products():
# #     # Extract search parameters from query string
# #     category = request.args.get('category')
# #     manufacturer_id = request.args.get('manufacturer_id')

# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Build the query based on search parameters
# #     query = "SELECT * FROM product WHERE 1=1"
# #     params = []

# #     if category:
# #         query += " AND category = %s"
# #         params.append(category)
# #     if manufacturer_id:
# #         query += " AND manufacturer_id = %s"
# #         params.append(manufacturer_id)

# #     # Execute the query
# #     cur.execute(query, params)

# #     # Fetch all products matching the search criteria
# #     products = cur.fetchall()

# #     cur.close()
# #     conn.close()

# #     return jsonify(products)

# # # Route to get all products
# # @app.route('/products', methods=['GET'])
# # def get_all_products():
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Execute query to get all products
# #     cur.execute("""
# #     SELECT * FROM product
# #     """)

# #     # Fetch all products
# #     products = cur.fetchall()

# #     cur.close()
# #     conn.close()

# #     return jsonify(products)

# # # Route to add a new product
# # @app.route('/product', methods=['POST'])
# # def add_product():
# #     # Extract product data from request JSON
# #     product_data = request.json

# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Insert new product into product table
# #     cur.execute("""
# #     INSERT INTO product (product_id, product_name, description, manufacturer_id, supplier_id, unit_cost, selling_price, quantity_available, reorder_level, category, subcategory_id, location_id, date_added) 
# #     VALUES 
# #     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# #     """, (
# #         product_data['product_id'],
# #         product_data['product_name'],
# #         product_data['description'],
# #         product_data['manufacturer_id'],
# #         product_data['supplier_id'],
# #         product_data['unit_cost'],
# #         product_data['selling_price'],
# #         product_data['quantity_available'],
# #         product_data['reorder_level'],
# #         product_data['category'],
# #         product_data['subcategory_id'],
# #         product_data['location_id'],
# #         product_data['date_added']
# #     ))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": "Product added successfully"})

# # # Route to update a product
# # @app.route('/product/<int:product_id>', methods=['PUT'])
# # def update_product(product_id):
# #     # Extract updated product data from request JSON
# #     updated_product_data = request.json

# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Update product in product table
# #     cur.execute("""
# #     UPDATE product 
# #     SET 
# #     product_name = %s, 
# #     description = %s, 
# #     manufacturer_id = %s, 
# #     supplier_id = %s, 
# #     unit_cost = %s, 
# #     selling_price = %s, 
# #     quantity_available = %s, 
# #     reorder_level = %s, 
# #     category = %s, 
# #     subcategory_id = %s, 
# #     location_id = %s, 
# #     date_added = %s
# #     WHERE product_id = %s
# #     """, (
# #         updated_product_data['product_name'],
# #         updated_product_data['description'],
# #         updated_product_data['manufacturer_id'],
# #         updated_product_data['supplier_id'],
# #         updated_product_data['unit_cost'],
# #         updated_product_data['selling_price'],
# #         updated_product_data['quantity_available'],
# #         updated_product_data['reorder_level'],
# #         updated_product_data['category'],
# #         updated_product_data['subcategory_id'],
# #         updated_product_data['location_id'],
# #         updated_product_data['date_added'],
# #         product_id
# #     ))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": f"Product with ID {product_id} updated successfully"})

# # # Route to delete a product
# # @app.route('/product/<int:product_id>', methods=['DELETE'])
# # def delete_product(product_id):
# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Delete product from product table
# #     cur.execute("""
# #     DELETE FROM product WHERE product_id = %s
# #     """, (product_id,))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": f"Product with ID {product_id} deleted successfully"})

# # if __name__ == '__main__':
# #     app.run(debug=True)


# # from flask import Flask, request, jsonify
# # import snowflake.connector

# # # Initialize Flask app
# # app = Flask(__name__)

# # # Snowflake connection configuration
# # snowflake_config = {
# #     'user': 'Nithin',
# #     'password': 'Nithin@2024',
# #     'account': 'bdhriyc-ke24872',
# #     'database': 'INVENTORY',
# #     'schema': 'PUBLIC'
# # }

# # # Function to establish Snowflake connection
# # def get_snowflake_connection():
# #     return snowflake.connector.connect(**snowflake_config)

# # # Route to search for products
# # @app.route('/products/search', methods=['GET'])
# # def search_products():
# #     # Extract search parameters from query string
# #     category = request.args.get('category')
# #     manufacturer_id = request.args.get('manufacturer_id')

# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Build the query based on search parameters
# #     query = "SELECT * FROM product WHERE 1=1"
# #     params = []

# #     if category:
# #         query += " AND category = %s"
# #         params.append(category)
# #     if manufacturer_id:
# #         query += " AND manufacturer_id = %s"
# #         params.append(manufacturer_id)

# #     # Execute the query
# #     cur.execute(query, params)

# #     # Fetch all products matching the search criteria
# #     products = cur.fetchall()

# #     cur.close()
# #     conn.close()

# #     return jsonify(products)

# # # Route to get all products
# # @app.route('/products', methods=['GET'])
# # def get_all_products():
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Execute query to get all products
# #     cur.execute("""
# #     SELECT * FROM product
# #     """)

# #     # Fetch all products
# #     products = cur.fetchall()

# #     cur.close()
# #     conn.close()

# #     return jsonify(products)

# # # Route to add a new product
# # @app.route('/product', methods=['POST'])
# # def add_product():
# #     # Extract product data from request JSON
# #     product_data = request.json

# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Insert new product into product table
# #     cur.execute("""
# #     INSERT INTO product (product_id, product_name, description, manufacturer_id, supplier_id, unit_cost, selling_price, quantity_available, reorder_level, category, subcategory_id, location_id, date_added) 
# #     VALUES 
# #     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# #     """, (
# #         product_data['product_id'],
# #         product_data['product_name'],
# #         product_data['description'],
# #         product_data['manufacturer_id'],
# #         product_data['supplier_id'],
# #         product_data['unit_cost'],
# #         product_data['selling_price'],
# #         product_data['quantity_available'],
# #         product_data['reorder_level'],
# #         product_data['category'],
# #         product_data['subcategory_id'],
# #         product_data['location_id'],
# #         product_data['date_added']
# #     ))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": "Product added successfully"})

# # # Route to update a product
# # @app.route('/product/<int:product_id>', methods=['PUT'])
# # def update_product(product_id):
# #     # Extract updated product data from request JSON
# #     updated_product_data = request.json

# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Update product in product table
# #     cur.execute("""
# #     UPDATE product 
# #     SET 
# #     product_name = %s, 
# #     description = %s, 
# #     manufacturer_id = %s, 
# #     supplier_id = %s, 
# #     unit_cost = %s, 
# #     selling_price = %s, 
# #     quantity_available = %s, 
# #     reorder_level = %s, 
# #     category = %s, 
# #     subcategory_id = %s, 
# #     location_id = %s, 
# #     date_added = %s
# #     WHERE product_id = %s
# #     """, (
# #         updated_product_data['product_name'],
# #         updated_product_data['description'],
# #         updated_product_data['manufacturer_id'],
# #         updated_product_data['supplier_id'],
# #         updated_product_data['unit_cost'],
# #         updated_product_data['selling_price'],
# #         updated_product_data['quantity_available'],
# #         updated_product_data['reorder_level'],
# #         updated_product_data['category'],
# #         updated_product_data['subcategory_id'],
# #         updated_product_data['location_id'],
# #         updated_product_data['date_added'],
# #         product_id
# #     ))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": f"Product with ID {product_id} updated successfully"})

# # # Route to delete a product
# # @app.route('/product/<int:product_id>', methods=['DELETE'])
# # def delete_product(product_id):
# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Delete product from product table
# #     cur.execute("""
# #     DELETE FROM product WHERE product_id = %s
# #     """, (product_id,))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": f"Product with ID {product_id} deleted successfully"})

# # # Route to search for sales
# # @app.route('/sales/search', methods=['GET'])
# # def search_sales():
# #     # Extract search parameters from query string
# #     product_id = request.args.get('product_id')
# #     customer_name = request.args.get('customer_name')

# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Build the query based on search parameters
# #     query = "SELECT * FROM sales WHERE 1=1"
# #     params = []

# #     if product_id:
# #         query += " AND product_id = %s"
# #         params.append(product_id)
# #     if customer_name:
# #         query += " AND customer_name = %s"
# #         params.append(customer_name)

# #     # Execute the query
# #     cur.execute(query, params)

# #     # Fetch all sales matching the search criteria
# #     sales = cur.fetchall()

# #     cur.close()
# #     conn.close()

# #     return jsonify(sales)

# # # Route to get all sales
# # @app.route('/sales', methods=['GET'])
# # def get_all_sales():
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Execute query to get all sales
# #     cur.execute("""
# #     SELECT * FROM sales
# #     """)

# #     # Fetch all sales
# #     sales = cur.fetchall()

# #     cur.close()
# #     conn.close()

# #     return jsonify(sales)

# # # Route to add a new sale
# # @app.route('/sale', methods=['POST'])
# # def add_sale():
# #     # Extract sale data from request JSON
# #     sale_data = request.json

# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Insert new sale into sales table
# #     cur.execute("""
# #     INSERT INTO sales (product_id, product_name, category, quantity_sold, sale_amount, sale_date, customer_name, payment_method) 
# #     VALUES 
# #     (%s, %s, %s, %s, %s, %s, %s, %s)
# #     """, (
# #         sale_data['product_id'],
# #         sale_data['product_name'],
# #         sale_data['category'],
# #         sale_data['quantity_sold'],
# #         sale_data['sale_amount'],
# #         sale_data['sale_date'],
# #         sale_data['customer_name'],
# #         sale_data['payment_method']
# #     ))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": "Sale added successfully"})

# # # Route to delete a sale
# # @app.route('/sale/<int:sale_id>', methods=['DELETE'])
# # def delete_sale(sale_id):
# #     # Connect to Snowflake
# #     conn = get_snowflake_connection()
# #     cur = conn.cursor()

# #     # Delete sale from sales table
# #     cur.execute("""
# #     DELETE FROM sales WHERE sale_id = %s
# #     """, (sale_id,))

# #     # Commit changes
# #     conn.commit()

# #     cur.close()
# #     conn.close()

# #     return jsonify({"message": f"Sale with ID {sale_id} deleted successfully"})

# # if __name__ == '__main__':
# #     app.run(debug=True)


# from flask import Flask, request, jsonify
# import snowflake.connector
# import json
# from decimal import Decimal
# from datetime import date

# # Initialize Flask app
# app = Flask(__name__)

# # Snowflake connection configuration
# snowflake_config = {
#     'user': 'Nithin',
#     'password': 'Nithin@2024',
#     'account': 'bdhriyc-ke24872',
#     'database': 'INVENTORY',
#     'schema': 'PUBLIC'
# }

# # Function to establish Snowflake connection
# def get_snowflake_connection():
#     return snowflake.connector.connect(**snowflake_config)

# # Function to convert list of lists to list of dictionaries

# def list_to_dict(data_list):
#     keys = [
#         'product_id', 'product_name', 'description', 'manufacturer_id', 'supplier_id',
#         'unit_cost', 'selling_price', 'quantity_available', 'reorder_level',
#         'category', 'subcategory_id', 'location_id', 'date_added'
#     ]
#     # Convert date objects to ISO formatted strings
#     return [dict(zip(keys, [item.isoformat() if isinstance(item, date) else item for item in row])) for row in data_list]

# # Route to search for products
# @app.route('/products/search', methods=['GET'])
# def search_products():
#     # Extract search parameters from query string
#     category = request.args.get('category')
#     manufacturer_id = request.args.get('manufacturer_id')

#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Build the query based on search parameters
#     query = "SELECT * FROM product WHERE 1=1"
#     params = []

#     if category:
#         query += " AND category = %s"
#         params.append(category)
#     if manufacturer_id:
#         query += " AND manufacturer_id = %s"
#         params.append(manufacturer_id)

#     # Execute the query
#     cur.execute(query, params)

#     # Fetch all products matching the search criteria
#     products_data = cur.fetchall()

#     cur.close()
#     conn.close()

#     # Convert list of lists to list of dictionaries
#     products = list_to_dict(products_data)

#     return jsonify(products)

# # Route to get all products
# @app.route('/products', methods=['GET'])
# def get_all_products():
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Execute query to get all products
#     cur.execute("""
#     SELECT * FROM product
#     """)

#     # Fetch all products
#     products_data = cur.fetchall()
    
#     # Convert list of lists to list of dictionaries
#     products = list_to_dict(products_data)

#     cur.close()
#     conn.close()

#     # Return JSON-formatted data
#     return json.dumps(products)

# # Route to add a new product
# @app.route('/product', methods=['POST'])
# def add_product():
#     # Extract product data from request JSON
#     product_data = request.json

#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Insert new product into product table
#     cur.execute("""
#     INSERT INTO product (product_id, product_name, description, manufacturer_id, supplier_id, unit_cost, selling_price, quantity_available, reorder_level, category, subcategory_id, location_id, date_added) 
#     VALUES 
#     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, (
#         product_data['product_id'],
#         product_data['product_name'],
#         product_data['description'],
#         product_data['manufacturer_id'],
#         product_data['supplier_id'],
#         product_data['unit_cost'],
#         product_data['selling_price'],
#         product_data['quantity_available'],
#         product_data['reorder_level'],
#         product_data['category'],
#         product_data['subcategory_id'],
#         product_data['location_id'],
#         product_data['date_added']
#     ))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": "Product added successfully"})

# # Route to update a product
# @app.route('/product/<int:product_id>', methods=['PUT'])
# def update_product(product_id):
#     # Extract updated product data from request JSON
#     updated_product_data = request.json

#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Update product in product table
#     cur.execute("""
#     UPDATE product 
#     SET 
#     product_name = %s, 
#     description = %s, 
#     manufacturer_id = %s, 
#     supplier_id = %s, 
#     unit_cost = %s, 
#     selling_price = %s, 
#     quantity_available = %s, 
#     reorder_level = %s, 
#     category = %s, 
#     subcategory_id = %s, 
#     location_id = %s, 
#     date_added = %s
#     WHERE product_id = %s
#     """, (
#         updated_product_data['product_name'],
#         updated_product_data['description'],
#         updated_product_data['manufacturer_id'],
#         updated_product_data['supplier_id'],
#         updated_product_data['unit_cost'],
#         updated_product_data['selling_price'],
#         updated_product_data['quantity_available'],
#         updated_product_data['reorder_level'],
#         updated_product_data['category'],
#         updated_product_data['subcategory_id'],
#         updated_product_data['location_id'],
#         updated_product_data['date_added'],
#         product_id
#     ))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": f"Product with ID {product_id} updated successfully"})

# # Route to delete a product
# @app.route('/product/<int:product_id>', methods=['DELETE'])
# def delete_product(product_id):
#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Delete product from product table
#     cur.execute("""
#     DELETE FROM product WHERE product_id = %s
#     """, (product_id,))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": f"Product with ID {product_id} deleted successfully"})

# # Route to search for sales
# @app.route('/sales/search', methods=['GET'])
# def search_sales():
#     # Extract search parameters from query string
#     product_id = request.args.get('product_id')
#     customer_name = request.args.get('customer_name')

#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Build the query based on search parameters
#     query = "SELECT * FROM sales WHERE 1=1"
#     params = []

#     if product_id:
#         query += " AND product_id = %s"
#         params.append(product_id)
#     if customer_name:
#         query += " AND customer_name = %s"
#         params.append(customer_name)

#     # Execute the query
#     cur.execute(query, params)

#     # Fetch all sales matching the search criteria
#     sales_data = cur.fetchall()

#     cur.close()
#     conn.close()

#     # Convert list of lists to list of dictionaries
#     sales = list_to_dict(sales_data)

#     return jsonify(sales)

# # Route to get all sales
# @app.route('/sales', methods=['GET'])
# def get_all_sales():
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Execute query to get all sales
#     cur.execute("""
#     SELECT * FROM sales
#     """)

#     # Fetch all sales
#     sales_data = cur.fetchall()
    
#     # Convert list of lists to list of dictionaries
#     sales = list_to_dict(sales_data)

#     cur.close()
#     conn.close()

#     # Return JSON-formatted data
#     return json.dumps(sales)

# # Route to add a new sale
# @app.route('/sale', methods=['POST'])
# def add_sale():
#     # Extract sale data from request JSON
#     sale_data = request.json

#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Insert new sale into sales table
#     cur.execute("""
#     INSERT INTO sales (product_id, product_name, category, quantity_sold, sale_amount, sale_date, customer_name, payment_method) 
#     VALUES 
#     (%s, %s, %s, %s, %s, %s, %s, %s)
#     """, (
#         sale_data['product_id'],
#         sale_data['product_name'],
#         sale_data['category'],
#         sale_data['quantity_sold'],
#         sale_data['sale_amount'],
#         sale_data['sale_date'],
#         sale_data['customer_name'],
#         sale_data['payment_method']
#     ))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": "Sale added successfully"})

# # Route to delete a sale
# @app.route('/sale/<int:sale_id>', methods=['DELETE'])
# def delete_sale(sale_id):
#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Delete sale from sales table
#     cur.execute("""
#     DELETE FROM sales WHERE sale_id = %s
#     """, (sale_id,))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": f"Sale with ID {sale_id} deleted successfully"})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import snowflake.connector
import json
from decimal import Decimal
from datetime import date
from json import JSONEncoder

# Custom JSON encoder class to handle Decimal and date objects
class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, date):
            return obj.isoformat()
        else:
            return super().default(obj)

# Initialize Flask app
app = Flask(__name__)
app.json_encoder = CustomJSONEncoder

# Snowflake connection configuration
snowflake_config = {
    'user': 'Nithin',
    'password': 'Nithin@2024',
    'account': 'bdhriyc-ke24872',
    'database': 'INVENTORY',
    'schema': 'PUBLIC'
}

# Function to establish Snowflake connection
def get_snowflake_connection():
    return snowflake.connector.connect(**snowflake_config)

# Function to convert list of lists to list of dictionaries
def list_to_dict(data_list):
    keys = [
        'product_id', 'product_name', 'description', 'manufacturer_id', 'supplier_id',
        'unit_cost', 'selling_price', 'quantity_available', 'reorder_level',
        'category', 'subcategory_id', 'location_id', 'date_added'
    ]
    return [dict(zip(keys, [item.isoformat() if isinstance(item, date) else item for item in row])) for row in data_list]

# Route to search for products
@app.route('/products/search', methods=['GET'])
def search_products():
    # Extract search parameters from query string
    category = request.args.get('category')
    manufacturer_id = request.args.get('manufacturer_id')

    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Build the query based on search parameters
    query = "SELECT * FROM product WHERE 1=1"
    params = []

    if category:
        query += " AND category = %s"
        params.append(category)
    if manufacturer_id:
        query += " AND manufacturer_id = %s"
        params.append(manufacturer_id)

    # Execute the query
    cur.execute(query, params)

    # Fetch all products matching the search criteria
    products_data = cur.fetchall()

    cur.close()
    conn.close()

    # Convert list of lists to list of dictionaries
    products = list_to_dict(products_data)

    return jsonify(products)

# Route to get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Execute query to get all products
    cur.execute("""
    SELECT * FROM product
    """)

    # Fetch all products
    products_data = cur.fetchall()
    
    # Convert list of lists to list of dictionaries
    products = list_to_dict(products_data)

    cur.close()
    conn.close()

    # Return JSON-formatted data
    return jsonify(products)

# Route to add a new product
@app.route('/product', methods=['POST'])
def add_product():
    # Extract product data from request JSON
    product_data = request.json

    # Connect to Snowflake
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Insert new product into product table
    cur.execute("""
    INSERT INTO product (product_id, product_name, description, manufacturer_id, supplier_id, unit_cost, selling_price, quantity_available, reorder_level, category, subcategory_id, location_id, date_added) 
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        product_data['product_id'],
        product_data['product_name'],
        product_data['description'],
        product_data['manufacturer_id'],
        product_data['supplier_id'],
        product_data['unit_cost'],
        product_data['selling_price'],
        product_data['quantity_available'],
        product_data['reorder_level'],
        product_data['category'],
        product_data['subcategory_id'],
        product_data['location_id'],
        product_data['date_added']
    ))

    # Commit changes
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": "Product added successfully"})

# Route to update a product
@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    # Extract updated product data from request JSON
    updated_product_data = request.json

    # Connect to Snowflake
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Update product in product table
    cur.execute("""
    UPDATE product 
    SET 
    product_name = %s, 
    description = %s, 
    manufacturer_id = %s, 
    supplier_id = %s, 
    unit_cost = %s, 
    selling_price = %s, 
    quantity_available = %s, 
    reorder_level = %s, 
    category = %s, 
    subcategory_id = %s, 
    location_id = %s, 
    date_added = %s
    WHERE product_id = %s
    """, (
        updated_product_data['product_name'],
        updated_product_data['description'],
        updated_product_data['manufacturer_id'],
        updated_product_data['supplier_id'],
        updated_product_data['unit_cost'],
        updated_product_data['selling_price'],
        updated_product_data['quantity_available'],
        updated_product_data['reorder_level'],
        updated_product_data['category'],
        updated_product_data['subcategory_id'],
        updated_product_data['location_id'],
        updated_product_data['date_added'],
        product_id
    ))

    # Commit changes
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": f"Product with ID {product_id} updated successfully"})

# Route to delete a product
@app.route('/product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # Connect to Snowflake
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Delete product from product table
    cur.execute("""
    DELETE FROM product WHERE product_id = %s
    """, (product_id,))

    # Commit changes
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": f"Product with ID {product_id} deleted successfully"})

# Route to search for sales
@app.route('/sales/search', methods=['GET'])
def search_sales():
    # Extract search parameters from query string
    product_id = request.args.get('product_id')
    customer_name = request.args.get('customer_name')

    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Build the query based on search parameters
    query = "SELECT * FROM sales WHERE 1=1"
    params = []

    if product_id:
        query += " AND product_id = %s"
        params.append(product_id)
    if customer_name:
        query += " AND customer_name = %s"
        params.append(customer_name)

    # Execute the query
    cur.execute(query, params)

    # Fetch all sales matching the search criteria
    sales_data = cur.fetchall()

    cur.close()
    conn.close()

    # Convert list of lists to list of dictionaries
    sales = list_to_dict(sales_data)

    return jsonify(sales)

# Route to get all sales
# Route to get all sales
@app.route('/sales', methods=['GET'])
def get_all_sales():
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Execute query to get all sales
    cur.execute("""
    SELECT * FROM sales
    """)

    # Fetch all sales
    sales_data = cur.fetchall()
    
    # Convert list of lists to list of dictionaries with correct key-value pairs
    sales = [
        {
            "sale_id": row[0],
            "product_id": row[1],
            "product_name": row[2],
            "category": row[3],
            "quantity_sold": row[4],
            "sale_amount": str(row[5]),  # Convert Decimal to string
            "sale_date": row[6].isoformat(),  # Convert date to ISO format string
            "customer_name": row[7],
            "payment_method": row[8]
        }
        for row in sales_data
    ]

    cur.close()
    conn.close()

    # Return JSON-formatted data
    return jsonify(sales)


# Route to add a new sale
@app.route('/sale', methods=['POST'])
def add_sale():
    # Extract sale data from request JSON
    sale_data = request.json

    # Connect to Snowflake
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Insert new sale into sales table
    cur.execute("""
    INSERT INTO sales (product_id, product_name, category, quantity_sold, sale_amount, sale_date, customer_name, payment_method) 
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        sale_data['product_id'],
        sale_data['product_name'],
        sale_data['category'],
        sale_data['quantity_sold'],
        sale_data['sale_amount'],
        sale_data['sale_date'],
        sale_data['customer_name'],
        sale_data['payment_method']
    ))

    # Commit changes
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": "Sale added successfully"})

# Route to delete a sale
@app.route('/sale/<int:sale_id>', methods=['DELETE'])
def delete_sale(sale_id):
    # Connect to Snowflake
    conn = get_snowflake_connection()
    cur = conn.cursor()

    # Delete sale from sales table
    cur.execute("""
    DELETE FROM sales WHERE sale_id = %s
    """, (sale_id,))

    # Commit changes
    conn.commit()

    cur.close()
    conn.close()

    return jsonify({"message": f"Sale with ID {sale_id} deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)


# from flask import Flask, request, jsonify
# import snowflake.connector
# import json
# from decimal import Decimal
# from datetime import date
# from json import JSONEncoder

# # Custom JSON encoder class to handle Decimal and date objects
# class CustomJSONEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Decimal):
#             return str(obj)
#         elif isinstance(obj, date):
#             return obj.isoformat()
#         else:
#             return super().default(obj)

# # Initialize Flask app
# app = Flask(__name__)
# app.json_encoder = CustomJSONEncoder

# # Snowflake connection configuration
# snowflake_config = {
#     'user': 'Nithin',
#     'password': 'Nithin@2024',
#     'account': 'bdhriyc-ke24872',
#     'database': 'INVENTORY',
#     'schema': 'PUBLIC'
# }

# # Function to establish Snowflake connection
# def get_snowflake_connection():
#     return snowflake.connector.connect(**snowflake_config)

# # Function to convert list of lists to list of dictionaries
# def list_to_dict(data_list):
#     keys = [
#         'product_id', 'product_name', 'description', 'manufacturer_id', 'supplier_id',
#         'unit_cost', 'selling_price', 'quantity_available', 'reorder_level',
#         'category', 'subcategory_id', 'location_id', 'date_added'
#     ]
#     return [dict(zip(keys, [item.isoformat() if isinstance(item, date) else item for item in row])) for row in data_list]

# # Route to handle product operations
# @app.route('/product', methods=['GET', 'POST', 'PUT', 'DELETE'])
# def product_operations():
#     if request.method == 'GET':
#         return get_all_products()
#     elif request.method == 'POST':
#         return add_product()
#     elif request.method == 'PUT':
#         return update_product(request.json['product_id'])
#     elif request.method == 'DELETE':
#         return delete_product(request.json['product_id'])

# # Route to handle sale operations
# @app.route('/sale', methods=['GET', 'POST', 'DELETE'])
# def sale_operations():
#     if request.method == 'GET':
#         return get_all_sales()
#     elif request.method == 'POST':
#         return add_sale()
#     elif request.method == 'DELETE':
#         return delete_sale(request.json['sale_id'])

# # Functions to handle product operations
# def add_product():
#     # Extract product data from request JSON
#     product_data = request.json

#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Insert new product into product table
#     cur.execute("""
#     INSERT INTO product (product_id, product_name, description, manufacturer_id, supplier_id, unit_cost, selling_price, quantity_available, reorder_level, category, subcategory_id, location_id, date_added) 
#     VALUES 
#     (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#     """, (
#         product_data['product_id'],
#         product_data['product_name'],
#         product_data['description'],
#         product_data['manufacturer_id'],
#         product_data['supplier_id'],
#         product_data['unit_cost'],
#         product_data['selling_price'],
#         product_data['quantity_available'],
#         product_data['reorder_level'],
#         product_data['category'],
#         product_data['subcategory_id'],
#         product_data['location_id'],
#         product_data['date_added']
#     ))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": "Product added successfully"})

# def update_product(product_id):
#     # Extract updated product data from request JSON
#     updated_product_data = request.json

#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Update product in product table
#     cur.execute("""
#     UPDATE product 
#     SET 
#     product_name = %s, 
#     description = %s, 
#     manufacturer_id = %s, 
#     supplier_id = %s, 
#     unit_cost = %s, 
#     selling_price = %s, 
#     quantity_available = %s, 
#     reorder_level = %s, 
#     category = %s, 
#     subcategory_id = %s, 
#     location_id = %s, 
#     date_added = %s
#     WHERE product_id = %s
#     """, (
#         updated_product_data['product_name'],
#         updated_product_data['description'],
#         updated_product_data['manufacturer_id'],
#         updated_product_data['supplier_id'],
#         updated_product_data['unit_cost'],
#         updated_product_data['selling_price'],
#         updated_product_data['quantity_available'],
#         updated_product_data['reorder_level'],
#         updated_product_data['category'],
#         updated_product_data['subcategory_id'],
#         updated_product_data['location_id'],
#         updated_product_data['date_added'],
#         product_id
#     ))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": f"Product with ID {product_id} updated successfully"})

# def delete_product(product_id):
#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Delete product from product table
#     cur.execute("""
#     DELETE FROM product WHERE product_id = %s
#     """, (product_id,))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": f"Product with ID {product_id} deleted successfully"})

# def get_all_products():
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Execute query to get all products
#     cur.execute("""
#     SELECT * FROM product
#     """)

#     # Fetch all products
#     products_data = cur.fetchall()
    
#     # Convert list of lists to list of dictionaries
#     products = list_to_dict(products_data)

#     cur.close()
#     conn.close()

#     # Return JSON-formatted data
#     return jsonify(products)

# # Functions to handle sale operations
# def add_sale():
#     # Extract sale data from request JSON
#     sale_data = request.json

#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Insert new sale into sales table
#     cur.execute("""
#     INSERT INTO sales (product_id, product_name, category, quantity_sold, sale_amount, sale_date, customer_name, payment_method) 
#     VALUES 
#     (%s, %s, %s, %s, %s, %s, %s, %s)
#     """, (
#         sale_data['product_id'],
#         sale_data['product_name'],
#         sale_data['category'],
#         sale_data['quantity_sold'],
#         sale_data['sale_amount'],
#         sale_data['sale_date'],
#         sale_data['customer_name'],
#         sale_data['payment_method']
#     ))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": "Sale added successfully"})

# def delete_sale(sale_id):
#     # Connect to Snowflake
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Delete sale from sales table
#     cur.execute("""
#     DELETE FROM sales WHERE sale_id = %s
#     """, (sale_id,))

#     # Commit changes
#     conn.commit()

#     cur.close()
#     conn.close()

#     return jsonify({"message": f"Sale with ID {sale_id} deleted successfully"})

# def get_all_sales():
#     conn = get_snowflake_connection()
#     cur = conn.cursor()

#     # Execute query to get all sales
#     cur.execute("""
#     SELECT * FROM sales
#     """)

#     # Fetch all sales
#     sales_data = cur.fetchall()
    
#     # Convert list of lists to list of dictionaries with correct key-value pairs
#     sales = [
#         {
#             "sale_id": row[0],
#             "product_id": row[1],
#             "product_name": row[2],
#             "category": row[3],
#             "quantity_sold": row[4],
#             "sale_amount": str(row[5]),  # Convert Decimal to string
#             "sale_date": row[6].isoformat(),  # Convert date to ISO format string
#             "customer_name": row[7],
#             "payment_method": row[8]
#         }
#         for row in sales_data
#     ]

#     cur.close()
#     conn.close()

#     # Return JSON-formatted data
#     return jsonify(sales)

# if __name__ == '__main__':
#     app.run(debug=True)
