# section_pandas.py
import pandas as pd

# 36. Read shipments.csv
df = pd.read_csv("shipments.csv")

# 37. Filter Delivered shipments
print("--- Delivered Shipments ---")
delivered_df = df[df["status"] == "Delivered"]
print(delivered_df)

# 38. Count records by status
print("\n--- Shipment Count by Status ---")
print(df["status"].value_counts())

# 39. Convert shipment date to datetime
df["shipment_date"] = pd.to_datetime(df["shipment_date"])

# 40. Count shipments by month and status
df["month"] = df["shipment_date"].dt.month_name()
print("\n--- Shipments by Month and Status ---")
print(df.groupby(["month", "status"]).size())

# 41. Calculate average cost by destination
print("\n--- Average Cost by Destination ---")
print(df.groupby("destination")["cost"].mean())

# 42. Calculate total weight by destination
print("\n--- Total Weight by Destination ---")
print(df.groupby("destination")["weight"].sum())

# 43. Read only selected columns using a dynamic usecols list
dynamic_cols = ["shipment_id", "destination", "cost"]
selected_df = pd.read_csv("shipments.csv", usecols=dynamic_cols)
print("\n--- Selected Columns Read (Dynamic usecols) ---")
print(selected_df.head(4))

# 44. Read hubs.csv
hubs_df = pd.read_csv("hubs.csv")

# 45. Inner join shipments and hubs using hub_id
merged_df = pd.merge(df, hubs_df, on="hub_id", how="inner")
print("\n--- Merged Shipments and Hubs ---")
print(
    merged_df[
        ["shipment_id", "hub_name", "destination", "cost", "status"]
    ].head(5)
)

# 46. Find total shipment cost handled by each hub
print("\n--- Total Cost Handled by Hub ---")
cost_by_hub = merged_df.groupby("hub_name")["cost"].sum()
print(cost_by_hub)

# 47. Find total number of shipments handled by each hub
print("\n--- Total Shipments Handled by Hub ---")
count_by_hub = merged_df.groupby("hub_name")["shipment_id"].count()
print(count_by_hub)

# 48. Sort hubs by total shipment cost
hub_summary = (
    merged_df.groupby(["hub_id", "hub_name"])
    .agg(
        total_cost=("cost", "sum"), total_shipments=("shipment_id", "count")
    )
    .reset_index()
)

hub_summary = hub_summary.sort_values(by="total_cost", ascending=False)
print("\n--- Hubs Sorted by Total Shipment Cost ---")
print(hub_summary)

# 49. Save results to CSV
hub_summary.to_csv("hub_summary.csv", index=False)

# 50. Save results to JSON
hub_summary.to_json("hub_summary.json", orient="records", indent=2)
print("\nResults successfully saved to hub_summary.csv and hub_summary.json")