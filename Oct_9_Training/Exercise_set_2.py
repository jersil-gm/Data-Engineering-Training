# Lists and Tuples
sales = [
    ("North", 12000),
    ("South", 18000),
    ("West", 9500),
    ("North", 22000),
    ("East", 15000),
    ("South", 11000)
]

# 1. Display all tuples
print("--- 1. All Tuples ---")
for item in sales:
    print(item)

# 2. Display only the region from every tuple
print("\n--- 2. Regions Only ---")
for region, _ in sales:
    print(region)

# 3. Display only the sales amount
print("\n--- 3. Sales Amounts Only ---")
for _, amount in sales:
    print(amount)

# 4. Find sales greater than 12000
print("\n--- 4. Sales > 12000 ---")
sales_gt_12000 = [item for item in sales if item[1] > 12000]
print(sales_gt_12000)

# 5. Calculate total sales
print("\n--- 5. Total Sales ---")
total_sales = sum(amount for _, amount in sales)
print(f"Total: ₹{total_sales}")

# 6. Find the highest and lowest sales amount
print("\n--- 6. High & Low ---\n")
sales_amounts = [amount for _, amount in sales]
highest_sale = max(sales_amounts)
lowest_sale = min(sales_amounts)
print(f"Highest: ₹{highest_sale}\nLowest: ₹{lowest_sale}")

# 7. Create a list containing only sales amounts
print("\n--- 7. Sales Amounts List ---")
amounts_list = [amount for _, amount in sales]
print(amounts_list)

# 8. Find unique regions using a set
print("\n--- 8. Unique Regions ---")
unique_regions = set(region for region, _ in sales)
print(unique_regions)

# 9. Sort the tuples based on sales amount
print("\n--- 9. Sorted by Sales Amount ---")
sorted_by_amount = sorted(sales, key=lambda item: item[1])
print(sorted_by_amount)

# 10. Sort the tuples based on region name
print("\n--- 10. Sorted by Region Name ---")
sorted_by_region = sorted(sales, key=lambda item: item[0])
print(sorted_by_region)