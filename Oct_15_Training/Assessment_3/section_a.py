# section_a.py

# 1. Take attendee name, number of tickets and ticket price from the user
attendee_name = input("Enter attendee name: ").strip()
tickets = int(input("Enter number of tickets: "))
ticket_price = float(input("Enter ticket price: "))

# 2. Calculate total booking amount
total_amount = tickets * ticket_price

# 3. Apply discount (10% if >= 10000, else 5%)
if total_amount >= 10000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05

final_amount = total_amount - discount

# 4. Display all results using f-strings
print("\n--- Booking Summary ---")
print(f"Attendee Name : {attendee_name}")
print(f"Tickets Booked: {tickets}")
print(f"Total Amount  : ₹{total_amount:,.2f}")
print(f"Discount      : ₹{discount:,.2f}")
print(f"Final Payable : ₹{final_amount:,.2f}")

# 5. Ask for event capacity and registered participants
print("\n--- Capacity Check ---")
capacity = int(input("Enter total event capacity: "))
registered = int(input("Enter registered participants: "))

# 6. Display capacity status
if registered > capacity:
    print("Status: Invalid Data")
elif registered == capacity:
    print("Status: Full")
else:
    print("Status: Seats Available")

# 7. Print numbers 1–15 using a for loop
print("\n--- Numbers 1 to 15 ---")
for num in range(1, 16):
    print(num, end=" ")
print()

# 8. Display only numbers divisible by 3
print("\n--- Numbers Divisible by 3 (1-15) ---")
for num in range(1, 16):
    if num % 3 == 0:
        print(num, end=" ")
print()

# 9. Countdown from 10 to 1 using while loop
print("\n--- Countdown 10 to 1 ---")
count = 10
while count >= 1:
    print(count, end=" ")
    count -= 1
print()

# 10. Suitable examples using break and continue
print("\n--- Example using continue (skip 5) ---")
for num in range(1, 10):
    if num == 5:
        continue
    print(num, end=" ")
print()

print("\n--- Example using break (stop at 7) ---")
for num in range(1, 10):
    if num == 7:
        break
    print(num, end=" ")
print()