import pandas as pd
import uuid # for customer id generation

class Inventory:
    number_of_products = 0
    products = []
    discount = 5
    cart_items = []
    ordered_items = []

    def  __init__(self, name, price, quantity, rating):
        self.name = name
        self.price = price 
        self.quantity = quantity
        self.rating = rating 
        Inventory.number_of_products += 1
    # func for adding the products in inventory products 
    def add_prodcut(self):
        Inventory.products.append(self)
        print("Product added successfully..:)")
    
    def apply_discount(self):
        discount_price = self.price - (self.price  * (Inventory/100)) # in this inventory/100 returns decimal val, after multiplication with price it return discount amount, finally removing da in price
        return discount_price
    
    def add_cart(self):
        Inventory.cart_items.append(self)
        print(f"Item {self.name} added into cart succssfully..:)")

    def remove_cart_item(self, name):
        for item in Inventory.cart_items:
            if item.name == name:
                Inventory.cart_items.remove(item)
                print(f"Item {name} removed successfully from the cart..:(")

        print("No product there in the cart with the given name")

    @classmethod
    def display_cart_items(cls):
        if not cls.cart_items:
            print("Cart empty")
        else:
            print("Cart items: " )
            for item in cls.cart_items:
                df = pd.DataFrame()
