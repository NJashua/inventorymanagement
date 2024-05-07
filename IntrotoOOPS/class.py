"""import pandas as pd
import uuid

class Product:
    def __init__(self, name, price, quantity, rating):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rating = rating
        return

class Inventory:
    number_of_products = 0 
    products = []
    discount = 5
    cart_items = []

    def __init__(self, name, price, quantity, rating):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rating = rating
        Inventory.number_of_products += 1

    @classmethod
    def add_product(cls, name, price, quantity, rating):
        cls.products.append(Product(name, price, quantity, rating))
        print("Product added successfully")



    @classmethod
    def apply_discount(cls, price):
        discount_price = price - (price * (cls.discount / 100))
        return discount_price
    
    def add_cart(self, product):
        item = {"name": product.name, "price": product.price}
        Inventory.cart_items.append(item)
        print(f"Item {product.name} added into cart successfully")
        return item

    
    def remove_cart_item(self, name):
        for item in Inventory.cart_items:
            if item["name"] == name:
                Inventory.cart_items.remove(item)
                print(f"Item {name} deleted successfully from the cart")
                return
        print("No product found in the cart with the given name")

    @classmethod
    def display_cart_items(cls):
        if not cls.cart_items:
            print("Cart is empty")
        else:
            print("Cart Items: ")
            for item in cls.cart_items:
                print(f'{item["name"]}: ${item["price"]}, discount price: {cls.apply_discount(item["price"])}')

    
    @classmethod
    def display_products_table(cls):
        df = pd.DataFrame([[p.name, p.price, p.quantity, p.rating, cls.apply_discount(p.price)] for p in cls.products],
                          columns=['Name', 'Price', 'Quantity', 'Rating', 'Discounted Price'],
                          index=[i+1 for i in range(len(cls.products))])
        print(df)

    def get_total_price(self):
        total_price = 0
        for item in Inventory.products:
            total_price += item.price * item.quantity
        return total_price

class Ecommerce(Inventory):
    customers = []
    customer_id_count = 1000
    orders = []

    @classmethod
    def add_customer(cls, name, address, phonenum):
        customer_id = str(uuid.uuid4())[:5]
        email = name.replace(" ", "").lower() + "@gmail.com"
        customer_info = {"customer_id": customer_id, "name": name, "address": address, "number": phonenum}
        cls.customers.append(customer_info)
        print(f"Customer {name} added successfully with id {customer_id}")

    @classmethod
    def view_customers(cls):
        if not cls.customers:
            print("No customers found.")
        else:
            print("Customers: ")
            for customer in cls.customers:
                print(customer)
    
    @classmethod
    def buy_process_order(cls, customer_name, product_name, quantity):
        product = None
        customer = None

        for buyer in cls.customers:
            if buyer['name'] == customer_name:
                customer = buyer
                break
        if customer is None:
            print("Customer not found")
            return

        for prod in Inventory.products:
            if prod.name == product_name:
                product = prod
                break
        if product is None:
            print("Product not found")
            return

        if product.quantity < quantity:
            print("Insufficient quantity")
            return
        
        total_price = quantity * product.price
        order = {"customer_id": customer['customer_id'], "product_name": product_name, "quantity": quantity, "total_price": total_price}
        cls.orders.append(order)
        product.quantity -= quantity

        print(f"Product {product_name} purchased successfully by {customer_name} with id {customer['customer_id']} and total price is {total_price}")

        total_amount = sum(o["total_price"] for o in cls.orders if o["customer_id"] == customer['customer_id'])
        print(f"Total amount to be paid by customer {customer_name}: ${total_amount}")

        print(f"Shipping orders for customer {customer_name}:")
        customer_orders = [o for o in cls.orders if o["customer_id"] == customer['customer_id']]
        for o in customer_orders:
            print(o)
        
    @classmethod
    def payment_shipment(cls, customer_name):
        customer = None
        for buyer in cls.customers:
            if buyer['name'] == customer_name:
                customer = buyer
                break
        if customer is None:
            print("Customer not found buddy...:)")
            return
        
        total_amount = sum(o['total_price'] for o in cls.orders if o['customer_id'] == customer['customer_id'])
        print(f"Total amount to be paid by customer {customer_name} : {total_amount}")
        print("Payment Done..:)")

        print(f'Shipping orders for customer {customer_name}')
        customer_orders = [o for o in cls.orders if o['customer_id'] == customer['customer_id']]
        for o in customer_orders:
            print(o)

        print(f"Order shipped to {customer['address']}")

# Switch case for user input

def main():
    while True:
        print("1. Add Product")
        print("2. Add Customer")
        print("3. Process Order")
        print("4. Display Products Table")
        print("5. Display Cart Items")
        print("6. View Customers")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
    # Add Product
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))  # Convert to float
            quantity = int(input("Enter product quantity: "))  # Convert to int
            rating = float(input("Enter product rating: "))  # Convert to float
            Inventory.add_product(name, price, quantity, rating)

            
            add_to_cart = input("Do you want to add this product to the cart? (yes/no): ").lower()
            if add_to_cart == "yes":
                instance_1 = Inventory("", 0, 0, 0)
                product = Product(name, price, quantity, rating)
                Inventory.add_cart(name, price)


        elif choice == "2":
            # Add Customer
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            phonenum = input("Enter customer phone number: ")
            Ecommerce.add_customer(name, address, phonenum)  # corrected line

        elif choice == "3":
            # Process Order
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            Ecommerce.buy_process_order(customer_name, product_name, quantity)

        elif choice == "4":
            # Display Products Table
            Inventory.display_products_table()

        elif choice == "5":
            # Display Cart Items
            Inventory.display_cart_items()

        elif choice == "6":
            # View Customers
            Ecommerce.view_customers()
        
        elif choice == "7":
            # Exit
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

main()




products = [
    ["Nike Air Zoom Pegasus 38", 120, 50, 4.8],
    ["Apple MacBook Pro (13-inch)", 1299, 100, 4.9],
    ["Sony WH-1000XM4 Wireless Headphones", 349.99, 30, 4.7],
    ["Samsung 55-inch QLED 4K Smart TV", 1099.99, 20, 4.6],
    ["Instant Pot Duo 7-in-1 Electric Pressure Cooker", 99.95, 80, 4.8],
    ["Adidas Ultraboost 21 Running Shoes", 180, 40, 4.7],
    ["Amazon Echo Dot (4th Gen)", 49.99, 120, 4.6],
    ["GoPro HERO9 Black", 449.99, 25, 4.8],
    ["KitchenAid Artisan Stand Mixer", 399.99, 60, 4.9],
    ["Samsung Galaxy S21 Ultra 5G", 1199.99, 35, 4.7],
    ["Bose QuietComfort 35 II Wireless Headphones", 299.95, 50, 4.8],
    ["Dyson V11 Torque Drive Cordless Vacuum", 699.99, 15, 4.6],
    ["Canon EOS Rebel T7 DSLR Camera", 499.99, 70, 4.7],
    ["Fitbit Charge 4 Fitness Tracker", 129.95, 90, 4.5],
    ["LG 27-inch UltraGear QHD Gaming Monitor", 399.99, 40, 4.8],
    ["Apple AirPods Pro", 249.99, 80, 4.9],
    ["Nintendo Switch", 299.99, 60, 4.8],
    ["Samsung Galaxy Watch 3 (45mm)", 429.99, 25, 4.7],
    ["Sony PlayStation 5", 499.99, 30, 4.8],
    ["Razer BlackWidow Elite Mechanical Gaming Keyboard", 169.99, 45, 4.7],
    ["Keurig K-Elite Single Serve Coffee Maker", 169.99, 55, 4.6],
    ["Fitbit Versa 3 Smartwatch", 229.95, 40, 4.7],
    ["LG CX 65-inch OLED 4K Smart TV", 1999.99, 10, 4.9],
    ["Microsoft Surface Laptop 4", 1299.99, 30, 4.7],
    ["Samsung Galaxy Buds Pro", 199.99, 50, 4.8],
    ["Garmin Forerunner 945 GPS Running Watch", 599.99, 20, 4.7],
    ["Anker Soundcore Liberty Air 2 Pro True Wireless Earbuds", 129.99, 70, 4.6],
    ["ASUS ROG Strix Scar 15 Gaming Laptop", 2199.99, 15, 4.8],
    ["Vitamix 5200 Blender", 449.95, 25, 4.9],
    ["Google Nest Hub Max", 229.99, 35, 4.7],
    ["Fitbit Inspire 2 Fitness Tracker", 99.95, 65, 4.5],
    ["JBL Charge 4 Portable Bluetooth Speaker", 139.95, 50, 4.7],
    ["LG OLED65C1PUA 65-inch OLED 4K Smart TV", 2499.99, 5, 4.9],
    ["Microsoft Xbox Series X", 499.99, 25, 4.8],
    ["Logitech MX Master 3 Wireless Mouse", 99.99, 60, 4.8],
    ["Amazon Kindle Paperwhite", 129.99, 75, 4.6],
    ["Sennheiser Momentum 3 Wireless Noise-Canceling Headphones", 399.95, 30, 4.8],
    ["Dell XPS 15 Laptop", 1899.99, 20, 4.7],
    ["Fujifilm Instax Mini 11 Instant Camera", 69.95, 85, 4.6],
    ["Roku Ultra 4K Streaming Media Player", 99.99, 45, 4.7],
    ["Apple Watch Series 6 (GPS + Cellular)", 499.99, 40, 4.9],
    ["Nikon D850 DSLR Camera", 2999.99, 10, 4.8],
    ["Breville Smart Oven Air Fryer", 399.95, 30, 4.9],
    ["Samsung 75-inch QLED 8K Smart TV", 3999.99, 5, 4.9],
    ["Sonos One (Gen 2) Smart Speaker", 199.99, 40, 4.7],
    ["ASUS ROG Swift 27-inch Gaming Monitor", 699.99, 20, 4.8],
    ["Google Pixel 5", 699.99, 30, 4.7],
    ["Microsoft Surface Pro 7", 899.99, 25, 4.8],
    ["Nespresso VertuoPlus Coffee and Espresso Maker", 199.99, 50, 4.6],
    ["LG Gram 17 Laptop", 1499.99, 15, 4.7],
    ["Fitbit Sense Advanced Smartwatch", 299.95, 35, 4.8],
    ["DJI Mavic Air 2 Drone", 799.00, 20, 4.8],
]


import pandas as pd
import uuid

class Product:
    def __init__(self, name, price, quantity, rating):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rating = rating

class Inventory:
    number_of_products = 0 
    products = []
    discount = 5
    cart_items = []

    @classmethod
    def add_product(cls, product):
        cls.products.append(product)
        print("Product added successfully")

    @classmethod
    def apply_discount(cls, price):
        discount_price = price - (price * (cls.discount / 100))
        return discount_price   
    
    def add_cart(self, product):
        item = {"name": product.name, "price": product.price}
        Inventory.cart_items.append(item)
        print(f"Item {product.name} added into cart successfully")
        return item


    def remove_cart_item(self, name):
        for item in Inventory.cart_items:
            if item["name"] == name:
                Inventory.cart_items.remove(item)
                print(f"Item {name} deleted successfully from the cart")
                return
        print("No product found in the cart with the given name")

    @classmethod
    def display_cart_items(cls):
        if not cls.cart_items:
            print("Cart is empty")
        else:
            print("Cart Items: ")
            for item in cls.cart_items:
                print(f'{item["name"]}: ${item["price"]}, discount price: {cls.apply_discount(item["price"])}')

    @classmethod
    def display_products_table(cls):
        df = pd.DataFrame([[p.name, p.price, p.quantity, p.rating, cls.apply_discount(p.price)] for p in cls.products],
                          columns=['Name', 'Price', 'Quantity', 'Rating', 'Discounted Price'],
                          index=[i+1 for i in range(len(cls.products))])
        print(df)

class Ecommerce(Inventory):
    customers = []
    customer_id_count = 1000
    orders = []

    @classmethod
    def add_customer(cls, name, address, phonenum):
        customer_id = str(uuid.uuid4())[:5]
        email = name.replace(" ", "").lower() + "@gmail.com"
        customer_info = {"customer_id": customer_id, "name": name, "address": address, "number": phonenum}
        cls.customers.append(customer_info)
        print(f"Customer {name} added successfully with id {customer_id}")

    @classmethod
    def view_customers(cls):
        if not cls.customers:
            print("No customers found.")
        else:
            print("Customers: ")
            for customer in cls.customers:
                print(customer)
    
    @classmethod
    def buy_process_order(cls, customer_name, product_name, quantity):
        product = None
        customer = None

        for buyer in cls.customers:
            if buyer['name'] == customer_name:
                customer = buyer
                break
        if customer is None:
            print("Customer not found")
            return

        for prod in Inventory.products:
            if prod.name == product_name:
                product = prod
                break
        if product is None:
            print("Product not found")
            return

        if product.quantity < quantity:
            print("Insufficient quantity")
            return
        
        total_price = quantity * product.price
        order = {"customer_id": customer['customer_id'], "product_name": product_name, "quantity": quantity, "total_price": total_price}
        cls.orders.append(order)
        product.quantity -= quantity

        print(f"Product {product_name} purchased successfully by {customer_name} with id {customer['customer_id']} and total price is {total_price}")

        total_amount = sum(o["total_price"] for o in cls.orders if o["customer_id"] == customer['customer_id'])
        print(f"Total amount to be paid by customer {customer_name}: ${total_amount}")

        print(f"Shipping orders for customer {customer_name}:")
        customer_orders = [o for o in cls.orders if o["customer_id"] == customer['customer_id']]
        for o in customer_orders:
            print(o)
        
    @classmethod
    def payment_shipment(cls, customer_name):
        customer = None
        for buyer in cls.customers:
            if buyer['name'] == customer_name:
                customer = buyer
                break
        if customer is None:
            print("Customer not found buddy...:)")
            return
        
        total_amount = sum(o['total_price'] for o in cls.orders if o['customer_id'] == customer['customer_id'])
        print(f"Total amount to be paid by customer {customer_name} : {total_amount}")
        print("Payment Done..:)")

        print(f'Shipping orders for customer {customer_name}')
        customer_orders = [o for o in cls.orders if o['customer_id'] == customer['customer_id']]
        for o in customer_orders:
            print(o)

        print(f"Order shipped to {customer['address']}")

# Products details
products = [
    ["Nike Air Zoom Pegasus 38", 120, 50, 4.8],
    ["Apple MacBook Pro (13-inch)", 1299, 100, 4.9],
    ["Sony WH-1000XM4 Wireless Headphones", 349.99, 30, 4.7],
    ["Samsung 55-inch QLED 4K Smart TV", 1099.99, 20, 4.6],
    ["Instant Pot Duo 7-in-1 Electric Pressure Cooker", 99.95, 80, 4.8],
    ["Adidas Ultraboost 21 Running Shoes", 180, 40, 4.7],
    ["Amazon Echo Dot (4th Gen)", 49.99, 120, 4.6],
    ["GoPro HERO9 Black", 449.99, 25, 4.8],
    ["KitchenAid Artisan Stand Mixer", 399.99, 60, 4.9],
    ["Samsung Galaxy S21 Ultra 5G", 1199.99, 35, 4.7],
    # Add more products here if needed
]

# Initialize products in Inventory
for item in products:
    Inventory.add_product(Product(*item))

# Switch case for user input
def main():
    while True:
        print("1. Add Customer")
        print("2. Process Order")
        print("3. Display Products Table")
        print("4. Display Cart Items")
        print("5. View Customers")
        print("6. Add cart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Customer
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            phonenum = input("Enter customer phone number: ")
            Ecommerce.add_customer(name, address, phonenum)  

        elif choice == "2":
            # Process Order
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            Ecommerce.buy_process_order(customer_name, product_name, quantity)

        elif choice == "3":
            # Display Products Table
            Inventory.display_products_table()

        elif choice == "4":
            # Display Cart Items
            Inventory.display_cart_items()

        elif choice == "5":
            # View Customers
            Ecommerce.view_customers()

        elif choice == '6':
            product_name = input("Enter product name: ")
            for product in Inventory.products:
                if product.name == product_name:
                    Inventory.add_cart(product)
                break
            else:
                print("Product not found.")

        
        elif choice == "7":
            # Exit
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

main()
"""

