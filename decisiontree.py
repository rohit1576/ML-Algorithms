import pandas as pd
import math
# Importing the dataset
dataset = pd.read_csv('tennis.csv')
X = dataset.iloc[:, 1:].values

# print(X)
attribute = [0,1,2,3]

def findEntropy(arr):
    yes = 0
    no = 0
    idx = len(arr[0]) - 1
    for i in range(0, len(arr)):
        if arr[i][idx] == 'Yes':
            yes = yes + 1
        else:
            no = no + 1

    x = yes/(yes+no)
    y = no/(yes+no)
    entropy = -1 * (x*math.log2(x) + y*math.log2(y))
    return entropy


# print(findEntropy())
def findGain(arr, index):

    entropy = findEntropy(arr)
    # print(entropy)
    mydict = {}
    for i in range(0, len(arr)):
        key = arr[i][index]
        if key in mydict:
            mydict[key] = mydict[key] + 1
        else:
            mydict[key] = 1
    # print(mydict)
    gain = entropy
    for key in mydict:
        yes = 0
        no = 0
        idx = len(arr[0]) - 1
        for j in range(0, len(arr)):
            if arr[j][index] == key:
                if arr[j][idx] == 'Yes':
                    yes = yes + 1
                else:
                    no = no + 1
        x = yes/(yes+no)
        y = no/(yes+no)
        #print(x, y)
        if x != 0 and y != 0:
            #print(x, y)
            gain = gain + (mydict[key] * (x*math.log2(x) + y*math.log2(y)))/14

    return gain


#print(findGain(0), findGain(1), findGain(2), findGain(3))

def buildTree(arr):
    max = -100000
    idx = -1
    for i in range(0, len(arr[0])-1):
        temp = findGain(arr, i)
        if max < temp:
            max = temp
            idx = i

    


buildTree(X)
