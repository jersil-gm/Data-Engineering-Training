# section_f.py

# 57. Import the module
import retail_utils

# 58. Call all three functions
total = retail_utils.calculate_order_total(65000, 2)
discount = retail_utils.calculate_discount(total)
status = retail_utils.check_stock(12)
print(f"Total: {total}, Discount: {discount}, Stock: {status}")

# 59. Import one function directly and call it
from retail_utils import calculate_order_total

print("Direct call total:", calculate_order_total(3000, 4))

# 60. Import the module using an alias
import retail_utils as ru

print("Alias call discount:", ru.calculate_discount(20000))