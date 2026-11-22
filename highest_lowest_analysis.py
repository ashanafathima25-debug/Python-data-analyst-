import pandas as pd
data = {
    "Student": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Marks": [85, 90, 78, 95, 82]
}
df = pd.DataFrame(data)
highest = df["Marks"].max()
lowest = df["Marks"].min()
print("HIGHEST AND LOWEST MARKS")
print("------------------------")
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("\nStudent with Highest Marks:")
print(df[df["Marks"] == highest])
print("\nStudent with Lowest Marks:")
print(df[df["Marks"] == lowest])
