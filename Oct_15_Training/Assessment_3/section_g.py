# section_g.py
import json

# 61. Read JSON into Python
with open("staff.json", "r", encoding="utf-8") as f:
    staff_data = json.load(f)

# 62. Check datatype of returned object
print("--- Datatype of Returned Object ---")
print(f"Type: {type(staff_data)}")

# 63. Display all staff names
print("\n--- All Staff Names ---")
for s in staff_data:
    print(s["name"])

# 64. Display employees from Operations
print("\n--- Employees from Operations ---")
for s in staff_data:
    if s["department"] == "Operations":
        print(f"{s['name']} ({s['department']})")

# 65. Display employees whose salary exceeds ₹75,000
print("\n--- Employees with Salary > ₹75,000 ---")
for s in staff_data:
    if s["salary"] > 75000:
        print(f"{s['name']}: ₹{s['salary']}")

# 66. Find employees having Python in their skills
print("\n--- Employees Knowing Python ---")
for s in staff_data:
    if "Python" in s["skills"]:
        print(s["name"])

# 67. Display Name, Rating, Events Handled
print("\n--- Staff Performance Details ---")
for s in staff_data:
    print(
        f"Name: {s['name']} | Rating: {s['performance']['rating']} | "
        f"Events Handled: {s['performance']['events_handled']}"
    )

# 68. Find staff whose performance rating exceeds 4.5
print("\n--- Staff with Rating > 4.5 ---")
for s in staff_data:
    if s["performance"]["rating"] > 4.5:
        print(f"{s['name']} - Rating: {s['performance']['rating']}")

# 69. Extract all skills into one list
all_skills = []
for s in staff_data:
    all_skills.extend(s["skills"])
print("\n--- All Extracted Skills ---")
print(all_skills)

# 70. Find unique skills
print("\n--- Unique Skills ---")
print(set(all_skills))

# 71. Sort employees by salary descending
print("\n--- Employees Sorted by Salary (Descending) ---")
sorted_by_salary = sorted(staff_data, key=lambda s: s["salary"], reverse=True)
for s in sorted_by_salary:
    print(f"{s['name']}: ₹{s['salary']}")

# 72. Sort employees by performance rating descending
print("\n--- Employees Sorted by Rating (Descending) ---")
sorted_by_rating = sorted(
    staff_data, key=lambda s: s["performance"]["rating"], reverse=True
)
for s in sorted_by_rating:
    print(f"{s['name']}: Rating {s['performance']['rating']}")

# 73. Add "Pandas" to staff ID 503
print("\n--- Updating Skills for Staff ID 503 ---")
for s in staff_data:
    if s["staff_id"] == 503:
        if "Pandas" not in s["skills"]:
            s["skills"].append("Pandas")
        print(f"Updated skills for {s['name']}: {s['skills']}")

# 74. Save modified JSON as staff_updated.json
with open("staff_updated.json", "w", encoding="utf-8") as f:
    json.dump(staff_data, f, indent=2)
print("\nModified staff data saved to staff_updated.json")