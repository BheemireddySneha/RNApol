import os
import sys
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


A = []

file_num = input("No.of files:")

for i in range (int(file_num)):
    file_i = input ("file:")
    A.append (file_i)

lis1, lis2, lis3, B = [], [], [], []

for j in range (int(file_num)) :
    print ("The File(s) are: \n"+A[j]+'\n')
    infile = A[j]
    with open (A[j],'r') as infile :
        for line in infile:
            lis = line.split()
            lis1.append(float(lis[0]))
            lis2.append(lis[2])
            lis3.append(int(lis[3]))
        Chains = sorted(set(lis2))
        print (Chains)
        for o in Chains:
            lis0 = []
            lis4 = []
            for j in range(0, len(lis1)):
                    if lis2[j] == o:
                            lis0.append(lis1[j])
                            lis4.append(lis3[j])
            x = np.array(lis0)
            result = stats.zscore(x)
            plt.plot(lis4, result)
            plt.title('Chain: ' + str(o))
            plt.xlabel('Residue no.')
            plt.ylabel('Zscore')
            plt.grid(True)
            plt.show()
