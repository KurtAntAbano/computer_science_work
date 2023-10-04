import matplotlib.pyplot as plt # abbreviatied ver is plt to shorten typing

def plotGra(x,y,xl,yl,t):
    plt.plot(x, y)
    plt.title(t)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.show()
# xVal = [1, 2, 3]
# yVal = [2, 4, 1]
# xLab = "X-Value"
# yLab = "Y-Value"
# tLab = "Generic Graph"
# plotGra(xVal,yVal,xLab,yLab,tLab)