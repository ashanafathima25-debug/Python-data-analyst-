import pandas as pd
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6],
    "Marks": [45, 50, 60, 65, 75, 90]
}
df = pd.DataFrame(data)
print("Correlation Analysis")
print("--------------------")
correlation = df["Study_Hours"].corr(df["Marks"])
print("Study Hours and Marks Correlation:", correlation)
if correlation > 0:
    print("Positive Relationship")
elif correlation < 0:
    print("Negative Relationship")
else:
    print("No Linear Relationship")
