import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('zoo.csv')
X = dataset.iloc[:, 1:].values
#y = dataset.iloc[:, 2].values

#print(X)
data = [ [] * 17 for i in range(7)]
flag = [0] * 7
print(data)

for i in range(0,101):
    index = X[i][16] - 1
    if flag[index] == 0 :
        for j in range(0,17):
            data[index].append(X[i][j])
        flag[index] = 1
    else:
        for j in range(0,17):
            if(data[index][j]!=X[i][j]):
                data[index][j] = '?'


for i in range(0,7):
    print(i,":",end = " ")
    for j in range(0,16):
        print(data[i][j]," ",end=" ")
    print(" ")

        