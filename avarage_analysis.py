import pandas as pd
data = {
    "Student": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Marks": [85, 90, 78, 95, 82]
}
df = pd.DataFrame(data)
average = df["Marks"].mean()
print("STUDENT MARKS ANALYSIS")
print("----------------------")
print(df)
print("\nAverage Marks:", average)
print("\nAverage Analysis Completed!")
