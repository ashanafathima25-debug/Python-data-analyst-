import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("datasets/sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]
daily_sales = df.groupby("Date")["Revenue"].sum()
print("SALES TREND ANALYSIS")
print("--------------------")
print(daily_sales)
plt.figure(figsize=(9, 5))
plt.plot(daily_sales.index, daily_sales.values, marker="o")
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_trend.png")
plt.show()
