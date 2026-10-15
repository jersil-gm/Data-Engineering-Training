# section_a.py

# 1. Take product name, unit price, and quantity from the user
product_name = input("Enter product name : ").strip()
unit_price = float(input("Enter unit price : "))
quantity = int(input("Enter quantity: "))

# 2. Calculate total amount
total_amount = unit_price * quantity

# 3. Apply discount based on total amount
if total_amount >= 50000:
    discount = total_amount * 0.10
else:
    discount = total_amount * 0.05

final_amount = total_amount - discount

# 4. Display amounts using f-strings
print(f"\nProduct: {product_name}")
print(f"Original Amount : Rs. {total_amount:,.2f}")
print(f"Discount        : Rs. {discount:,.2f}")
print(f"Final Amount    : Rs. {final_amount:,.2f}\n")

# 5. Check stock levels
stock_quantity = int(input("Enter stock quantity: "))

if stock_quantity > 20:
    print("Stock Status: High Stock")
elif 1 <= stock_quantity <= 20:
    print("Stock Status: Low Stock")
else:
    print("Stock Status: Out of Stock")

# 6. For loop: numbers 1 through 10
print("\nNumbers 1 through 10:")
for num in range(1, 11):
    print(num, end=" ")
print()

# 7. While loop: reduce stock from 5 to 0
print("\nReducing stock from 5 to 0:")
current_stock = 5
while current_stock >= 0:
    print(f"Stock: {current_stock}")
    current_stock -= 1

# 8. Skip number 5 using continue
print("\nLoop with continue (skip 5):")
for num in range(1, 11):
    if num == 5:
        continue
    print(num, end=" ")
print()

# 9. Stop loop at 8 using break
print("\nLoop with break (stop at 8):")
for num in range(1, 11):
    if num == 8:
        break
    print(num, end=" ")
print()