# section_i.py
import pandas as pd

# 80. Read registrations.csv into DataFrame
df = pd.read_csv("registrations.csv")

# 81. Display basic information
print("--- First 5 Rows ---")
print(df.head())

print("\n--- Last 5 Rows ---")
print(df.tail())

print(f"\n--- Shape of DataFrame ---\n{df.shape}")

print("\n--- Column Names ---")
print(list(df.columns))

print("\n--- Data Types ---")
print(df.dtypes)

# 82. Display only selected columns
selected_cols = ["attendee_name", "city", "status", "amount"]
print("\n--- Selected Columns ---")
print(df[selected_cols].head())

# 83. Use query() to find Confirmed registrations
print("\n--- Confirmed Registrations (query) ---")
confirmed_df = df.query("status == 'Confirmed'")
print(confirmed_df[selected_cols])

# 84. Find registrations whose amount exceeds ₹6,000
print("\n--- Registrations with Amount > ₹6,000 ---")
high_amount_df = df[df["amount"] > 6000]
print(high_amount_df[["registration_id", "attendee_name", "amount"]])

# 85. Find Confirmed registrations from Hyderabad
print("\n--- Confirmed Registrations from Hyderabad ---")
hyd_confirmed = df[(df["city"] == "Hyderabad") & (df["status"] == "Confirmed")]
print(hyd_confirmed[["registration_id", "attendee_name", "city", "status"]])

# 86. Count registrations by status
print("\n--- Registration Count by Status ---")
print(df["status"].value_counts())

# 87. Find total amount by status
print("\n--- Total Amount by Status ---")
print(df.groupby("status")["amount"].sum())

# 88. Find average amount by city
print("\n--- Average Amount by City ---")
print(df.groupby("city")["amount"].mean())