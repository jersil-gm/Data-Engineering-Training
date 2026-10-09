# Exercise Set 1: CSV, Lists, Lambda, Filter, Map, Set, Sorting

import csv

csv_data = """shipment_id,customer,city,weight,status,cost
S101,Alpha Stores,Hyderabad,12.5,Delivered,850
S102,Metro Mart,Mumbai,8.2,In Transit,620
S103,Fresh Foods,Hyderabad,15.0,Delivered,1100
S104,Quick Shop,Pune,5.5,Pending,450
S105,Urban Retail,Mumbai,20.0,Delivered,1450
S106,Daily Needs,Delhi,9.8,In Transit,700
S107,Smart Bazaar,Hyderabad,7.5,Pending,550
S108,Green Market,Delhi,18.2,Delivered,1300"""

with open("shipments.csv", "w") as f:
    f.write(csv_data)

# 1. Read shipments.csv using Python's csv module
print("--- 1. Reading shipments.csv ---")
with open("shipments.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2. Store all records inside a Python list (using DictReader so rows are dictionaries)
shipments = []
with open("shipments.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        shipments.append(dict(row))

# 3. Display the complete list
print("\n--- 3. Complete List ---")
for s in shipments:
    print(s)

# 4. Display only: shipment ID, customer, status
print("\n--- 4. ID, Customer, Status ---")
for s in shipments:
    print(f"ID: {s['shipment_id']}, Customer: {s['customer']}, Status: {s['status']}")

# 5. Convert weight and cost from strings to numeric values
for s in shipments:
    s["weight"] = float(s["weight"])
    s["cost"] = float(s["cost"])

# 6. Calculate total shipping cost
print("\n--- 6. Total Shipping Cost ---\n")
total_cost = sum(s["cost"] for s in shipments)
print(f"Total: {total_cost:.2f}")

# 7. Find shipments whose cost is greater than 700
print("\n--- 7. Cost > 700 ---")
cost_above_700 = [s for s in shipments if s["cost"] > 700]
for s in cost_above_700:
    print(f"{s['shipment_id']} - {s['cost']}")

# 8. Use filter() and lambda to display only Delivered shipments
print("\n--- 8. Delivered Shipments ---")
delivered_shipments = list(filter(lambda s: s["status"] == "Delivered", shipments))
for s in delivered_shipments:
    print(f"{s['shipment_id']}: {s['customer']} ({s['status']})")

# 9. Use filter() and lambda to find shipments weighing more than 10
print("\n--- 9. Weight > 10 kg ---")
heavy_shipments = list(filter(lambda s: s["weight"] > 10, shipments))
for s in heavy_shipments:
    print(f"{s['shipment_id']}: {s['weight']} kg")

# 10. Use map() to extract all city names
print("\n--- 10. All Cities ---")
all_cities = list(map(lambda s: s["city"], shipments))
print(all_cities)

# 11. Use map() + set() to get unique cities
print("\n--- 11. Unique Cities ---")
unique_cities = set(map(lambda s: s["city"], shipments))
print(unique_cities)

# 12. Sort by cost from lowest to highest using key
print("\n--- 12. Sorted by Cost (Ascending) ---")
sorted_by_cost = sorted(shipments, key=lambda s: s["cost"])
for s in sorted_by_cost:
    print(f"{s['shipment_id']} - {s['cost']}")

# 13. Sort by weight from highest to lowest
print("\n--- 13. Sorted by Weight (Descending) ---")
sorted_by_weight_desc = sorted(shipments, key=lambda s: s["weight"], reverse=True)
for s in sorted_by_weight_desc:
    print(f"{s['shipment_id']} - {s['weight']} kg")

# 14. Sort alphabetically by customer name
print("\n--- 14. Sorted by Customer Name ---")
sorted_by_customer = sorted(shipments, key=lambda s: s["customer"])
for s in sorted_by_customer:
    print(f"{s['customer']} ({s['shipment_id']})")

# 15. Lambda function for cost per kg = cost / weight
print("\n--- 15. Cost Per KG ---")
calc_cost_per_kg = lambda s: s["cost"] / s["weight"]
for s in shipments:
    unit_cost = calc_cost_per_kg(s)
    print(f"{s['shipment_id']} ({s['customer']}): {unit_cost:.2f}/kg")