import pandas as pd
import uuid

class Product:
    def __init__(self, name, price, quantity, rating):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.rating = rating

class Inventory:
    number_of_products = 0 
    products = []
    discount = 5
    cart_items = []

    @classmethod
    def add_product(cls, product):
        cls.products.append(product)
        print("Product added successfully")

    @classmethod
    def apply_discount(cls, price):
        discount_price = price - (price * (cls.discount / 100))
        return discount_price
    
    @classmethod
    def add_cart(cls, product):
        item = {"name": product.name, "price": product.price}
        cls.cart_items.append(item)
        print(f"Item {product.name} added into cart successfully")
        return item


    def remove_cart_item(self, name):
        for item in Inventory.cart_items:
            if item["name"] == name:
                Inventory.cart_items.remove(item)
                print(f"Item {name} deleted successfully from the cart")
                return
        print("No product found in the cart with the given name")

    @classmethod
    def display_cart_items(cls):
        if not cls.cart_items:
            print("Cart is empty")
        else:
            print("Cart Items: ")
            for item in cls.cart_items:
                print(f'{item["name"]}: ${item["price"]}, discount price: {cls.apply_discount(item["price"])}')

    @classmethod
    def display_products_table(cls):
        df = pd.DataFrame([[p.name, p.price, p.quantity, p.rating, cls.apply_discount(p.price)] for p in cls.products],
                          columns=['Name', 'Price', 'Quantity', 'Rating', 'Discounted Price'],
                          index=[i+1 for i in range(len(cls.products))])
        print(df)

