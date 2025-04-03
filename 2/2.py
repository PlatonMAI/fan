# k = 7, l = 10, вариант = 7

# [a, b] = [0; 1.5]

# f(t) = (4 - t) ^ 2 = t^2 - 8t + 16
# y(t) = sin(3t)


from random import random
import numpy as np
import matplotlib.pyplot as plt


def plot(ys, iter):
    plt.plot(ts, ys, linestyle='-', color=(random(), random(), random()), label=f"{iter} степень")


def f(t):
    return t ** 2 - 8 * t + 16
def y(t):
    return np.sin(3 * t)

def calcIntegral(values):
    integral = 0
    for i in range(1, countPoints):
        integral += step * (values[i] + values[i - 1]) / 2

    return integral

def calcScalarProduct(xs, ys):
    values = xs * ys * fs
    return calcIntegral(values)

def calcNorm(xs):
    return np.sqrt(calcScalarProduct(xs, xs))

def calcValuesPolynom(polynom):
    values = np.zeros(countPoints)
    for i in range(countPoints):
        curDegreeT = 1
        for coef in polynom:
            values[i] += coef * curDegreeT
            curDegreeT *= ts[i]

    return values

def calcLengthProjectionError(projection):
    # Инициализация истинным значением приближаемой функции
    values = np.copy(ys)
        
    # Вычитаем текущее приближение многочленом
    values -= calcValuesPolynom(projection)

    return calcNorm(values)

def calcProjection(projection: list, newElem, curDegree):
    projection.append(0)
    coef = calcScalarProduct(calcValuesPolynom(newElem), ys)
    for coord in range(curDegree + 1):
        projection[coord] += coef * newElem[coord]

def solve(eps):
    system = []
    curDegree = -1
    projection = []

    while (True):
        # Вычисляем текущую длину ошибки проектирования
        error = calcLengthProjectionError(projection)

        # Останавливаемся когда длина ошибки проектирования будет меньше заданной точности
        if error < eps:
            break

        # Увеличиваем степень многочлена
        # Добавляем еще один элемент в текущую ортонормированную систему функций

        # Ортогонализируем - для каждого элемента из системы вычисляем свой коэффициент
        curDegree += 1
        newElem = [0] * (curDegree + 1)
        newElem[curDegree] = 1
        for elem in system:
            coef = calcScalarProduct(calcValuesPolynom(newElem), calcValuesPolynom(elem))
            for coord in range(len(elem)):
                newElem[coord] -= coef * elem[coord]
        
        # Нормируем
        normNewElem = calcNorm(calcValuesPolynom(newElem))
        for coord in range(curDegree + 1):
            newElem[coord] /= normNewElem

        system.append(newElem)

        # Пересчитываем проекцию
        calcProjection(projection, newElem, curDegree)

        plot(calcValuesPolynom(projection), curDegree)


a = 0
b = 1.5

degreeCountPoints = int(input("Порядок количества точек - 10 ^ "))
countPoints = int(pow(10, degreeCountPoints) + 1)
eps = float(input("Точность: "))

ts = np.linspace(a, b, countPoints)
ys = np.array([y(t) for t in ts])
fs = np.array([f(t) for t in ts])
step = (b - a) / (countPoints - 1)

plt.plot(ts, ys, linestyle='-', color=(random(), random(), random()), label=f"sin(3x)")

solve(eps)

plt.title(f"Приближение sin(3x) (точность {eps})")
plt.legend()

plt.grid(True)
plt.show()
