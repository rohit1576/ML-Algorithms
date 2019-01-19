import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = []
y = []


def abline(slope, intercept):
    Xi = np.array([0,20])
    plt.plot(Xi, Xi*slope + intercept, color = "black")
    plt.pause(0.001)
    plt.draw()


def gradient_descent():
    n = len(X)
    alpha = 0.0075
    m = 0
    b = 0
    for i in range(0,100):
        plt.clf()
        plt.scatter(X,y,color="red")
        yguess = []
        for j in range(0,n):
            yguess.append(m * X[j] + b)
        
        ynew = []
        for j in range(0,n):
         ynew.append((yguess[j]-y[j]) * X[j])
        derivative1 = sum(ynew) / n
        ynew = []
        for j in range(0,n):
            ynew.append(yguess[j] - y[j])
        derivative0 = sum(ynew) / n
        
        m = m - alpha * derivative1
        b = b - alpha * derivative0
        abline(m,b)
        
    #abline(m,b)

fig = plt.figure()
ax = fig.add_subplot(111)


def onclick(event):
    plt.clf()
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))

    X.append(event.xdata)
    y.append(event.ydata)

    plt.scatter(X,y,color="red")
 
    gradient_descent()    

    

cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.show()

