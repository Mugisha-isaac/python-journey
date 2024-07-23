import pandas as pd

data = pd.read_json("data.json")
# print(data.head(10))
# print(data.tail())
# print(data.info())
data.dropna(inplace=True)
data.fillna(130, inplace=True)
print(data.to_string())