class Ecommerce(Inventory):
    customers = []
    customer_id_count = 1000
    orders = []

    @classmethod
    def add_customer(cls, name, address, phonenum):
        customer_id = str(uuid.uuid4())[:5]
        email = name.replace(" ", "").lower() + "@gmail.com"
        customer_info = {"customer_id": customer_id, "name": name, "address": address, "number": phonenum}
        cls.customers.append(customer_info)
        print(f"Customer {name} added successfully with id {customer_id}")

    @classmethod
    def view_customers(cls):
        if not cls.customers:
            print("No customers found.")
        else:
            print("Customers: ")
            for customer in cls.customers:
                print(customer)
    
    @classmethod
    def buy_process_order(cls, customer_name, product_name, quantity):
        product = None
        customer = None

        for buyer in cls.customers:
            if buyer['name'] == customer_name:
                customer = buyer
                break
        if customer is None:
            print("Customer not found")
            return

        for prod in Inventory.products:
            if prod.name == product_name:
                product = prod
                break
        if product is None:
            print("Product not found")
            return

        if product.quantity < quantity:
            print("Insufficient quantity")
            return
        
        total_price = quantity * product.price
        order = {"customer_id": customer['customer_id'], "product_name": product_name, "quantity": quantity, "total_price": total_price}
        cls.orders.append(order)
        product.quantity -= quantity

        print(f"Product {product_name} purchased successfully by {customer_name} with id {customer['customer_id']} and total price is {total_price}")

        total_amount = sum(o["total_price"] for o in cls.orders if o["customer_id"] == customer['customer_id'])
        print(f"Total amount to be paid by customer {customer_name}: ${total_amount}")

        print(f"Shipping orders for customer {customer_name}:")
        customer_orders = [o for o in cls.orders if o["customer_id"] == customer['customer_id']]
        for o in customer_orders:
            print(o)
        
    @classmethod
    def payment_shipment(cls, customer_name):
        customer = None
        for buyer in cls.customers:
            if buyer['name'] == customer_name:
                customer = buyer
                break
        if customer is None:
            print("Customer not found buddy...:)")
            return
        
        total_amount = sum(o['total_price'] for o in cls.orders if o['customer_id'] == customer['customer_id'])
        print(f"Total amount to be paid by customer {customer_name} : {total_amount}")
        print("Payment Done..:)")

        print(f'Shipping orders for customer {customer_name}')
        customer_orders = [o for o in cls.orders if o['customer_id'] == customer['customer_id']]
        for o in customer_orders:
            print(o)

        print(f"Order shipped to {customer['address']}")

