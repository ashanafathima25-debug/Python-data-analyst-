import pandas as pd
df = pd.read_csv("datasets/sales_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]
category_sales = df.groupby("Category")["Revenue"].sum()
print("CATEGORY SALES ANALYSIS")
print("-----------------------")
print(category_sales)
print("\nHighest Revenue Category:")
print(category_sales.idxmax())
print("\nLowest Revenue Category:")
print(category_sales.idxmin())
