from sklearn import svm
from sklearn import datasets
import pandas as pd

# iris = datasets.load_iris()

# x = iris.data[:, :2]
# y = iris.target


# model = svm.SVC(kernel="linear")
# model.fit(x, y)

# # predicting using svm model
# prediction = model.predict(x)

# # Evaluating prediction
# accuracy = model.score(x, y)

# print(f"Accuracy of svm model: {accuracy}")


# ============================================================================== #
# predicting svm model with california dataset


# california_housing = datasets.fetch_california_housing()

# m = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
# n = pd.DataFrame(california_housing.target, columns=["Target"])


# california_housing_model = svm.SVC(kernel="linear")
# california_housing_model.fit(m, n)

# california_housing_model_prediction = california_housing_model.predict(m)
# california_housing_model_accuracy = california_housing_model.score(m, n)

# print(f" california housing model accuracy: {california_housing_model_accuracy}")
