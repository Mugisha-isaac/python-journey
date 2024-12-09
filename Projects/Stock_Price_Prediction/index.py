import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn import metrics
import warnings


warnings.filterwarnings("ignore")

# Load the data
df = pd.read_csv("Tesla.csv")

# Plotting
# plt.figure(figsize=(15, 5))
# plt.plot(df["Close"])
# plt.title("Tesla Close price.", fontsize=15)
# plt.ylabel("Price in dollars.")

# print(df.isnull().sum())

features = ["Open", "High", "Low", "Close", "Volume"]
plt.subplots(figsize=(20, 10))

for i, col in enumerate(features):
    plt.subplot(3, 2, i + 1)
    sb.distplot(df[col])

plt.show()
