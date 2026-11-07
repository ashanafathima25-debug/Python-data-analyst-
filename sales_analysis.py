import pandas as pd
data = {
    "Product": ["Rice", "Sugar", "Oil", "Rice", "Sugar"],
    "Sales": [5000, 3000, 4000, 6000, 3500]
}
df = pd.DataFrame(data)
print("SALES DATA ANALYSIS")
print("-------------------")
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)
product_sales = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:")
print(product_sales)
best_product = product_sales.idxmax()
print("\nBest Selling Product:", best_product)
