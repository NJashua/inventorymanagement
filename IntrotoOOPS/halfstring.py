"""class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Buyer:
    def __init__(self, name, address, pincode):
        self.name = name
        self.address = address
        self.pincode = pincode
        

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.name] = product

    def check_inventory(self, product_name):
        if product_name in self.products:
            return self.products[product_name].quantity
        else:
            return 0

    def check_all_products(self):
        print("Inventory:")
        for product_name, product in self.products.items():
            print(f"Product: {product_name}, Price: {product.price}, Quantity: {product.quantity}")

class PincodeService:
    def __init__(self, serviceable_pincodes):
        self.serviceable_pincodes = serviceable_pincodes

    def check_serviceability(self, pincode):
        if pincode in self.serviceable_pincodes:
            print(f'The order is serviceable {pincode}')
        else:
            print("It's not possible")

    

class Order:
    def __init__(self, buyer, product_name, quantity):
        self.buyer = buyer
        self.product_name = product_name
        self.quantity = quantity

class ECommercePlatform:
    def __init__(self, inventory, pincode_service):
        self.inventory = inventory
        self.pincode_service = pincode_service
        self.orders = []

    def add_product(self, product):
        self.inventory.add_product(product)

    def add_buyer(self, buyer):
        self.buyer = buyer

    def create_order(self, buyer, product_name, quantity):
        if self.pincode_service.check_serviceability(buyer.pincode):
            if self.inventory.check_inventory(product_name) >= quantity:
                order = Order(buyer, product_name, quantity)
                self.orders.append(order)
                print("Order created successfully!")
            else:
                print("Sorry, product is out of stock.")
        else:
            print("Sorry, service is not available in this area.")

# Example usage:
inventory = Inventory()
pincode_service = PincodeService([507318, 507403, 582042])
ecommerce_platform = ECommercePlatform(inventory, pincode_service)


product_1 = Product("shirt", 2000, 10)

inventory.add_product(product_1)
inventory.check_all_products()

"""


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price 
        self.quantity = quantity

class Inventory: 
    def __init__(self) -> None:
        self.products = []

    def add_product(self, product):
        if product in self.products:
            print("Product already in inventory, please use update")
        else:
            self.products.append(product)
            print("Product added successfully")
    
    def check_all_products(self):
        print("Inventory: ")
        for product in self.products:
            print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")


inventory = Inventory()

product_1 = Product("Lenin pant", 2500, 5)
inventory.add_product(product_1)

inventory.check_all_products()  # Call the method on the instance of Inventory
