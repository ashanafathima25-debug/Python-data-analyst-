import pandas as pd
data = {
    "Student": ["Arun", "Priya", "Kumar", "Divya", "Ravi"],
    "Marks": [85, 90, 45, 95, 32]
}
df = pd.DataFrame(data)
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"
df["Grade"] = df["Marks"].apply(calculate_grade)
print("STUDENT GRADE ANALYSIS")
print("----------------------")
print(df)
print("\nGrade Analysis Completed!")
