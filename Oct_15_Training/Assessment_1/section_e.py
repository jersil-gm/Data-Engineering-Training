# section_e.py
import csv
import json

# 40-41. Create activity.txt and write three messages
file = open("activity.txt", "w")
file.write("Processing started.\n")
file.write("Loading datasets.\n")
file.write("Validating records.\n")
file.close()

# 42. Append one additional message
file = open("activity.txt", "a")
file.write("Processing finished.\n")
file.close()

# 43. Read and display the complete file
print("--- activity.txt ---")
file = open("activity.txt", "r")
print(file.read())
file.close()

# 44-45. Read customers.csv using csv module into a list
customer_records = []
with open("customers.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        customer_records.append(row)

# 46. Display only active customers (active is index 4)
print("\nActive Customers:")
for row in customer_records:
    if row[4] == "True":
        print(row[1])

# 47. Display only Hyderabad customers (city is index 2)
print("\nHyderabad Customers:")
for row in customer_records:
    if row[2] == "Hyderabad":
        print(row[1])

# 48. Read products.json
with open("products.json", "r") as f:
    products = json.load(f)

# 49. Display all product names
print("\nProduct Names:")
for p in products:
    print(p["product_name"])

# 50. Display products costing above 10000
print("\nProducts > 10000:")
for p in products:
    if p["price"] > 10000:
        print(p["product_name"], p["price"])

# 51. Display supplier name and city
print("\nSuppliers:")
for p in products:
    print(f"{p['product_name']} -> {p['supplier']['name']}, {p['supplier']['city']}")

# 52. Extract all colors into one list
all_colors = []
for p in products:
    all_colors.extend(p["colors"])
print(f"\nAll Colors: {all_colors}")

# 53. Display unique colors
print(f"Unique Colors: {set(all_colors)}")

# 54. Increase stock of product ID 202
for p in products:
    if p["product_id"] == 202:
        p["stock"] += 5
        print(f"\nNew stock for 202: {p['stock']}")

# 55. Write modified data back to products_updated.json
with open("products_updated.json", "w") as f:
    json.dump(products, f, indent=2)