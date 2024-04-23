from flask import Flask, render_template, session, redirect, url_for
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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

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

# Function to add product to cart
def add_to_cart(name):
    product = get_product_by_name(name)
    if product:
        if 'cart' not in session:
            session['cart'] = []

        session['cart'].append(product)
        session.modified = True  # Set session.modified to True after modifying the session
        print("Product added to cart:", product)

# Function to remove product from cart
def remove_from_cart(name):
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item[1] != name]
        session.modified = True  # Set session.modified to True after modifying the session

# Function to get cart contents
def get_cart():
    return session.get('cart', [])

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

@app.route('/add_to_cart/<string:name>', methods=['POST'])
def add_to_cart_route(name):
    add_to_cart(name)
    return redirect(url_for('index'))

@app.route('/remove_from_cart/<string:name>', methods=['POST'])
def remove_from_cart_route(name):
    remove_from_cart(name)
    return redirect(url_for('cart'))

@app.route('/cart')
def cart():
    cart_contents = get_cart()
    print("Cart contents:", cart_contents)
    return render_template('cart.html', cart_contents=cart_contents)

if __name__ == '__main__':
    app.run(debug=True)
