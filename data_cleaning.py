import pandas as pd

data = {
    'Name': ['Arun', 'Priya', 'Kumar', 'Divya'],
    'Age': [21, 22, 23, 20],
    'Marks': [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nAverage Marks:")
print(df['Marks'].mean())
