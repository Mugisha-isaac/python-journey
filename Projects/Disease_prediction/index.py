# importing the necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import mode
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


# Reading training data excluding last column
data = pd.read_csv("Training.csv").dropna(axis=1)

# checking if dataset is balanced or not
disease_count = data["prognosis"].value_counts()
temp_def = pd.DataFrame({"Disease": disease_count.index, "Count": disease_count.values})

# plt.figure(figsize=(18, 8))
# sns.barplot(x="Disease", y="Count", data=temp_def)
# plt.xticks(rotation=90)
# plt.show()


# Encoding the categorical data
le = LabelEncoder()
data["prognosis"] = le.fit_transform(data["prognosis"])

# Splitting the data into training and testing data
x = data.iloc[:, :-1]
y = data.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=24
)

# print(f"Train: {x_train.shape}, {y_train.shape}")
# print(f"Test: {x_test.shape}, {y_test.shape}")

# Evaluating the test cores for models


# def cv_scoring(estimator, x, y):
#     return accuracy_score(y, estimator.predict(x))


# # initializing models

# models = {
#     "SVC": SVC(),
#     "Gaussian NB": GaussianNB(),
#     "Random Forest": RandomForestClassifier(),
# }


# # producing cross validation score for models

# for model_name in models:
#     model = models[model_name]
#     scores = cross_val_score(model, x, y, cv=10, n_jobs=-1, scoring=cv_scoring)

#     print("==" * 30)
#     print(model_name)
#     print(f"Scores: {scores}")
#     print(f"Mean score: {np.mean(scores)}")

# Training and testing SVM Classifier
svm_model = SVC()
svm_model.fit(x_train, y_train)
preds = svm_model.predict(x_test)

print(
    f"Accuracy on train data by SVM Classifier\
: {accuracy_score(y_train, svm_model.predict(x_train))*100}"
)

print(
    f"Accuracy on test data by SVM Classifier\
: {accuracy_score(y_test, preds)*100}"
)
cf_matrix = confusion_matrix(y_test, preds)
plt.figure(figsize=(12, 8))
sns.heatmap(cf_matrix, annot=True)
plt.title("Confusion Matrix for SVM Classifier on Test Data")
plt.show()

# Training and testing Naive Bayes Classifier
nb_model = GaussianNB()
nb_model.fit(x_train, y_train)
preds = nb_model.predict(x_test)
print(
    f"Accuracy on train data by Naive Bayes Classifier\
: {accuracy_score(y_train, nb_model.predict(x_train))*100}"
)

print(
    f"Accuracy on test data by Naive Bayes Classifier\
: {accuracy_score(y_test, preds)*100}"
)
cf_matrix = confusion_matrix(y_test, preds)
plt.figure(figsize=(12, 8))
sns.heatmap(cf_matrix, annot=True)
plt.title("Confusion Matrix for Naive Bayes Classifier on Test Data")
plt.show()

# Training and testing Random Forest Classifier
rf_model = RandomForestClassifier(random_state=18)
rf_model.fit(x_train, y_train)
preds = rf_model.predict(x_test)
print(
    f"Accuracy on train data by Random Forest Classifier\
: {accuracy_score(y_train, rf_model.predict(x_train))*100}"
)

print(
    f"Accuracy on test data by Random Forest Classifier\
: {accuracy_score(y_test, preds)*100}"
)

cf_matrix = confusion_matrix(y_test, preds)
plt.figure(figsize=(12, 8))
sns.heatmap(cf_matrix, annot=True)
plt.title("Confusion Matrix for Random Forest Classifier on Test Data")
plt.show()
