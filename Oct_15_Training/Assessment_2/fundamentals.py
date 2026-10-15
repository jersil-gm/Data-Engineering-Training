# section_fundamentals.py

# 1. Accept shipment weight and cost from the user
weight = float(input("Enter shipment weight (kg): "))
cost = float(input("Enter shipment cost: "))

# 2. Calculate cost per kg
cost_per_kg = cost / weight
print("\n--- Cost Per Kg ---")
print(f"Cost per kg: Rs. {cost_per_kg:.2f}")

# 3. Classify weight
print("\n--- Weight Classification ---")
if weight > 20:
    print("Category: Heavy")
elif weight >= 10:
    print("Category: Medium")
else:
    print("Category: Light")

# 4. Use loops to display shipment numbers from 1–20
print("\n--- Shipment Numbers 1 to 20 ---")
for num in range(1, 21):
    print(num, end=" ")
print()

# 5. Display only even shipment numbers
print("\n--- Even Shipment Numbers ---")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")
print()

# 6. Use a while loop to simulate five processing attempts
print("\n--- Processing Attempts Simulation ---")
attempt = 1
while attempt <= 5:
    print(f"Processing attempt {attempt} of 5")
    attempt += 1