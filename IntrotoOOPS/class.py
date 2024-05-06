import pandas as pd
import uuid

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

    def add_product(self):
        Inventory.products.append(self)
        print("Product added successfully")

    def apply_discount(self):
        discount_price = self.price - (self.price * (Inventory.discount / 100))
        return discount_price
    
    
    def add_cart(self):
        Inventory.cart_items.append(self)
        print(f"Item {self.name} added into cart successfully")
        return self
    
    def remove_cart_item(self, name):
        for item in Inventory.cart_items:
            if item.name == name:
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
                print(f'{item.name}: ${item.price}, discount price: {item.apply_discount()}')

    @classmethod
    def display_products_table(cls):
        df = pd.DataFrame([[p.name, p.price, p.quantity, p.rating, p.apply_discount()] for p in cls.products],
                          columns=['Name', 'Price', 'Quantity', 'Rating', 'Discounted Price'],
                          index=[i+1 for i in range(len(cls.products))])
        #df.to_excel(r"C:\Users\1038588\OneDrive - Blue Yonder\program files\python\PythonforPandas\sample.xlsx", index=False)
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

    def __init__(self, name, price, quantity, rating):
        super().__init__(name, price, quantity, rating)

    @classmethod
    def add_customer(cls, name, address, phonenum):
        customer_id = str(uuid.uuid4())[:5]
        email = name.replace(" ", "").lower() + "@gmail.com"
        customer_info = {"customer_id": customer_id, "name": name, "address": address, "number": phonenum}
        cls.customers.append(customer_info)
        print(f"Customer {name} added successfully with id {customer_id}")
        #return customer_id
    
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
            print("Customer not found budy...:)")
            return
        
        total_amount = sum(o['total_price'] for o in cls.orders if o['customer_id'] == customer['customer_id'])
        print(f"Total amount to be payed by customer {customer_name} : {total_amount}")
        print("Payment Done..:)")

        print(f'Shipping orders for customer {customer_name}')
        customer_orders = [o for o in cls.orders if o['customer_id'] == customer['customer_id']]
        for o in customer_orders:
            print(*o)

        print(f"Order shippid to {cls.customers.address}")

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
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            rating = float(input("Enter product rating: "))
            product = Inventory(name, price, quantity, rating)
            product.add_product()

        elif choice == "2":
            # Add Customer
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            phonenum = input("Enter customer phone number: ")
            Ecommerce.add_customer(name, address, phonenum)

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
            continue

        elif choice == "7":
    # Exit
            print("Exiting program...")
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
