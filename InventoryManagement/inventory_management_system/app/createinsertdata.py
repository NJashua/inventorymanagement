# import snowflake.connector
# import random
# from datetime import datetime, timedelta

# # Define the Config class
# class Config:
#     SNOWFLAKE_USER = 'Nithin'
#     SNOWFLAKE_PASSWORD = 'Nithin@2024'
#     SNOWFLAKE_ACCOUNT = 'bdhriyc-ke24872'
#     SNOWFLAKE_DATABASE = 'INVENTORY'
#     SNOWFLAKE_SCHEMA = 'PUBLIC'

# # Connect to Snowflake
# conn = snowflake.connector.connect(
#     user=Config.SNOWFLAKE_USER,
#     password=Config.SNOWFLAKE_PASSWORD,
#     account=Config.SNOWFLAKE_ACCOUNT,
#     database=Config.SNOWFLAKE_DATABASE,
#     schema=Config.SNOWFLAKE_SCHEMA
# )

# # Create cursor
# cur = conn.cursor()

# # Create product table with category column
# cur.execute("""
# CREATE TABLE product (
#     product_id INT PRIMARY KEY,
#     product_name VARCHAR(100) NOT NULL,
#     description TEXT,
#     manufacturer_id INT,
#     supplier_id INT,
#     unit_cost DECIMAL(10, 2),
#     selling_price DECIMAL(10, 2),
#     quantity_available INT,
#     reorder_level INT,
#     category VARCHAR(50),
#     subcategory_id INT,
#     location_id INT,
#     date_added DATE,
#     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
#     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
# )
# """)

# # Define real dummy data for products with same category names and subcategory IDs
# dummy_data = [
#     (1, 'Laptop', 'Powerful laptop with SSD', 101, 201, 800.00, 1200.00, 50, 10, 'Electronics', 1, 1, '2023-05-10'),
#     (2, 'Smartphone', 'Latest model smartphone', 102, 202, 600.00, 900.00, 100, 20, 'Electronics', 1, 2, '2023-05-12'),
#     (3, 'Headphones', 'Noise-canceling headphones', 103, 203, 100.00, 150.00, 200, 30, 'Electronics', 1, 3, '2023-05-15'),
#     (4, 'Smartwatch', 'Fitness tracker smartwatch', 104, 204, 150.00, 250.00, 80, 15, 'Electronics', 1, 4, '2023-05-18'),
#     (5, 'Rice', 'Premium Basmati Rice', 105, 205, 20.00, 30.00, 200, 50, 'Grocery', 2, 5, '2023-05-20'),
#     (6, 'T-shirt', 'Cotton T-shirt for men', 106, 206, 10.00, 20.00, 100, 20, 'Clothing', 3, 6, '2023-05-22')
# ]

# # Insert dummy data into product table
# cur.executemany("""
# INSERT INTO product (product_id, product_name, description, manufacturer_id, supplier_id, unit_cost, selling_price, quantity_available, reorder_level, category, subcategory_id, location_id, date_added) 
# VALUES 
# (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
# """, dummy_data)

# # Commit changes
# conn.commit()

# # Close cursor and connection
# cur.close()
# conn.close()


import snowflake.connector
import random
from datetime import datetime, timedelta

# Define the Config class
data = {
    'user': 'Nithin',
    'password': 'Nithin@2024',
    'account': 'bdhriyc-ke24872',
    'database': 'INVENTORY',
    'schema': 'PUBLIC'
}

# Connect to Snowflake
conn = snowflake.connector.connect(**data)

# Create cursor
cur = conn.cursor()

# Create sales table
cur.execute("""
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT AUTOINCREMENT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    quantity_sold INT,
    sale_amount DECIMAL(10, 2),
    sale_date DATE,
    customer_name VARCHAR(100),
    payment_method VARCHAR(50),
    FOREIGN KEY (product_id) REFERENCES product (product_id)
)
""")

# Query product table to get product_id, product_name, category, and selling_price
cur.execute("""
SELECT p.product_id, p.product_name, p.category, p.selling_price, p.quantity_available 
FROM product p
""")

# Fetch all rows
product_data = cur.fetchall()

# Check if product_data is not empty
if product_data:
    # Define dummy sales data with corresponding product_id, quantity_sold, and sale_amount
    dummy_sales_data = []
    for product in product_data:
        product_id = product[0]
        product_name = product[1]
        category = product[2]
        selling_price = product[3]
        available_quantity = product[4]
        # Generate random quantity sold within available quantity
        quantity_sold = random.randint(1, min(10, available_quantity))
        # Calculate sale amount based on selling price and quantity sold
        sale_amount = round(quantity_sold * selling_price, 2)
        # Generate random sale date within the last 30 days
        sale_date = datetime.now().date() - timedelta(days=random.randint(1, 30))
        # Generate random customer name
        customer_name = "Customer" + str(random.randint(1, 1000))
        # Select random payment method
        payment_method = random.choice(["Cash", "Credit Card", "PayPal"])
        # Append data to dummy_sales_data
        dummy_sales_data.append((product_id, product_name, category, quantity_sold, sale_amount, sale_date, customer_name, payment_method))

    # Insert dummy data into sales table
    cur.executemany("""
    INSERT INTO sales (product_id, product_name, category, quantity_sold, sale_amount, sale_date, customer_name, payment_method)
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s, %s)
    """, dummy_sales_data)

    # Commit changes
    conn.commit()
    print("Data inserted into sales table successfully.")
else:
    print("No product data found.")

# Close cursor and connection
cur.close()
conn.close()
