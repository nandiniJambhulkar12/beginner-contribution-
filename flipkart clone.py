class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total


# Sample products
product1 = Product("Smartphone", 500, "A high-quality smartphone")
product2 = Product("Laptop", 1000, "A powerful laptop")
product3 = Product("Headphones", 100, "Noise-canceling headphones")

# Sample shopping cart
cart = ShoppingCart()

# Adding products to the cart
cart.add_item(product1)
cart.add_item(product2)
cart.add_item(product3)

# Removing a product from the cart
cart.remove_item(product2)

# Calculating the total price
total_price = cart.calculate_total()
print(f"Total price: ${total_price}")
