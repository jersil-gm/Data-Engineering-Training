# section_json.py
import json

# 24. Read employees.json
with open("employees.json", "r") as f:
    employees = json.load(f)

# 25. Display all employee names
print("--- All Employee Names ---")
for emp in employees:
    print(emp["name"])

# 26. Find employees earning above 75000
print("\n--- Employees Earning Above 75000 ---")
for emp in employees:
    if emp["salary"] > 75000:
        print(f"{emp['name']} - Rs. {emp['salary']}")

# 27. Display employees knowing Python
print("\n--- Employees Knowing Python ---")
for emp in employees:
    if "Python" in emp["skills"]:
        print(emp["name"])

# 28. Display employee name and performance rating
print("\n--- Employee Name and Performance Rating ---")
for emp in employees:
    print(f"{emp['name']}: {emp['performance']['rating']}")

# 29. Find employees whose rating exceeds 4.5
print("\n--- Employees with Rating Above 4.5 ---")
for emp in employees:
    if emp["performance"]["rating"] > 4.5:
        print(f"{emp['name']} - Rating: {emp['performance']['rating']}")

# 30. Sort employees by rating descending
print("\n--- Employees Sorted by Rating (Descending) ---")
sorted_employees = sorted(
    employees, key=lambda e: e["performance"]["rating"], reverse=True
)
for emp in sorted_employees:
    print(f"{emp['name']} - Rating: {emp['performance']['rating']}")

# 31. Add one skill to employee 303
print("\n--- Updating Employee 303 Skills ---")
for emp in employees:
    if emp["employee_id"] == 303:
        if "Docker" not in emp["skills"]:
            emp["skills"].append("Docker")
        print(f"Updated skills for {emp['name']}: {emp['skills']}")

# 32. Save the modified JSON
with open("employees.json", "w") as f:
    json.dump(employees, f, indent=2)
print("Changes successfully saved to employees.json")