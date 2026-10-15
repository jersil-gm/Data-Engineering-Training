# section_b.py

sales = [65000, 4500, 36000, 12000, 18000, 72000, 9000]

# 10. Find total sales
total_sales = sum(sales)
print(f"Total Sales: {total_sales}")

# 11. Find highest and lowest sale
print(f"Highest Sale: {max(sales)}")
print(f"Lowest Sale: {min(sales)}")

# 12. Display sales greater than 20000
for s in sales:
    if s > 20000:
        print(f"Sale > 20000: {s}")

# 13. Sort sales from highest to lowest
sales.sort(reverse=True)
print(f"Sorted Sales: {sales}")

# 14. Create a set from cities and display unique cities
cities = ["Hyderabad", "Mumbai", "Delhi", "Hyderabad", "Pune", "Mumbai"]
unique_cities = set(cities)
print(f"Unique Cities: {unique_cities}")

# 15. Create a tuple and unpack it
product_tuple = (201, "Laptop", "Electronics", 65000)
prod_id, prod_name, category, price = product_tuple
print(f"ID: {prod_id}, Name: {prod_name}, Category: {category}, Price: {price}")

# 16. Create a dictionary representing a customer
customer = {
    "id": "C101",
    "name": "North Star Retail",
    "city": "Hyderabad",
    "orders": 4,
    "active": True,
}

# 17. Update customer's city
customer["city"] = "Bangalore"

# 18. Increase order count by 1
customer["orders"] += 1

# 19. Add an email field
customer["email"] = "northstar@gmail.com"

# 20. Loop through all keys and values
print("\nCustomer Details:")
for key, value in customer.items():
    print(f"{key}: {value}")