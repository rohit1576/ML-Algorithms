import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])
y2 = np.array([9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74])
y3 = np.array([7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73])
x4 = np.array([8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0])
y4 = np.array([6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89])

def abline(slope, intercept):
    X = np.array([0,20])
    plt.plot(X, X*slope + intercept, '--')

def calculate(X,y,i): 
    xbar = sum(X)/len(X)
    ybar = sum(y)/len(y)
    Xmod=X
    Xmod = X-xbar
    ymod = y
    ymod = ymod - ybar
    m = (Xmod * ymod)
    m = sum(m)
    z = Xmod * Xmod
    z = sum(z)
    m = m / z
    c = ybar - m*xbar
    plt.subplot(2,2,i)
    plt.scatter(X,y,color="red")
    abline(m,c)

plt.figure()
plt.xlim(0,20)
plt.ylim(0,20)

calculate(x,y1,1)
calculate(x,y2,2)
calculate(x,y3,3)
calculate(x4,y4,4)

plt.show()