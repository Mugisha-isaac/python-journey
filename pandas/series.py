import pandas as pd

# a = [1, 7, 2]
# series = pd.Series(a, index=["x", "y", "z"])

# calories = {"day1": 420, "day2": 380, "day3": 390}
# calories_series = pd.Series(calories, index=["day1", "day2"])
# print(calories_series)

# reading data from a csv file
pd.options.display.max_rows = 10
data = pd.read_csv("data.csv")
print(data.to_string())
