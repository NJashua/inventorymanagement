import snowflake.connector

# Snowflake connection parameters
snowflake_config = {
    'user': 'NITHIN',
    'password': 'Nithin@2024',
    'account': 'azqcwil-tf37140',
    'database': 'PRODUCTSDATA', 
    'schema': 'PRODUCTSDATA.PUBLIC' 
}

try:
    # Connect to Snowflake
    conn = snowflake.connector.connect(**snowflake_config)
    cursor = conn.cursor()

    # Function to insert product details
    def insert_product(product_id, name, quantity, price, description, image_url):
        cursor.execute("INSERT INTO PRODUCTS (PRODUCT_ID, NAME, QUANTITY, PRICE, DESCRIPTION, IMAGE_URL) VALUES (%s, %s, %s, %s, %s, %s)",
                       (product_id, name, quantity, price, description, image_url))
        conn.commit()

    # Example usage
    insert_product(1, 'Vivo V29', 5, 25999, 'mobile for good camera with best features', 'https://www.91-img.com/gallery_images_uploads/c/d/cdd9c8786c37fbc15e675fe6da9e507391581a55.JPG?tr=h-550,w-0,c-at_max')

    # Close the connection
    cursor.close()
    conn.close()

except snowflake.connector.errors.ProgrammingError as e:
    print("Snowflake programming error:", e)
except snowflake.connector.errors.DatabaseError as e:
    print("Snowflake database error:", e)
except snowflake.connector.errors.ForbiddenError as e:
    print("Snowflake forbidden error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
