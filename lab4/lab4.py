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
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('Вид fi(x)', 'Линейная', 'Полиномиальная', 'Экспоненциальная',
                                                      'Логарифмическая', 'Степенная'))
        print("{:10}{:10}{:20}{:20}{:20}{:20}{:20}".format('X', 'Y', 'F = ax+b', 'F = ax^2+bx+c',
                                                           'F = ae^(bx)', 'F = alnx+b', 'F = ax^b'))
        for i in range(len(x)):
            print("{:10}{:10}{:20}{:20}{:20}{:20}{:20}".format(x[i], y[i], fi1[i], fi2[i],
                                                               fi3[i], fi4[i], fi5[i]))
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('S', s1, s2, s3, s4, s5))
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('Среднекв. отклонение', sko1, sko2, sko3, sko4, sko5))
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('a', a1, a2, a3, a4, a5))
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('b', b1, b2, b3, b4, b5))
        print("{:20}{:20}{:20}{:20}{:20}{:20}".format('c', '-', c, '-', '-', '-'))
    elif out == 'f':
        with open('output.txt', 'w') as f:
            f.write(
                "{:20}{:20}{:20}{:20}{:20}{:20}\n".format('Вид fi(x)', 'Линейная', 'Полиномиальная', 'Экспоненциальная',
                                                          'Логарифмическая', 'Степенная'))
            f.write("{:10}{:10}{:20}{:20}{:20}{:20}{:20}\n".format('X', 'Y', 'F = ax+b', 'F = ax^2+bx+c',
                                                                   'F = ae^(bx)', 'F = alnx+b', 'F = ax^b'))
            for i in range(len(x)):
                f.write("{:10}{:10}{:20}{:20}{:20}{:20}{:20}\n".format(x[i], y[i], fi1[i], fi2[i],
                                                                       fi3[i], fi4[i], fi5[i]))
            f.write("{:20}{:20}{:20}{:20}{:20}{:20}\n".format('S', s1, s2, s3, s4, s5))
            f.write("{:20}{:20}{:20}{:20}{:20}{:20}\n".format('Среднекв. отклонение', sko1, sko2, sko3, sko4, sko5))
            f.write("{:20}{:20}{:20}{:20}{:20}{:20}\n".format('a', a1, a2, a3, a4, a5))
            f.write("{:20}{:20}{:20}{:20}{:20}{:20}\n".format('b', b1, b2, b3, b4, b5))
            f.write("{:20}{:20}{:20}{:20}{:20}{:20}\n".format('c', '-', c, '-', '-', '-'))
    else:
        print('Неверный выбор формата вывода. Введите k или f для корректной работы.')


def sko(fi, y):
    res = 0
    for i in range(len(fi)):
        res += (fi[i] - y[i]) ** 2
    return sqrt(res / len(fi))


def find_coeffs(sx, sy, sxx, sxy, n):
    return (sxy * n - sx * sy) / (sxx * n - sx * sx), (sxx * sy - sx * sxy) / (sxx * n - sx * sx)


def linear(x, y, n):
    sx = sum(x)
    sy = sum(y)
    sxx = sum([elem ** 2 for elem in x])
    sxy = sum([y[i] * x[i] for i in range(n)])
    a, b = find_coeffs(sx, sy, sxx, sxy, n)
    ylin = [a * x[i] + b for i in range(n)]
    plt.plot(x, ylin, label = 'Линейный')
    plt.grid(True)
    #plt.show()
    slin = 0
    for i in range(n):
        slin += (ylin[i] - y[i]) ** 2
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
    ypol = [a2 * x[i] ** 2 + a1 * x[i] + a0 for i in range(n)]
    plt.plot(x, ypol, label = 'Квадратичный')
    plt.grid(True)
    # plt.show()
    spol = 0
    for i in range(n):
        spol += (ypol[i] - y[i]) ** 2
    return ypol, spol, sko(ypol, y), a2, a1, a0


def exponential(x, y, n):
    # Экспоненциальная функция
    sx = sum(x)
    sxx = sum([elem ** 2 for elem in x])
    sxy = sum([log(y[i]) * x[i] for i in range(n)])
    sy = sum([log(y[i]) for i in range(n)])
    a, b = find_coeffs(sx, sy, sxx, sxy, n)
    #a = exp(a)
    yexp = [a * exp(b * x[i]) for i in range(n)]
    plt.plot(x, yexp, label = 'Экспоненциальный')
    plt.grid(True)
    # plt.show()
    sexp = 0
    for i in range(n):
        sexp += (yexp[i] - y[i]) ** 2
    return yexp, sexp, sko(yexp, y), a, b


def logarithmic(x, y, n):
    # Логарифмическая функция

    sx = sum([log(elem) for elem in x])
    sy = sum(y)
    sxx = sum([(log(elem)) ** 2 for elem in x])
    sxy = sum([y[i] * log(x[i]) for i in range(n)])
    a, b = find_coeffs(sx, sy, sxx, sxy, n)
    ylog = [a * log(x[i]) + b for i in range(n)]
    plt.plot(x, ylog, label = 'Логарифмический')
    plt.grid(True)
    # plt.show()
    slog = 0
    for i in range(n):
        slog += (ylog[i] - y[i]) ** 2
    return ylog, slog, sko(ylog, y), a, b


def power(x, y, n):
    # Степенная функция
    sx = sum([log(elem) for elem in x])
    sy = sum([log(elem) for elem in y])
    sxx = sum([(log(elem)) ** 2 for elem in x])
    sxy = sum([log(y[i]) * log(x[i]) for i in range(n)])
    a, b = find_coeffs(sx, sy, sxx, sxy, n)
    #a = exp(a)
    ystep = [a * x[i] ** b for i in range(n)]
    plt.plot(x, ystep, label = 'Степенной')
    plt.grid(True)
    #plt.show()
    sstep = 0
    for i in range(n):
        sstep += (ystep[i] - y[i]) ** 2
    return ystep, sstep, sko(ystep, y), a, b


inp = input("Вы хотите вводить с клавиатуры(k) или из файла(f)?\n")
out = input("Вы хотите выводить на консоль(k) или в файл(f)?\n")
if inp == 'k':
    x = list(map(float, input("Введите координаты х через пробел:\n").split()))
    y = list(map(float, input("Введите координаты y через пробел:\n").split()))
    main_action(x, y, out)
    plt.plot(x, y, marker='o', label='Изначальный')
    plt.legend()
    plt.show()
elif inp == 'f':
    path = input("Введите путь к файлу с исходными данными:\n")
    with open(path, 'r') as f:
        x = list(map(float, f.readline().split()))
        y = list(map(float, f.readline().split()))
        main_action(x, y, out)
        plt.plot(x,y, marker = 'o', label='Изначальный')
        plt.legend()
        plt.show()
else:
    print('Неверный выбор формата ввода. Введите k или f для корректной работы.')
