from random import random
import numpy as np
import matplotlib.pyplot as plt

ALPHA = 0.125
COUNT_POINTS = int(1e4 - 1)
EPS = 1e-10

def plot(x, y, iter):
    plt.plot(x, y, linestyle='-', color=(random(), random(), random()), label=f"{iter} итераций")

# def x0(t):
#     return t
# def x0(t):
#     return -0.0015 * t
# def x0(t):
#     return 47125/9072*t**9 - 45725/2016*t**8 + 255085/6048*t**7 - 25499/576*t**6 + 1013549/34560*t**5 - 1478083/115200*t**4 + 16630303/4536000*t**3 - 13028291/20160000*t**2 + 3180851/50400000*t - 497/200000
def x0(t):
    return 0

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
            curX[i] = -1/8 * (1 + prevX_1 - np.cos(np.pi/6 * (t - 1/3)))
        elif 2*COUNT_POINTS/3 <= i < COUNT_POINTS:
            curX[i] = -1/8 * prevX[3 * i - 2*COUNT_POINTS] + 1/8 * (prevX_0 - prevX_1 - 1 + np.cos(np.pi/18))

    if (isPlot):
        plot(ts, curX.values(), iter)

    # Расстояние
    rho = 0
    for i in range(COUNT_POINTS):
        rho = max(rho, abs(curX[i] - prevX[i]))

    # Погрешность
    curEps = ALPHA / (1 - ALPHA) * rho

    if (curEps < EPS):
        if (not isPlot):
            plot(ts, curX.values(), iter)
        break
    
    iter += 1
    prevX = curX

print(f"{iter} итераций")

plt.title('Неподвижная точка')
plt.legend()

plt.grid(True)
plt.show()
