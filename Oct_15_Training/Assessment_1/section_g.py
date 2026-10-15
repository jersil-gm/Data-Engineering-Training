# section_g.py
import pandas as pd

# 61. Read orders.csv into DataFrame
df = pd.read_csv("orders.csv")

# 62. Display first 5 rows
print("First 5 rows:")
print(df.head())

# 63. Display column names and datatypes
print("\nColumns and Types:")
print(df.dtypes)

# 64. Display shape of DataFrame
print(f"\nShape: {df.shape}")

# 65. Filter Delivered orders using query()
delivered = df.query("status == 'Delivered'")
print("\nDelivered Orders:")
print(delivered)

# 66. Filter orders where quantity > 2
qty_above_2 = df[df["quantity"] > 2]
print("\nQuantity > 2:")
print(qty_above_2)

# 67. Calculate order_value = quantity * unit_price
df["order_value"] = df["quantity"] * df["unit_price"]

# 68. Count orders by status
print("\nOrder count by status:")
print(df["status"].value_counts())

# 69. Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# 70. Create month column
df["month"] = df["order_date"].dt.month_name()

# 71. Find order count by month and status
print("\nCount by Month and Status:")
print(df.groupby(["month", "status"]).size())

# 72. Find total order value by category
print("\nTotal Value by Category:")
print(df.groupby("category")["order_value"].sum())

# 73. Find average order value by category
print("\nAverage Value by Category:")
print(df.groupby("category")["order_value"].mean())

# 74. Sort orders by order value descending
sorted_orders = df.sort_values(by="order_value", ascending=False)
print("\nSorted Orders (Descending):")
print(sorted_orders)