import pandas as pd

lis1 , lis2 = [], []


with open ("6C04_6.pdb",'r') as file:
    for lines in file:
        lis = lines.split()
        lis1.append(lis[0])
        lis2.append(int(lis[1]))

file_data = {
    'Type' : [lis1],
    'Num' : [lis2]
}

df = pd.DataFrame(file_data)
    
