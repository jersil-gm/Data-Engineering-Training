# section_h.py

# 76. Import the entire module
import event_utils

# 78. Import one function directly
from event_utils import calculate_booking_amount

# 79. Import the module using an alias
import event_utils as eu

print("--- Calling Functions Using Entire Module ---")
# 77. Call all three functions
amount = event_utils.calculate_booking_amount(2500, 4)
discount = event_utils.calculate_discount(amount)
status = event_utils.check_event_capacity(450, 500)
print(f"Booking Amount: ₹{amount}")
print(f"Discount: ₹{discount}")
print(f"Event Capacity Status: {status}")

print("\n--- Calling Directly Imported Function ---")
direct_amt = calculate_booking_amount(1500, 3)
print(f"Direct call result: ₹{direct_amt}")

print("\n--- Calling Function Using Alias ---")
alias_discount = eu.calculate_discount(15000)
print(f"Aliased call discount: ₹{alias_discount}")