import pandas as pd
df=pd.read_csv("orders.csv")
print(df)
print(df.tail())
print(df.head())
print(df.columns)
print(df.shape)
print(df.dtypes)
df.info()
print(df["product"])
print(df[["order_id","product","amount"]])

#Filter
delivered = df.query("status == 'Delivered'")
print(delivered)

result=df.query("amount>20000")
print(result)

# print(df["status"].value_counts())
result=(
    df.groupby("status").size()
)
print(result)

#string to date
df["order_date"]=pd.to_datetime(df["order_date"])
df["month"]=df["order_date"].dt.month
print(df)
