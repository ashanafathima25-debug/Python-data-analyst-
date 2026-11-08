import pandas as pd
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [30, 32, 29, 35, 33],
    "Humidity": [65, 70, 60, 75, 68]
}
df = pd.DataFrame(data)
print("WEATHER DATA ANALYSIS")
print("---------------------")
print("\nWeather Data:")
print(df)
print("\nAverage Temperature:",
      df["Temperature"].mean())
print("Highest Temperature:",
      df["Temperature"].max())
print("Lowest Temperature:",
      df["Temperature"].min())
print("Average Humidity:",
      df["Humidity"].mean())
