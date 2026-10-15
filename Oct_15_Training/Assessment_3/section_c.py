# section_c.py


# 26. Function: calculate_booking(ticket_price, tickets)
def calculate_booking(ticket_price, tickets):
    return ticket_price * tickets


print("--- Calculate Booking ---")
print(f"Booking total for 3 tickets @ ₹2500: ₹{calculate_booking(2500, 3)}")


# 27. Function returning discount amount
def get_discount(amount):
    if amount >= 10000:
        return amount * 0.10
    return amount * 0.05


print("\n--- Discount on ₹12,000 ---")
print(f"Discount: ₹{get_discount(12000)}")


# 28. Function returning whether registration is active
def is_active_registration(status):
    return status.strip().lower() == "confirmed"


print("\n--- Check Active Status ---")
print(f"Is 'Confirmed' active? -> {is_active_registration('Confirmed')}")
print(f"Is 'Cancelled' active? -> {is_active_registration('Cancelled')}")


# 29. Function accepting a list of booking amounts and returning total
def get_total_bookings(amounts_list):
    return sum(amounts_list)


amounts = [5000, 3500, 7500, 6000]
print("\n--- Total of Booking Amounts List ---")
print(f"Total: ₹{get_total_bookings(amounts)}")

# 30. Lambda function that increases an amount by 10%
increase_by_ten_percent = lambda x: x * 1.10
print("\n--- Increase ₹5000 by 10% (Lambda) ---")
print(f"Increased Amount: ₹{increase_by_ten_percent(5000):.2f}")

# 31. filter() and lambda to select amounts greater than 6000
booking_amounts = [5000, 3500, 7500, 6000, 4000, 7000, 3000, 10000]
high_amounts = list(filter(lambda amt: amt > 6000, booking_amounts))
print("\n--- Amounts > 6000 (Filter) ---")
print(high_amounts)

# Shared list of dictionaries for Tasks 32-35
registrations = [
    {
        "id": "R1001",
        "name": "Aarav",
        "city": "Hyderabad",
        "status": "Confirmed",
        "amount": 5000,
    },
    {
        "id": "R1002",
        "name": "Simran",
        "city": "Mumbai",
        "status": "Confirmed",
        "amount": 3500,
    },
    {
        "id": "R1003",
        "name": "Faiz",
        "city": "Pune",
        "status": "Pending",
        "amount": 7500,
    },
    {
        "id": "R1005",
        "name": "Mohit",
        "city": "Delhi",
        "status": "Cancelled",
        "amount": 4000,
    },
    {
        "id": "R1006",
        "name": "Ananya",
        "city": "Hyderabad",
        "status": "Confirmed",
        "amount": 7000,
    },
]

# 32. filter() to return Confirmed registrations
confirmed_regs = list(filter(lambda r: r["status"] == "Confirmed", registrations))
print("\n--- Confirmed Registrations (Filter) ---")
for r in confirmed_regs:
    print(r)

# 33. map() to extract attendee cities
all_cities = list(map(lambda r: r["city"], registrations))
print("\n--- Extracted Cities (Map) ---")
print(all_cities)

# 34. map() and set() to obtain unique cities
unique_extracted_cities = set(map(lambda r: r["city"], registrations))
print("\n--- Unique Extracted Cities ---")
print(unique_extracted_cities)

# 35. Sort a list of registration dictionaries using key= based on amount
sorted_by_amount = sorted(registrations, key=lambda r: r["amount"])
print("\n--- Registrations Sorted by Amount (Ascending) ---")
for r in sorted_by_amount:
    print(f"{r['name']}: ₹{r['amount']}")