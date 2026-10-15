# section_h.py
import pandas as pd

customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

# Add order_value needed for aggregation
orders["order_value"] = orders["quantity"] * orders["unit_price"]

# 75. Perform inner join on customer_id
merged = pd.merge(customers, orders, on="customer_id", how="inner")

# 76. Display specific columns
cols = [
    "order_id",
    "customer_name",
    "city",
    "product",
    "status",
    "order_value",
]
print("Joined Records:")
print(merged[cols])

# 77. Display only Delivered orders from Hyderabad
hyd_delivered = merged[
    (merged["city"] == "Hyderabad") & (merged["status"] == "Delivered")
]
print("\nHyderabad Delivered Orders:")
print(hyd_delivered[cols])

# 78. Calculate total orders, total sales, and avg order value by city
city_summary = (
    merged.groupby("city")
    .agg(
        total_orders=("order_id", "count"),
        total_sales=("order_value", "sum"),
        avg_order_value=("order_value", "mean"),
    )
    .reset_index()
)

# 79. Sort results by total sales descending
city_summary = city_summary.sort_values(by="total_sales", ascending=False)
print("\nCity Summary:")
print(city_summary)

# 80. Write result to city_sales_summary.csv
city_summary.to_csv("city_sales_summary.csv", index=False)

# 81. Write result to city_sales_summary.json (record-oriented)
city_summary.to_json("city_sales_summary.json", orient="records", indent=2)