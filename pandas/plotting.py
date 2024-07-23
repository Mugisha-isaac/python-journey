import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("newCorr.csv")
data.plot(kind="scatter", x="Duration", y="Calories")
plt.show()
