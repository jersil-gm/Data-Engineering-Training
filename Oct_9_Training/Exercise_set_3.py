#Exercise Set 3 - JSON Processing
import json

json_content = """[
  {
    "project_id": 101,
    "project_name": "Data Migration",
    "department": "IT",
    "budget": 450000,
    "technologies": ["Python", "SQL", "Azure"],
    "team": [
      {"name": "Vikram", "role": "Engineer", "experience": 4},
      {"name": "Meera", "role": "Analyst", "experience": 3}
    ]
  },
  {
    "project_id": 102,
    "project_name": "Customer Analytics",
    "department": "Analytics",
    "budget": 300000,
    "technologies": ["Python", "Pandas", "Power BI"],
    "team": [
      {"name": "Karan", "role": "Data Analyst", "experience": 5},
      {"name": "Zoya", "role": "Developer", "experience": 2}
    ]
  },
  {
    "project_id": 103,
    "project_name": "Cloud Modernization",
    "department": "Cloud",
    "budget": 600000,
    "technologies": ["Azure", "Docker", "Python"],
    "team": [
      {"name": "Naveen", "role": "Cloud Engineer", "experience": 6},
      {"name": "Isha", "role": "Engineer", "experience": 4}
    ]
  }
]"""

with open("projects.json", "w") as file:
    file.write(json_content)

# 1. Read the JSON file into Python
with open("projects.json", "r") as f:
    projects = json.load(f)

# 2. Check the datatype of the returned object
print("--- 2. Datatype of Returned Object ---")
print(f"Datatype: {type(projects)}")

# 3. Display all project names
print("\n--- 3. Project Names ---")
for p in projects:
    print(p["project_name"])

# 4. Display projects having a budget above ₹4,00,000
print("\n--- 4. Projects with Budget > 400,000 ---")
for p in projects:
    if p["budget"] > 400000:
        print(f"{p['project_name']} (Budget: ₹{p['budget']})")

# 5. Display projects that use Python
print("\n--- 5. Projects using Python ---")
for p in projects:
    if "Python" in p["technologies"]:
        print(p["project_name"])

# 6. Calculate total budget of all projects
print("\n--- 6. Total Budget ---\n")
total_budget = sum(p["budget"] for p in projects)
print(f"Total: ₹{total_budget}")

# 7. Extract all technologies into one Python list
print("\n--- 7. All Technologies List ---")
all_technologies = [tech for p in projects for tech in p["technologies"]]
print(all_technologies)

# 8. Find the unique technologies
print("\n--- 8. Unique Technologies ---")
unique_technologies = set(all_technologies)
print(unique_technologies)

# 9. Display every team member's: name, role, experience
print("\n--- 9. All Team Members ---")
for p in projects:
    for m in p["team"]:
        print(f"Name: {m['name']}, Role: {m['role']}, Experience: {m['experience']} yrs")

# 10. Display team members having more than 3 years of experience
print("\n--- 10. Members with Experience > 3 Years ---")
for p in projects:
    for m in p["team"]:
        if m["experience"] > 3:
            print(f"{m['name']} ({m['role']}) - {m['experience']} years [Project: {p['project_name']}]")

# 11. Find the total number of team members across all projects
print("\n--- 11. Total Team Member Count ---\n")
total_members = sum(len(p["team"]) for p in projects)
print(f"Total: {total_members}")

# 12. Sort projects by budget from highest to lowest
print("\n--- 12. Projects Sorted by Budget ---")
sorted_by_budget = sorted(projects, key=lambda p: p["budget"], reverse=True)
for p in sorted_by_budget:
    print(f"{p['project_name']}: {p['budget']}")

# 13. Sort projects alphabetically by project name
print("\n--- 13. Projects Sorted by Name  ---")
sorted_by_pname = sorted(projects, key=lambda p: p["project_name"])
for p in sorted_by_pname:
    print(p["project_name"])

# 14. Sort each project's team members based on experience
print("\n--- 14. Team Members Sorted by Experience  ---")
for p in projects:
    p["team"].sort(key=lambda m: m["experience"], reverse=True)
    print(f"\nProject: {p['project_name']}")
    for m in p["team"]:
        print(f"  {m['name']} - {m['experience']} years ({m['role']})")