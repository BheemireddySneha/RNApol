import sys
import os
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspc
import seaborn as sns

from scipy import stats

lis1, lis2 ,lis3, lis = [], [], [], []
liste, liste1, liste2 ,liste3, liste4 = [], [], [], [], []
yax = []
lista, listb = {},{}


x = '/home/snehab/Work/z_s_6c0'
y1 = '/home/snehab/Work/contact_apo'
y2 = '/home/snehab/Work/contact_DNA_onlyF'
y3 = '/home/snehab/Work/contact_RbpA'
y4 = '/home/snehab/Work/contact_carD'

y = [y1,y2,y3,y4]

with open(x) as file1:
    for line in file1:
        lis = line.split()
        lis1.append(lis[0])
        #print (lis[0])
        lis2.append(lis[1])
        lis3.append(float(lis[2]))

for k in range(0,len(y)):
    lista[(k)] = []
    listb[(k)] = []
    with open(y[k]) as file2:
        for line in file2:
            liste = line.split()
            lista[k].append(liste[0])
            listb[k].append(liste[2])
            #print (listb[k])

for l in range (0, len(y)):
    if l == 0:
        print ('ok')
        for i in range(0,len(lis1)):
            for j in range (0,len(lista[l])):
                if lis1[i] == lista[l][j]and lis2[i] == listb[l][j]:
                    #print ('ok')
                    liste1.append(lis3[i])
        #print (lista[0])
    elif l == 1:
        for i in range(0,len(lis1)):
            for j in range (0,len(lista[l])):
                if lis1[i] == lista[l][j]and lis2[i] == listb[l][j]:
                    #print ('ok')
                    liste2.append(lis3[i])
                    
                    
    elif l == 2:
        for i in range(0,len(lis1)):
            for j in range (0,len(lista[l])):
                if lis1[i] == lista[l][j]and lis2[i] == listb[l][j]:
                    #print ('ok')
                    liste3.append(lis3[i])
                    yax.append(j)
    else:
        for i in range(0,len(lis1)):
            for j in range (0,len(lista[l])):
                if lis1[i] == lista[l][j]and lis2[i] == listb[l][j]:
                    #print ('ok')
                    liste4.append(lis3[i])

data = [liste1, liste2,liste3,liste4]

#data['value'] = data['value'].astype(float)
#sns.factorplot(x='dataset', y='value', hue='Model', data=data , kind = 'box')
plt.scatter(yax, liste3)
#my_pal = {"versicolor": "g", "setosa": "b", "virginica":"m"}
#plt.scatter(data,, patch_artist=True)
'''colors = ['blue', 'green', 'purple', 'tan']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
plt.ylim(-2,4)
plt.xticks([1,2,3,4], ['apo','DNA','RbpA','CarD'])
'''
plt.show()
            
    
