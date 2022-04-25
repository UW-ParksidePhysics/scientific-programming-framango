from numpy import *
from matplotlib.pyplot import *

v0 = 10
g = 9.81
t = linspace(0, 2 * v0 / g, 100)


def ball(t):
    y = v0 * t - 0.5 * g * t ** 2
    return y


xlist = t.tolist()
ylist = [ball(i) for i in xlist]
plot(xlist, ylist)
xlabel('time')
ylabel('height')
show()