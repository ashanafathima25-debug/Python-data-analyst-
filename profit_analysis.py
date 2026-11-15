import pandas as pd
df = pd.read_csv("datasets/sales_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]
cost = 0.70
df["Profit"] = df["Revenue"] * (1 - cost)
print("PROFIT ANALYSIS")
print("----------------")
print(df[["Product", "Revenue", "Profit"]])
print("\nTotal Profit:")
print(df["Profit"].sum())
print("\nHighest Profit Product:")
print(df.groupby("Product")["Profit"].sum().idxmax())
