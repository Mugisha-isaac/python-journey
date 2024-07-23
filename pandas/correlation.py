import pandas as pd

data = pd.read_csv("newCorr.csv")

print(data.corr())
