import pandas as pd

data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya", "Arun"],
    "Age": [21, 22, None, 20, 21],
    "Marks": [85, 90, 78, 95, 85]
}
df = pd.DataFrame(data)
print("DATA QUALITY CHECK")
print("------------------")
print("\nOriginal Dataset:")
print(df)
print("\nMissing Values:")
print(df.isnull().sum())
print("\nDuplicate Rows:")
print(df.duplicated().sum())
df = df.drop_duplicates()
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nCleaned Dataset:")
print(df)
print("\nData Quality Check Completed!")
