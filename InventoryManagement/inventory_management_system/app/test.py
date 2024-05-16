import snowflake.connector

# Snowflake connection parameters
snowflake_credentials = {
    'user': 'Nithin',
    'password': 'Nithin@2024',
    'account': 'bdhriyc-ke24872',
    'database': 'INVENTORY',
    'schema': 'PUBLIC'
}

# Function to establish connection to Snowflake
def connect_to_snowflake(credentials):
    conn = snowflake.connector.connect(
        user=credentials['user'],
        password=credentials['password'],
        account=credentials['account'],
        database=credentials['database'],
        schema=credentials['schema']
    )
    return conn

# Function to insert data into Suppliers table using data from Product table
# Function to insert data into Suppliers table using data from Product table
def insert_into_suppliers_from_product(conn):
    cursor = conn.cursor()

    # Query the Product table to get the necessary values
    cursor.execute("""
        SELECT SUPPLIER_ID, PRODUCT_NAME, CATEGORY
        FROM PRODUCT
    """)
    
    # Fetch the result
    results = cursor.fetchall()
    if results:
        for result in results:
            supplier_id, product_name, category = result

            # Insert data into Suppliers table
            cursor.execute("""
                INSERT INTO Suppliers (SUPPLIERID, PRODUCT_NAME, SUPPLIERNAME, CATEGORY)
                VALUES (%s, %s, 'James Bond', %s)
            """, (supplier_id, product_name, category))
            conn.commit()
        print("Data inserted successfully into Suppliers table.")
    else:
        print("No products found in the Product table.")

    cursor.close()


# Connect to Snowflake
conn = connect_to_snowflake(snowflake_credentials)

# Insert values into Suppliers table from Product table
insert_into_suppliers_from_product(conn)

# Close connection
conn.close()
