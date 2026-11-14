import pandas as pd
df = pd.read_csv("datasets/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]
df["Month"] = df["Date"].dt.month_name()
monthly_sales = df.groupby("Month")["Revenue"].sum()
print("MONTHLY SALES ANALYSIS")
print("----------------------")
print(monthly_sales)
print("\nTotal Revenue:")
print(df["Revenue"].sum())
