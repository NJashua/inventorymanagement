import snowflake.connector
from flask import jsonify
import datetime

class SnowflakeDB:
    def __init__(self, config):
        self.config = config

    def get_connection(self):
        return snowflake.connector.connect(**self.config)
    
    def get_product_details_with_location(self, search_term):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            search_term = '%{}%'.format(search_term)
            
            # Command to get product details
            cursor.execute(""" 
                SELECT p.* 
                FROM PRODUCT p 
                WHERE p.PRODUCT_NAME LIKE ?
            """, (search_term,))
            products = cursor.fetchall()
            product_column_names = [desc[0].lower() for desc in cursor.description]
            products_list = [dict(zip(product_column_names, product)) for product in products]
            
            # Command to get product location details
            cursor.execute(""" 
                SELECT DISTINCT I.* 
              
