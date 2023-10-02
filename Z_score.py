import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


lis1, lis2 = [], []

with open("/home/snehab/Work/ANM_1/6C04_4.sq", 'r') as infile:
    for line in infile:
        lis = line.split()
        lis1.append(float(lis[0]))
        lis2.append(float(lis[1]))

x = np.array(lis1)
'''
average = np.mean(x)
std = np.std(x)
y = x-average
y = y/std
'''
result = stats.zscore(x)

plt.plot(lis2, result, 'og')
plt.plot(lis2, y, ':r')
plt.show()

