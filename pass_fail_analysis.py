import pandas as pd
data = {
    "Student": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Marks": [85, 90, 32, 95, 45]
}
df = pd.DataFrame(data)
df["Result"] = df["Marks"].apply(
    lambda marks: "Pass" if marks >= 40 else "Fail"
)
print("PASS AND FAIL ANALYSIS")
print("----------------------")
print(df)
print("\nTotal Passed:", (df["Result"] == "Pass").sum())
print("Total Failed:", (df["Result"] == "Fail").sum())
print("\nAnalysis Completed!")
