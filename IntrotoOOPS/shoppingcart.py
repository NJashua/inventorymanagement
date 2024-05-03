class Cart:
    def __init__(self):
        self.items = {}
        self.price_details = {"book": 500, "laptop": 30000}

    def add_item(self, item_name, quantity):
        self.items[item_name] = quantity
        print("Item added successfully")

    def remove_item(self, item_name):
        del self.items[item_name]

    def update_quantity(self, item_name, quantity):
        self.items[item_name] = quantity

    def get_cart_items(self):
        cart_items = list(self.items.keys())
        print(cart_items)
        return cart_items

    def get_total_price(self):
        total_price = 0
        for item, quantity in self.items.items():
            total_price += quantity * self.price_details[item]
        return total_price


cart_obj = Cart()

print(cart_obj.get_cart_items())