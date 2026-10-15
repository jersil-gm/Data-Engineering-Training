# section_collections.py

# 7. Create a list of shipment costs
costs = [850, 620, 1250, 480, 1600, 740, 590, 1100, 920, 1750, 520, 1050]

# 8. Calculate total, average, minimum and maximum
print("--- Shipment Cost Summary ---")
total_cost = sum(costs)
avg_cost = total_cost / len(costs)
print(f"Total Cost  : Rs. {total_cost}")
print(f"Average Cost: Rs. {avg_cost:.2f}")
print(f"Minimum Cost: Rs. {min(costs)}")
print(f"Maximum Cost: Rs. {max(costs)}")

# 9. Remove duplicate destination cities using a set
destinations = [
    "Hyderabad",
    "Mumbai",
    "Bangalore",
    "Delhi",
    "Pune",
    "Hyderabad",
    "Mumbai",
]
unique_destinations = set(destinations)
print("\n--- Unique Destination Cities ---")
print(unique_destinations)

# 10. Store one shipment using a dictionary
shipment = {
    "shipment_id": "S1001",
    "destination": "Hyderabad",
    "weight": 12.5,
    "cost": 850,
    "status": "Delivered",
}
print("\n--- Single Shipment Details ---")
for key, value in shipment.items():
    print(f"{key}: {value}")

# 11. Store multiple shipments using a list of dictionaries
shipments = [
    {
        "shipment_id": "S1001",
        "destination": "Hyderabad",
        "cost": 850,
        "status": "Delivered",
    },
    {
        "shipment_id": "S1002",
        "destination": "Mumbai",
        "cost": 620,
        "status": "In Transit",
    },
    {
        "shipment_id": "S1003",
        "destination": "Bangalore",
        "cost": 1250,
        "status": "Delivered",
    },
    {
        "shipment_id": "S1004",
        "destination": "Delhi",
        "cost": 480,
        "status": "Pending",
    },
]

# 12. Filter list records by status
print("\n--- Filtered Shipments (Delivered) ---")
for s in shipments:
    if s["status"] == "Delivered":
        print(s)