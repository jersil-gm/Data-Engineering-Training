# section_d.py


# 30-32. Product class
class Product:

    def __init__(self, product_id, product_name, price, stock):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def display_product(self):
        print(f"Product: {self.product_name}, Price: {self.price}")

    def calculate_value(self):
        return self.price * self.stock


# 33. Create two product objects
prod1 = Product(201, "Laptop", 65000, 12)
prod2 = Product(202, "Monitor", 18000, 8)


# 34-37. DiscountedProduct class
class DiscountedProduct(Product):

    def __init__(self, product_id, product_name, price, stock, discount_percent):
        super().__init__(product_id, product_name, price, stock)
        self.discount_percent = discount_percent

    def display_product(self):
        print(
            f"Product: {self.product_name}, Price: {self.price}, Discount: {self.discount_percent}%"
        )


# 38. PremiumProduct class
class PremiumProduct(Product):

    def display_product(self):
        print(f"*** Premium Product: {self.product_name} | Price: {self.price} ***")


# 39. Demonstrate polymorphism
p = Product(204, "Keyboard", 3000, 30)
dp = DiscountedProduct(203, "Office Chair", 9000, 15, 10)
prem = PremiumProduct(205, "Workstation", 120000, 5)

items = [p, dp, prem]
for item in items:
    item.display_product()