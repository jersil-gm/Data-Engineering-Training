# section_b.py

booking_amounts = [5000, 3500, 7500, 6000, 4000, 7000, 3000, 10000]

# 11. Find total booking amount
print("--- Total Booking Amount ---")
total_amount = sum(booking_amounts)
print(f"Total: ₹{total_amount}")

# 12. Find average booking amount
print("\n--- Average Booking Amount ---")
avg_amount = total_amount / len(booking_amounts)
print(f"Average: ₹{avg_amount:.2f}")

# 13. Find highest and lowest amounts
print("\n--- Highest & Lowest Booking Amounts ---")
print(f"Highest: ₹{max(booking_amounts)}")
print(f"Lowest : ₹{min(booking_amounts)}")

# 14. Display values greater than 5000
print("\n--- Amounts Greater Than 5000 ---")
for amt in booking_amounts:
    if amt > 5000:
        print(f"₹{amt}")

# 15. Sort amounts descending
print("\n--- Booking Amounts (Descending) ---")
sorted_amounts = sorted(booking_amounts, reverse=True)
print(sorted_amounts)

# 16. Find unique cities using a set
cities = ["Hyderabad", "Mumbai", "Pune", "Hyderabad", "Delhi", "Mumbai"]
unique_cities = set(cities)
print("\n--- Unique Cities ---")
print(unique_cities)

# 17. Add another city to the set
unique_cities.add("Bangalore")
print("\n--- Unique Cities after Adding Bangalore ---")
print(unique_cities)

# 18. Find number of unique cities
print("\n--- Count of Unique Cities ---")
print(f"Total Unique Cities: {len(unique_cities)}")

# 19. Create tuple
event_tuple = ("E101", "AI Innovation Summit", "Hyderabad", 500)

# 20. Unpack tuple into separate variables
event_id, event_name, venue, capacity = event_tuple
print("\n--- Unpacked Event Tuple ---")
print(
    f"ID: {event_id}, Name: {event_name}, Venue: {venue}, Capacity: {capacity}"
)

# 21. Create a dictionary representing one registration
registration = {
    "registration_id": "R1001",
    "attendee_name": "Aarav Shah",
    "city": "Hyderabad",
    "tickets": 2,
    "status": "Pending",
    "amount": 5000,
}

# 22. Change its status
registration["status"] = "Confirmed"

# 23. Increase ticket count
registration["tickets"] += 1

# 24. Add an email field
registration["email"] = "aarav.shah@example.com"

# 25. Loop through all dictionary items
print("\n--- Registration Dictionary Items ---")
for key, value in registration.items():
    print(f"{key}: {value}")