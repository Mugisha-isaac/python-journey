import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

x = np.random.normal(5.0, 1.0, 1000)
y = np.random.normal(10.0, 2.0, 1000)

slope, intercept, r, p, std_err = stats.linregress(x, y)


# def myFunc(x):
#     return slope * x + intercept


# myModel = list(map(myFunc, x))
# plt.scatter(x, y)
# plt.plot(x, myModel)
# plt.show()

print(r)
