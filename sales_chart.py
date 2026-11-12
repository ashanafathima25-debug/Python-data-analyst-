import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/sales_data.csv")
df["Revenue"] = df["Quantity"] * df["Price"]
sales = df.groupby("Product")["Revenue"].sum()
plt.figure(figsize=(8, 5))
sales.plot(kind="bar")
plt.title("Product Wise Sales Analysis")
plt.xlabel("Products")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
