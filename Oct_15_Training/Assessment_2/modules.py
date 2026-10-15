# section_modules.py

# 34. Normal import
import shipment_utils

# 35. Specific-function import
from shipment_utils import classify_shipment_weight

print("--- Module Function Calls ---")
# Using normal module dot-notation
calc_cost = shipment_utils.calculate_shipping_cost(12.5)
print(f"Normal Import -> Cost for 12.5 kg: Rs. {calc_cost}")

# Using specific imported function
cat = classify_shipment_weight(12.5)
print(f"Specific Import -> Weight category: {cat}")