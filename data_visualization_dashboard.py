import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/sales_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]
category_sales = df.groupby("Category")["Revenue"].sum()
plt.figure(figsize=(7, 7))
plt.pie(
    category_sales,
    labels=category_sales.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Category Wise Sales Distribution")
plt.savefig("category_sales.png")
plt.show()
