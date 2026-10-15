# section_functions.py


# 13. Create a function calculating shipping cost
def calculate_shipping_cost(weight, rate=70):
    return weight * rate


print("--- Shipping Cost Calculation ---")
print(f"Cost for 10 kg: Rs. {calculate_shipping_cost(10)}")


# 14. Create a function returning shipment category based on weight
def get_weight_category(weight):
    if weight > 20:
        return "Heavy"
    elif weight >= 10:
        return "Medium"
    return "Light"


print("\n--- Shipment Category by Weight ---")
print(f"18.5 kg is categorized as: {get_weight_category(18.5)}")

# Shared records for Tasks 15-17
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

# 15. Use lambda/filter to select Delivered shipments
print("\n--- Delivered Shipments (filter + lambda) ---")
delivered_shipments = list(
    filter(lambda s: s["status"] == "Delivered", shipments)
)
print(delivered_shipments)

# 16. Use map to obtain all destinations
print("\n--- All Destinations (map) ---")
all_destinations = list(map(lambda s: s["destination"], shipments))
print(all_destinations)

# 17. Sort shipment dictionaries by cost
print("\n--- Shipments Sorted by Cost (Ascending) ---")
sorted_shipments = sorted(shipments, key=lambda s: s["cost"])
print(sorted_shipments)