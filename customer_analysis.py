import pandas as pd
data = {
    "Customer": ["Arun", "Priya", "Kumar", "Arun", "Priya"],
    "Purchase": [2000, 3500, 1500, 2500, 3000]
}
df = pd.DataFrame(data)
print("CUSTOMER ANALYSIS")
print("-----------------")
total = df.groupby("Customer")["Purchase"].sum()
print("\nCustomer-wise Purchase:")
print(total)
print("\nTotal Customers:", df["Customer"].nunique())
print("\nHighest Spending Customer:")
print(total.idxmax())
print("\nTotal Purchase Amount:")
print(df["Purchase"].sum())
