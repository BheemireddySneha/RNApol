#---------Programme for calculating Z_Score & Graph of Z-Score-------#

import sys
import os
import math

open(sys.argv[1], 'r'):
#f=open(".sq","r")

lines=f.readlines()
result=[]
for x in lines:
    result.append(x.split(' ')[0])
sub=[float(i) for i in result]
sub1=sub[0:225]
sub2=sub[226:237]
sub3=sub[256:289]
sub4=sub[358:987]
sub5

s=len(item)
mean=sum(item)/s
st=sum([(item[i]-mean)**2 for i  in range(s)])

std=math.sqrt(st/s)
z=[((item[i]-mean)/std) for i in range(s)]
file1=open("zscore.txt","w")
#zs=[str(i) for i in z]
for i in range(s):
    print(z[i],file=file1)
f.close()
file1.close()
