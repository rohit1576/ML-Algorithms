
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X = []
y = []

def abline(slope, intercept):
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '--')


def calculate(): 
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
    abline(m,c)
    return m,c


#plt.scatter(X, y, color = 'red')
#abline(slope = m,intercept = c)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])

def onclick(event):
    plt.clf()
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))
    X.append(event.xdata)
    y.append(event.ydata)
    print(X)
    print(y)
    plt.scatter(X,y,color="red")
 
    #plt.scatter(event.xdata, event.ydata, color="red")
    if len(X) > 1:
        slope,intercept = calculate()
        for i in range(0,len(X)) :
           plt.plot([X[i],X[i]],[y[i],slope*X[i] + intercept],'--')
    fig.canvas.draw()
    

cid = fig.canvas.mpl_connect('button_press_event', onclick)
plt.show()

