import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

dataset = pd.read_csv('Iris.csv')
df = dataset.iloc[:, [1, 3]].values

x1 = df[:,0]
x2 = df[:,1]

setosa_x = x1[:40]
setosa_y = x2[:40]

versicolor_x = x1[40:80]
versicolor_y = x2[40:80]

test_x1 = x1[81:]
test_x2 = x2[81:]
#plt.figure(figsize=(8,6))

def abline(slope, intercept):
    Xi = np.array([0,8])
    
    plt.scatter(setosa_x,setosa_y,color='green')
    plt.scatter(versicolor_x,versicolor_y,color='red')

    plt.plot(Xi, Xi*slope + intercept, color = "black")
    #plt.pause(0.001)
    plt.draw()

# Importing the dataset

def sigm(t):
    return 1/(1+np.exp(-t))



def gradient_descent():
    n = 80
    alpha = 0.25
    theta2 = 0
    theta1 = 0
    theta0 = 0  
    for i in range(0,100):
        #plt.clf()
        plt.axis([0,8,0,6])
        #plt.scatter(X,y,color="red")
        yguess = []
        for j in range(0,n):
            res = sigm(theta1 * x1[j] + theta2*x2[j] + theta0)
            if res < 0.5:
                res = 0
            else:
                res = 1
            yguess.append(res)
        for j in range(0,n):
            if yguess[j] > 0.5:
                yguess[j] = 1
            else:
                yguess[j] = 0
        ynew = []
        for j in range(0,n):
         if j < 40 :
             p=0
         else:
             p=1

         ynew.append((yguess[j]-p) * x2[j])

        derivative2 = sum(ynew) / n

        ynew = []
        for j in range(0,n):
         if j < 40 :
             p=0
         else:
             p=1
         ynew.append((yguess[j]-p) * x1[j])

        derivative1 = sum(ynew) / n

        ynew = []
        for j in range(0,n):
         if j < 40 :
             p=0
         else:
             p=1
         ynew.append(yguess[j] - p)

        derivative0 = sum(ynew) / n
        
        theta0 = theta0 - alpha * derivative0
        theta1 = theta1 - alpha * derivative1
        theta2 = theta2 - alpha * derivative2

    abline(-theta1/theta2,-theta0/theta2)
    #print(theta2,theta1,theta0)
    #print(-theta1/theta2,-theta0/theta2)
    return theta0,theta1,theta2

setosa_x_result = []
setosa_y_result = []
verticolor_x_result = []
verticolor_y_result = []

t0,t1,t2 = gradient_descent()

for i in range(0,len(test_x1)):
    result = sigm(t2*test_x2[i] + t1*test_x1[i] + t0)
    #print(result)
    if result < 0.5 :
        setosa_x_result.append(test_x1[i])
        setosa_y_result.append(test_x2[i])
    else:
        verticolor_x_result.append(test_x1[i])
        verticolor_y_result.append(test_x2[i])


plt.scatter(setosa_x_result,setosa_y_result,color='blue')
plt.scatter(verticolor_x_result,verticolor_y_result,color='black')
plt.show()

