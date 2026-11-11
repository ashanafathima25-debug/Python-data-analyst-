import pandas as pd
df = pd.read_csv("datasets/sales_data.csv")
df["Total"] = df["Quantity"] * df["Price"]
print("SALES REPORT")
print("------------")
print("\nComplete Sales Data:")
print(df)
print("\nTotal Revenue:")
print(df["Total"].sum())
print("\nBest Selling Product:")
print(df.groupby("Product")["Quantity"].sum().idxmax())
print("\nProduct-wise Revenue:")
print(df.groupby("Product")["Total"].sum())
