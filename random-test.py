import numpy as np

colors = ['blue', 'red', 'green']
weights = [0.1, 0.8, 0.1]


# check if this weighted function works
for i in range(20):
    print(np.random.choice(colors, size=1, replace=False, p=weights))