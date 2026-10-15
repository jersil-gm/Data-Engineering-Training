# section_c.py


# 21. Create calculate_total
def calculate_total(price, quantity):
    return price * quantity


# 22. Create calculate_discount
def calculate_discount(amount):
    if amount >= 50000:
        return amount * 0.10
    return amount * 0.05


# 23. Function accepting list of sales and returning total
def get_total_sales(sales_list):
    return sum(sales_list)


# 24. Function returning Available or Out of Stock
def check_stock_status(prod):
    if prod.get("stock", 0) > 0:
        return "Available"
    return "Out of Stock"


# 25. Lambda function to calculate square
square = lambda x: x * x
print(f"Square of 6: {square(6)}")

# 26. filter() with lambda for sales > 20000
sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]
high_sales = list(filter(lambda s: s > 20000, sales))
print(f"Filtered Sales: {high_sales}")

# 27. map() to extract customer cities
customers = [
    {"name": "Blue Mart", "city": "Mumbai"},
    {"name": "Prime Stores", "city": "Hyderabad"},
    {"name": "Central Bazaar", "city": "Mumbai"},
]
extracted_cities = list(map(lambda c: c["city"], customers))
print(f"Extracted Cities: {extracted_cities}")

# 28. set() to get unique cities
print(f"Unique Cities: {set(extracted_cities)}")

# 29. Sort product dictionaries by price using key=
products = [
    {"name": "Laptop", "price": 65000},
    {"name": "Mouse", "price": 1500},
    {"name": "Monitor", "price": 18000},
]
sorted_products = sorted(products, key=lambda p: p["price"])
print(f"Sorted Products: {sorted_products}")