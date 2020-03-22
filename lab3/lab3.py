# f(x) : x^3−1.89x^2−2x+1.76=0
x2 = -1.15624  # (интервал изоляции: [-2;-1])
x3 = 0.629971  # (интервал изоляции: [0;1])
x1 = 2.41627  # (интервал изоляции: [2;3])

import pylab


def f(x):
    # return x**3 - x + 4
    return x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76


def fi1(x):
    return (x ** 3 - 1.89 * x ** 2 + 1.76) / 2


def derivative_fi1(x):
    return 1.5 * (x - 1.26) * x


def fi2(x):
    return ((x ** 3 - 2 * x + 1.76) / 1.89) ** (1 / 2)


def derivative_fi2(x):
    return (1.09109 * x ** 2 - 0.727393) / ((x ** 3 - 2 * x + 1.76) ** (1 / 2))


def fi3(x):
    return (1.89 * x ** 2 + 2 * x - 1.76) ** (1 / 3)


def derivative_fi3(x):
    return (1.26 * x + 2 / 3) / ((1.89 * x ** 2 + 2 * x - 1.76) ** (2 / 3))


def fi4(x, a, b):
    l = -1 / max(derivative(a), derivative(b))
    return x + l * f(x)


def derivative(x):
    return 3 * x ** 2 - 3.78 * x - 2


def second_derivative(x):
    # return 6 * x
    return 6 * x - 3.78


xmin = -10.0
xmax = 10.0
dx = 0.01
xlist = [x / 10.0 for x in range(-40, 40)]
ylist = [f(x) for x in xlist]
pylab.plot(xlist, ylist)
pylab.show()
# e1 = e2 = e3 = 0.01  # Точность вычисления
# Границы интервалов изоляции корней
# r1 = 3
# l1 = 2
# r2 = -1
# l2 = -2
# r3 = 1
# l3 = 0

hords = []
print("Метод хорд для правого корня")
l1 = float(input("Введите левую границу\n"))
r1 = float(input("Введите правую границу\n"))
e1 = float(input("Введите точность\n"))
if l1 <= x1 <= r1:
    if f(l1) * second_derivative(l1) > 0:
        hords.append(r1)
        i = 0
        print(i, l1, r1, hords[i], f(l1), f(r1), f(hords[i]), '-')
        while True:
            hords.append(l1 - f(l1) * (hords[i] - l1) / (f(hords[i]) - f(l1)))
            i += 1
            print(i, l1, hords[i - 1], hords[i], f(l1), f(hords[i - 1]), f(hords[i]), abs(hords[i] - hords[i - 1]))
            if abs(hords[i] - hords[i - 1]) <= e1 or abs(f(hords[i])) <= e1:
                break
    else:
        hords.append(l1)
        i = 0
        print(i, l1, r1, hords[i], f(l1), f(r1), f(hords[i]), '-')
        while True:
            hords.append(hords[i] - f(hords[i]) * (r1 - hords[i]) / (f(r1) - f(hords[i])))
            i += 1
            print(i, hords[i - 1], r1, hords[i], f(hords[i - 1]), f(r1), f(hords[i]), abs(hords[i] - hords[i - 1]))
            if abs(hords[i] - hords[i - 1]) <= e1 or abs(f(hords[i])) <= e1:
                break

secants = []
print("Метод секущих для левого корня")
l2 = float(input("Введите левую границу\n"))

r2 = float(input("Введите правую границу\n"))
e2 = float(input("Введите точность\n"))
if f(l2) * second_derivative(l2) > 0:
    print("x0 =", l2)
    secants.append(l2)
else:
    print("x0 =", r2)
    secants.append(r2)
secants.append(float(input("Введите x1\n")))
i = 1
while True:
    secants.append(secants[i] - f(secants[i]) * (secants[i] - secants[i - 1]) / (f(secants[i]) - f(secants[i - 1])))
    print(i, secants[i - 1], f(secants[i - 1]), secants[i], f(secants[i]), secants[i + 1], f(secants[i + 1]),
          abs(secants[i + 1] - secants[i]))
    if abs(secants[i + 1] - secants[i]) <= e2 or abs(f(secants[i + 1])) <= e2:
        break
    i += 1

iterations = []
print("Метод простых итераций для центрального корня")
l3 = float(input("Введите левую границу\n"))
r3 = float(input("Введите правую границу\n"))
# iterations.append(float(input("Введите начальное приближение:\n")))
e3 = float(input("Введите точность\n"))
iterations.append((l3+r3)/2)
i = 0
if abs(derivative_fi1(l3)) < 1 and abs(derivative_fi1(r3)) < 1:
    while True:
        iterations.append(fi1(iterations[i]))
        print(i + 1, iterations[i], f(iterations[i]), iterations[i + 1], abs(iterations[i + 1] - iterations[i]))
        i += 1
        if abs(iterations[i] - iterations[i - 1]) <= e3:
            break

elif abs(derivative_fi2(l3)) < 1 and abs(derivative_fi2(r3)) < 1:
    while True:
        iterations.append(fi2(iterations[i]))
        print(i + 1, iterations[i], f(iterations[i]), iterations[i + 1], abs(iterations[i + 1] - iterations[i]))
        i += 1
        if abs(iterations[i] - iterations[i - 1]) <= e3:
            break
elif abs(derivative_fi3(l3)) < 1 and abs(derivative_fi3(r3)) < 1:
    while True:
        iterations.append(fi3(iterations[i]))
        print(i + 1, iterations[i], f(iterations[i]), iterations[i + 1], abs(iterations[i + 1] - iterations[i]))
        i += 1
        if abs(iterations[i] - iterations[i - 1]) <= e3:
            break
else:
    while True:
        iterations.append(fi4(iterations[i],l3,r3))
        print(i + 1, iterations[i], f(iterations[i]), iterations[i + 1], abs(iterations[i + 1] - iterations[i]))
        i += 1
        if abs(iterations[i] - iterations[i - 1]) <= e3:
            break
