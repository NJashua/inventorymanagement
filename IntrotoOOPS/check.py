import time

class Product:
    def __init__(self, productId, name, inventoryCount):
        self.productId = productId
        self.name = name
        self.inventoryCount = inventoryCount

class Order:
    def __init__(self, orderId, productIds, quantityOrdered):
        self.orderId = orderId
        self.productIds = productIds
        self.quantityOrdered = quantityOrdered

class InventoryManagement:
    def __init__(self):
        self.products = {}
        self.blockedInventory = {}

    def createProduct(self, productId, name, count):
        product = Product(productId, name, count)
        self.products[productId] = product
        print(f"{productId} -> ({name}, {count})")

    def getInventory(self, productId):
        return self.products[productId].inventoryCount if productId in self.products else 0

    def createOrder(self, productIds, quantityOrdered, orderId):
        for i in range(len(productIds)):
            productId = productIds[i]
            requestedQuantity = quantityOrdered[i]
            if productId in self.products:
                product = self.products[productId]
                if product.inventoryCount >= requestedQuantity:
                    self.blockedInventory[productId] = self.blockedInventory.get(productId, 0) + requestedQuantity
                    product.inventoryCount -= requestedQuantity
                    print(f"{productId} -> {requestedQuantity} quantity blocked")
                else:
                    print(f"Insufficient inventory for product: {productId}")
            else:
                print(f"Product not found: {productId}")
        # Schedule release of blocked inventory after 5 minutes
        time.sleep(5 * 60)
        self.releaseBlockedInventory(orderId)

    def confirmOrder(self, orderId):
        if orderId in self.blockedInventory:
            for productId, quantity in self.blockedInventory.items():
                self.products[productId].inventoryCount += quantity
                print(f"{productId} -> {quantity} released back")
            print(f"Order confirmed: {orderId}")
            del self.blockedInventory[orderId]
        else:
            print(f"Order not found: {orderId}")

    def releaseBlockedInventory(self, orderId):
        if orderId in self.blockedInventory:
            for productId, quantity in self.blockedInventory.items():
                self.products[productId].inventoryCount += quantity
                print(f"{productId} -> {quantity} released back due to timeout")
            print(f"Order timeout: {orderId}")
            del self.blockedInventory[orderId]

if __name__ == "__main__":
    inventoryManagement = InventoryManagement()

    # Demo
    inventoryManagement.createProduct("1", "P1", 2)
    inventoryManagement.createProduct("2", "P2", 5)
    inventoryManagement.createProduct("3", "P3", 4)

    print("Inventory for Product 1:", inventoryManagement.getInventory("1"))
    print("Inventory for Product 2:", inventoryManagement.getInventory("2"))
    print("Inventory for Product 3:", inventoryManagement.getInventory("3"))

    inventoryManagement.createOrder(["1", "3"], [1, 2], "1")
    inventoryManagement.confirmOrder("1")

    print("Inventory for Product 1 after order confirmation:", inventoryManagement.getInventory("1"))
    print("Inventory for Product 2 after order confirmation:", inventoryManagement.getInventory("2"))
    print("Inventory for Product 3 after order confirmation:", inventoryManagement.getInventory("3"))
    
