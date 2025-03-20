from random import random
import numpy as np
import matplotlib.pyplot as plt

ALPHA = 0.375
COUNT_POINTS = int(1e4 - 1)
EPS = 1e-1

def plot(x, y, iter):
    plt.plot(x, y, linestyle='-', color=(random(), random(), random()), label=f"{iter} итераций")

def x0(t):
    return 0
# def x0(t):
#     return t
# def x0(t):
#     return t ** 2 - t

ts = np.linspace(0, 1, COUNT_POINTS)
prevX = dict()
for i in range(COUNT_POINTS):
    prevX[i] = x0(ts[i])

iter = 1
while (True):
    curX = dict()
    isPlot = iter > 4

    # Строим функцию
    for i in range(COUNT_POINTS):
        t = i/(COUNT_POINTS-1)
        prevX_0 = prevX[0]
        prevX_1 = prevX[COUNT_POINTS-1]

        if 0 <= i < COUNT_POINTS/3:
            curX[i] = -1/8 * prevX[3 * i]
        elif COUNT_POINTS/3 <= i < 2*COUNT_POINTS/3:
            curX[i] = -1/8 * (1 + prevX_1 - np.cos(6 * np.pi * (t - 1/3)))
        elif 2*COUNT_POINTS/3 <= i < COUNT_POINTS:
            curX[i] = -1/8 * (prevX[3 * i - 2*COUNT_POINTS] + prevX_1 - prevX_0)

    if (isPlot):
        plot(ts, curX.values(), iter)

    # Расстояние
    rho = 0
    for i in range(COUNT_POINTS):
        rho = max(rho, abs(curX[i] - x0(ts[i])))

    # Погрешность
    curEps = ALPHA ** iter / (1 - ALPHA) * rho

    if (curEps < EPS):
        if (not isPlot):
            plot(ts, curX.values(), iter)
        break
    
    iter += 1
    prevX = curX

print(f"{iter} итераций")

plt.title(f"Неподвижная точка (точность {EPS})")
plt.legend()

plt.grid(True)
plt.show()
