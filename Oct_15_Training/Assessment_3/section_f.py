# section_f.py
import csv

# 53-54. Read registrations.csv using csv module into a Python list
records = []
with open("registrations.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        records.append(row)

# Indices:
# 0: registration_id, 1: event_id, 2: attendee_name, 3: city
# 4: tickets, 5: registration_date, 6: status, 7: amount

# 55. Display only Confirmed registrations
print("--- Confirmed Registrations ---")
for row in records:
    if row[6] == "Confirmed":
        print(f"{row[0]} | {row[2]} | {row[6]}")

# 56. Display registrations from Hyderabad
print("\n--- Registrations from Hyderabad ---")
for row in records:
    if row[3] == "Hyderabad":
        print(f"{row[0]} | {row[2]} | {row[3]}")

# 57. Convert amount into a numeric datatype in place
for row in records:
    row[7] = float(row[7])

# 58. Find registrations where amount exceeds ₹7,000
print("\n--- Registrations with Amount > ₹7,000 ---")
for row in records:
    if row[7] > 7000:
        print(f"{row[2]} ({row[0]}): ₹{row[7]:,.2f}")

# 59. Calculate total registration amount
total_reg_amount = sum(row[7] for row in records)
print("\n--- Total Registration Amount ---")
print(f"Total: ₹{total_reg_amount:,.2f}")

# 60. Extract all cities and display unique cities
all_cities = [row[3] for row in records]
unique_cities = set(all_cities)
print("\n--- Unique Cities in Registrations ---")
print(unique_cities)