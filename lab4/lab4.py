import matplotlib.pyplot as plt
from math import *
from lab1 import lab1


def main_action(x, y, out):
    fi1, s1, sko1, a1, b1 = linear(x, y, len(x))
    fi2, s2, sko2, a2, b2, c = polynomial(x, y, len(x))
    fi3, s3, sko3, a3, b3 = exponential(x, y, len(x))
    fi4, s4, sko4, a4, b4 = logarithmic(x, y, len(x))
    fi5, s5, sko5, a5, b5 = power(x, y, len(x))
    if out == 'k':
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('Вид fi(x)', 'Линейная', 'Полиномиальная', 'Экспоненциальная', 'Логарифмическая', 'Степенная'))
    elif out == 'f':
        pass
    else:
        print('Неверный выбор формата вывода. Введите k или f для корректной работы.')


def sko(fi, y):
    res = 0
    for i in range(len(fi)):
        res += (fi[i] - y[i]) ** 2
    return sqrt(res / len(fi))


def linear(x, y, n):
    # Линейная функция
    sx = sum(x)
    sy = sum(y)
    sxx = sum([elem ** 2 for elem in x])
    sxy = sum([y[i] * x[i] for i in range(n)])
    a = (sxy * n - sx * sy) / (sxx * n - sx * sx)
    b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
    # print(a,b)
    # for i in range(n):
    #     print(a*x[i]+b, a*x[i]+b-y[i])
    ylin = [a * x[i] + b for i in range(n)]
    plt.plot(x, ylin)
    plt.grid(True)
    # plt.show()
    slin = 0
    for i in range(n):
        slin += (ylin[i] - y[i]) ** 2
    # print(slin)
    # print(sko(ylin, y))
    return ylin, slin, sko(ylin, y), a, b


def polynomial(x, y, n):
    # Квадратичная функция
    sx = sum(x)
    sy = sum(y)
    sxx = sum([elem ** 2 for elem in x])
    sxy = sum([y[i] * x[i] for i in range(n)])
    sxxx = sum([elem ** 3 for elem in x])
    sxxxx = sum([elem ** 4 for elem in x])
    sxxy = sum([y[i] * x[i] ** 2 for i in range(n)])
    a0, a1, a2 = lab1.solve([[n, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]], [sy, sxy, sxxy], 3)
    # for i in range(n):
    #     print(a2*x[i]**2+a1*x[i]+a0, a2*x[i]**2+a1*x[i]+a0 - y[i])
    ypol = [a2 * x[i] ** 2 + a1 * x[i] + a0 for i in range(n)]
    plt.plot(x, ypol)
    plt.grid(True)
    # plt.show()
    spol = 0
    for i in range(n):
        spol += (ypol[i] - y[i]) ** 2
    # print(spol)
    # print(sko(ypol, y))
    return ypol, spol, sko(ypol, y), a2, a1, a0


def exponential(x, y, n):
    # Экспоненциальная функция
    sx = sum(x)
    sxx = sum([elem ** 2 for elem in x])
    sxy = sum([log(y[i]) * x[i] for i in range(n)])
    sy = sum([log(y[i]) for i in range(n)])
    a = exp((sxy * n - sx * sy) / (sxx * n - sx * sx))
    b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
    # for i in range(n):
    #     print(a*exp(b*x[i]), a*exp(b*x[i]) - y[i])
    yexp = [a * exp(b * x[i]) for i in range(n)]
    plt.plot(x, yexp)
    plt.grid(True)
    # plt.show()
    sexp = 0
    for i in range(n):
        sexp += (yexp[i] - y[i]) ** 2
    # print(sexp)
    # print(sko(yexp, y))
    return yexp, sexp, sko(yexp, y), a, b


def logarithmic(x, y, n):
    # Логарифмическая функция

    sx = sum([log(elem) for elem in x])
    sy = sum(y)
    sxx = sum([(log(elem)) ** 2 for elem in x])
    sxy = sum([y[i] * log(x[i]) for i in range(n)])
    a = (sxy * n - sx * sy) / (sxx * n - sx * sx)
    b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
    # for i in range(n):
    # print(a*log(x[i])+b, a*log(x[i])+b - y[i])
    ylog = [a * log(x[i]) + b for i in range(n)]
    plt.plot(x, ylog)
    plt.grid(True)
    # plt.show()
    slog = 0
    for i in range(n):
        slog += (ylog[i] - y[i]) ** 2
    # print(slog)
    # print(sko(ylog, y))
    return ylog, slog, sko(ylog, y), a, b


def power(x, y, n):
    # Степенная функция
    sx = sum([log(elem) for elem in x])
    sy = sum([log(elem) for elem in y])
    sxx = sum([(log(elem)) ** 2 for elem in x])
    sxy = sum([log(y[i]) * log(x[i]) for i in range(n)])
    a = exp((sxy * n - sx * sy) / (sxx * n - sx * sx))
    b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
    # for i in range(n):
    #    print(a*x[i]**b, a*x[i]**b - y[i])
    ystep = [a * x[i] ** b for i in range(n)]
    plt.plot(x, ystep)
    plt.grid(True)
    # plt.show()
    sstep = 0
    for i in range(n):
        sstep += (ystep[i] - y[i]) ** 2
    # print(sstep)
    # print(sko(ystep, y))
    return ystep, sstep, sko(ystep, y), a, b


inp = input("Вы хотите вводить с клавиатуры(k) или из файла(f)?\n")
out = input("Вы хотите выводить на консоль(k) или в файл(f)?\n")
if inp == 'k':
    x = list(map(float, input("Введите координаты х через пробел:\n").split()))
    y = list(map(float, input("Введите координаты y через пробел:\n").split()))
    main_action(x, y, out)
elif inp == 'f':
    path = input("Введите путь к файлу с исходными данными:\n")
    with open(path, 'r') as f:
        x = list(map(float, f.readline().split()))
        y = list(map(float, f.readline().split()))
        main_action(x, y, out)
else:
    print('Неверный выбор формата ввода. Введите k или f для корректной работы.')
