import sys
import os
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

lis1, lis2, lis3 = [], [], []
d1 = {}

with open('6eec_final.sq', 'r') as infile:
	for line3 in infile:
		lis = line3.split()
		d1[float(lis[0])] = lis[2]
		lis1.append(float(lis[0]))
		lis2.append(lis[2])
		lis3.append(int(lis[3]))

chains = set(lis2)
print (chains)

for o in chains:
	lis0 = []
	lis4 = []
	for j in range(0, len(lis1)):
		if lis2[j] == o:
			lis0.append(lis1[j])
			lis4.append(lis3[j])
	#print lis4	
	x = np.array(lis0)
	result = stats.zscore(x)
	plt.plot(lis4, result)
	plt.title('Chain: ' + str(o))
	plt.xlabel('Residue no.')
	plt.ylabel('Zscore')
	plt.grid(True)
	plt.show()
	
'''
x = np.array(lis1)
result = stats.zscore(x)

average = np.mean(x)
std = np.std(x)
y = x-average
y = y/std


plt.plot(lis2, result, 'og')
#plt.plot(lis2, y, ':r')
plt.show()
'''
