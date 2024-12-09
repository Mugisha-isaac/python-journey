from sklearn.datasets import fetch_california_housing, load_iris
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn import svm
import pandas as pd
import numpy as np

# data = fetch_california_housing()

# x = pd.DataFrame(data.data, columns=data.feature_names)
# y = pd.DataFrame(data.target, columns=["Target"])

# k = 5
# kf = KFold(n_splits=k, shuffle=True, random_state=42)

# model = LinearRegression()

# scores = cross_val_score(model, x, y, scoring="r2", cv=kf)

# average_r2 = np.mean(scores)

# print(f"R² Score for each fold: {[round(score, 4) for score in scores]}")
# print(f"Average R² across {k} folds: {average_r2:.2f}")


# ======================================================================== #
# ================= model prediction using svm =========================== #

# iris = load_iris()

# m = iris.data[:, :2]
# n = iris.target

# model = svm.SVC(kernel="linear")
# model.fit(m, n)

# prediction = model.predict(m)
# accuracy = model.score(m, n)

# print(f"svc model accuracy: {accuracy}")
