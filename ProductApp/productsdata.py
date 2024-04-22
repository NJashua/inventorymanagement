from flask import Flask, render_template
import snowflake.connector

# Snowflake connection parameters
snowflake_config = {
    'user': 'NITHIN',
    'password': 'Nithin@2024',
    'account': 'azqcwil-tf37140',
    'database': 'PRODUCTSDATA',
    'schema': 'PRODUCTSDATA.PUBLIC'
}

app = Flask(__name__)

# Function to fetch product data from Snowflake
def get_products():
    products = []
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(**snowflake_config)
        cursor = conn.cursor()

        # Execute SQL query to fetch product data
        cursor.execute("SELECT * FROM PRODUCTS")

        # Fetch all rows
        products = cursor.fetchall()

    except Exception as e:
        print("An error occurred while fetching product data:", e)
    finally:
        # Close connection
        cursor.close()
        conn.close()

    return products

# Function to fetch product by name
def get_product_by_name(name):
    product = None
    try:
        # Connect to Snowflake
        conn = snowflake.connector.connect(**snowflake_config)
        cursor = conn.cursor()

        # Execute SQL query to fetch product data by name
        cursor.execute("SELECT * FROM PRODUCTS WHERE NAME = %s", (name,))

        # Fetch the row
        product = cursor.fetchone()

    except Exception as e:
        print("An error occurred while fetching product by name:", e)
    finally:
        # Close connection
        cursor.close()
        conn.close()

    return product

@app.route('/')
def index():
    # Fetch product data
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/product/<string:name>')
def product(name):
    # Fetch product data by name
    product = get_product_by_name(name)
    return render_template('product.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
