import numpy as np
import scipy.stats as stats

speed = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

meanSpeed = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)
sd = np.std(speed)
vr = np.var(speed)

print(f"Mean: {meanSpeed}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Standard Deviation: {sd}")
print(f"Variance: {vr}")
