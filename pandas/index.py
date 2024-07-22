import pandas as pd

dataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}
frame = pd.DataFrame(dataset)

print(frame)
print(pd.__version__)
