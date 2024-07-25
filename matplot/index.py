import matplotlib.pyplot as plt
import numpy as np

# xPoints = np.array([0, 6])
# yPoints = np.array([0, 250])

# plt.plot(xPoints, yPoints, "o")
# plt.show()

xPoints = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
yPoints = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {"family": "serif", "color": "blue", "size": 20}
font2 = {"family": "serif", "color": "darkred", "size": 15}

plt.plot(xPoints, yPoints)
plt.title("Sports Watch Data", fontdict=font1, loc="left")
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.show()
