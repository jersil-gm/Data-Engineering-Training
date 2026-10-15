# section_enrichment.py
import numpy as np
import pandas as pd

# Load datasets and join
shipments = pd.read_csv("shipments.csv")
hubs = pd.read_csv("hubs.csv")
df = pd.merge(shipments, hubs, on="hub_id", how="inner")

# 51. Add cost_per_kg = cost / weight
df["cost_per_kg"] = df["cost"] / df["weight"]
print("--- Added Column: cost_per_kg ---")
print(df[["shipment_id", "cost", "weight", "cost_per_kg"]].head(4))

# 52. Use NumPy to classify cost >= 1200 -> Expensive, otherwise -> Normal
df["cost_tier"] = np.where(df["cost"] >= 1200, "Expensive", "Normal")
print("\n--- Added Column: cost_tier ---")
print(df[["shipment_id", "cost", "cost_tier"]].head(4))

# 53. Add a shipment performance category based on both status and cost
conditions = [
    (df["status"] == "Delivered") & (df["cost"] < 1000),
    (df["status"] == "Delivered") & (df["cost"] >= 1000),
    (df["status"] == "In Transit"),
]
choices = ["Delivered - Low Cost", "Delivered - High Cost", "Moving"]

df["performance_category"] = np.select(
    conditions, choices, default="Pending Action"
)
print("\n--- Added Column: performance_category ---")
print(
    df[
        [
            "shipment_id",
            "destination",
            "status",
            "cost",
            "performance_category",
        ]
    ].head(6)
)

# 54. Save the final enriched dataset as shipment_analysis.csv
df.to_csv("shipment_analysis.csv", index=False)
print("\n--- Final File Exported ---")
print("Saved final enriched dataset to shipment_analysis.csv")