import matplotlib.pyplot as plt

lis1, lis2, A,B = [], [], [],[]
with open('6eec_final.sq', 'r') as infile1:
    for line1 in infile1:
        lis = line1.split()
        lis1.append(float(lis[0]))
        lis2.append(float(lis[1]))
    for i in range (len(lis1)):
        if i < 5:
            A.append (lis1[i])
        elif i>5:
            B.append (lis1[i])
lis3, lis4, A1,B1 = [], [], [],[]
with open('6eec_final.sq', 'r') as infile2:
    for line2 in infile2:
        lis0 = line2.split()
        lis3.append(float(lis[0]))
        lis4.append(float(lis[1]))
    for j in range (len(lis3)):
        if j < 5:
            A1.append (lis3[i])
        elif j>5:
            B1.append (lis3[i])
            
plt.plot (A ,'.r')
plt.plot (B)
plt.plot (A1 ,'.g')
plt.plot (B1)
print (A)
plt.show()
