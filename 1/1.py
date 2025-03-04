import numpy as np
import matplotlib.pyplot as plt

COUNT_POINTS = 1000
COUNT_ITERS = 5

def x0(t):
    return t

def T(t, iter):
    if (iter == 0):
        return x0(t)

    iter -= 1
    if 0 <= t <= 1/3:
        return -1/8 * T(3 * t, iter)
    if 1/3 < t < 2/3:
        return -1/8 * (1 + T(1, iter) - np.cos(np.pi/6 * (t - 1/3)))
    if 2/3 <= t <= 1:
        return -1/8 * T(3 * t - 2, iter) + 1/8 * (T(0, iter) - T(1, iter) - 1 + np.cos(np.pi/18))

x = np.linspace(0, 1, COUNT_POINTS)

y = [T(t, 5) for t in x]
plt.plot(x, y, marker='o', linestyle='-', color='r', label='5 итераций')

y = [T(t, 10) for t in x]
plt.plot(x, y, marker='o', linestyle='-', color='g', label='10 итераций')

y = [T(t, 15) for t in x]
plt.plot(x, y, marker='o', linestyle='-', color='b', label='15 итераций')

# Добавление подписей и заголовка
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Неподвижная точка')
plt.legend()

# Отображение графика
plt.grid(True)
plt.show()