# Products details
products = [
    ["Nike Air Zoom Pegasus 38", 120, 50, 4.8],
    ["Apple MacBook Pro (13-inch)", 1299, 100, 4.9],
    ["Sony WH-1000XM4 Wireless Headphones", 349.99, 30, 4.7],
    ["Samsung 55-inch QLED 4K Smart TV", 1099.99, 20, 4.6],
    ["Instant Pot Duo 7-in-1 Electric Pressure Cooker", 99.95, 80, 4.8],
    ["Adidas Ultraboost 21 Running Shoes", 180, 40, 4.7],
    ["Amazon Echo Dot (4th Gen)", 49.99, 120, 4.6],
    ["GoPro HERO9 Black", 449.99, 25, 4.8],
    ["KitchenAid Artisan Stand Mixer", 399.99, 60, 4.9],
    ["Samsung Galaxy S21 Ultra 5G", 1199.99, 35, 4.7],
    # Add more products here if needed
]

# Initialize products in Inventory
for item in products:
    Inventory.add_product(Product(*item))

# Switch case for user input
def main():
    while True:
        print("1. Add Customer")
        print("2. Process Order")
        print("3. Display Products Table")
        print("4. Display Cart Items")
        print("5. View Customers")
        print("6. Add cart")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Customer
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            phonenum = input("Enter customer phone number: ")
            Ecommerce.add_customer(name, address, phonenum)  

        elif choice == "2":
            # Process Order
            customer_name = input("Enter customer name: ")
            product_name = input("Enter product name: ")
            quantity = int(input("Enter quantity: "))
            Ecommerce.buy_process_order(customer_name, product_name, quantity)

        elif choice == "3":
            # Display Products Table
            Inventory.display_products_table()

        elif choice == "4":
            # Display Cart Items
            Inventory.display_cart_items()

        elif choice == "5":
            # View Customers
            Ecommerce.view_customers()

        elif choice == '6':
            product_name = input("Enter product name: ")
            for product in Inventory.products:
                if product.name == product_name:
                    Inventory.add_cart(product)
                    print("Product added successfully")
                    break  
            else:
                print("Product not found.")


        
        elif choice == "7":
            # Exit
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

main()
