import pandas as pd
df = pd.read_csv("datasets/sales_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]
top_products = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)
print("TOP SELLING PRODUCTS")
print("--------------------")
print(top_products.head(5))
print("\nHighest Revenue Product:")
revenue = df.groupby("Product")["Revenue"].sum()
print(revenue.idxmax())
