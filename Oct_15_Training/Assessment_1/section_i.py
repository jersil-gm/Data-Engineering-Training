# section_i.py
import numpy as np
import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")
orders["order_value"] = orders["quantity"] * orders["unit_price"]

# Join first to access segment and order_value together
df = pd.merge(customers, orders, on="customer_id", how="inner")

# 82. Create order_size using NumPy
conditions = [
    df["order_value"] >= 50000,
    df["order_value"] >= 15000,
]
choices = ["High", "Medium"]
df["order_size"] = np.select(conditions, choices, default="Low")

# 83. Create priority_customer (Corporate -> Priority, else Normal)
df["priority_customer"] = np.where(
    df["segment"] == "Corporate", "Priority", "Normal"
)

# 84. Save enriched dataset as enriched_orders.csv
df.to_csv("enriched_orders.csv", index=False)
print("Saved enriched_orders.csv:")
print(
    df[
        [
            "order_id",
            "customer_name",
            "segment",
            "order_value",
            "order_size",
            "priority_customer",
        ]
    ].head()
)