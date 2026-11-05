import pandas as pd
data = {
    "Name": ["Arun", "Priya", "Kumar", "Divya"],
    "Age": [21, 22, 23, 20],
    "Marks": [85, 90, 78, 95]
}
df = pd.DataFrame(data)
print("DATASET SUMMARY")
print("----------------")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())
