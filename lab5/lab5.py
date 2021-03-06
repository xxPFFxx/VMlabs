from lab1 import lab1
from math import *


def splitted_difference(a, b, f_a, f_b):
    return (f_b - f_a) / (b - a)


def finite_difference(a, b):
    return a - b


def newton_helper(massx, massy, index1, x):
    f_xo_x1 = splitted_difference(massx[index1], massx[index1 + 1], massy[index1], massy[index1 + 1])
    f_x1_x2 = splitted_difference(massx[index1 + 1], massx[index1 + 2], massy[index1 + 1], massy[index1 + 2])
    f_x0_x1_x2 = splitted_difference(massx[index1], massx[index1 + 2], f_xo_x1, f_x1_x2)
    return massy[index1] + f_xo_x1 * (x - massx[index1]) + f_x0_x1_x2 * (x - massx[index1]) * (x - massx[index1 + 1])


def linear_interpolation(massx, massy, x):
    for i in range(1, len(massx)):
        if massx[i - 1] <= x <= massx[i]:
            a = (massy[i] - massy[i - 1]) / (massx[i] - massx[i - 1])
            b = massy[i - 1] - a * massx[i - 1]
            return a * x + b


def quadratic_interpolation(massx, massy, x):
    min = abs(massx[0] - x) + abs(massx[1] - x) + abs(massx[2] - x)
    min_i = 1
    for i in range(2, len(massx) - 1):
        if abs(massx[i - 1] - x) + abs(massx[i] - x) + abs(massx[i + 1] - x) < min:
            min = abs(massx[i - 1] - x) + abs(massx[i] - x) + abs(massx[i + 1] - x)
            min_i = i
    a, b, c = lab1.solve([[massx[min_i - 1] ** 2, massx[min_i - 1], 1], [massx[min_i] ** 2, massx[min_i], 1],
                          [massx[min_i + 1] ** 2, massx[min_i + 1], 1]],
                         [massy[min_i - 1], massy[min_i], massy[min_i + 1]], 3)
    return a * x ** 2 + b * x + c


def lagrange_polynomial(massx, massy, x):
    s = 0
    for i in range(len(massx)):
        count = 1
        for j in range(len(massx)):
            if j != i:
                count *= (x - massx[j])
                count /= (massx[i] - massx[j])
        s += massy[i] * count
    return s


def newton_unequal_nodes(massx, massy, x):
    index1 = index2 = 0
    for i in range(len(massx)):
        if x > massx[i]:
            index1 = i - 1
            index2 = i
    s1 = newton_helper(massx, massy, index1, x)
    s2 = newton_helper(massx, massy, index2, x)
    return (s1 + s2) / 2


def newton_counter(i, t, table):
    if i == 0:
        return table[0][0]
    else:
        return newton_counter(i - 1, t, table)


def newton_equal_nodes(massx, massy, x):
    table = []
    s = 0
    h = massx[1] - massx[0]
    for i in range(len(massx)):
        if x > massx[i]:
            max_i = i
    if x <= (massx[0] + massx[-1]) / 2:
        table.append(massy[max_i:])
        for j in range(1, len(massx) - 1):
            table.append([finite_difference(table[j - 1][i + 1], table[j - 1][i]) for i in range(len(massx) - 1 - j)])
        t = (x - massx[max_i]) / h
        m = 1
        f = 0
        for i in range(len(table)):
            s += m * table[i][0]
            m *= (t - i)
            f += 1
            m /= f
        return s
    else:
        table.append(massy[:max_i+2])
        for j in range(1, len(massx) - 1):
            table.append([finite_difference(table[j - 1][i + 1], table[j - 1][i]) for i in range(len(massx) - 1 - j)])
        t = (x - massx[max_i+1]) / h
        m = 1
        f = 0
        for i in range(len(table)):
            s += m * table[i][-1]
            m *= (t + i)
            f += 1
            m /= f
        return s

inp = input("Вы желаете вводить с клавиатуры(k) или из файла(f)?\n")
if inp == 'k':
    table_x = list(map(float, input('Введите координаты х через пробел:\n').split()))
    table_y = list(map(float, input('Введите координаты y через пробел:\n').split()))
    x = float(input('Введите координату x, для которой хотите найти приближенное значение функции:\n'))
    print('Линейная интерполяция:', linear_interpolation(table_x, table_y, x))
    print('Квадратичная интерполяция:', quadratic_interpolation(table_x, table_y, x))
    print('Полином Лагранжа:', lagrange_polynomial(table_x, table_y, x))
    print('Полином Ньютона:', newton_unequal_nodes(table_x, table_y, x))
    print('Полином Нютона вперед:', newton_equal_nodes(table_x, table_y, x))
    print('Полином Нютона назад:', newton_equal_nodes(table_x, table_y, x))
elif inp == 'f':
    path = input("Введите путь до файла с исходными данными:\n")
    with open(path, 'r') as f:
        table4_x = list(map(float, f.readline().split()))
        table4_y = list(map(float, f.readline().split()))
        x1, x4 = map(float, f.readline().split())
        table8_x = list(map(float, f.readline().split()))
        table8_y = list(map(float, f.readline().split()))
        x2, x3 = map(float, f.readline().split())
        print('Линейная интерполяция:', linear_interpolation(table4_x, table4_y, x1))
        print('Квадратичная интерполяция:', quadratic_interpolation(table4_x, table4_y, x1))
        print('Полином Лагранжа:', lagrange_polynomial(table4_x, table4_y, x1))
        print('Полином Ньютона:', newton_unequal_nodes(table4_x, table4_y, x4))
        print('Полином Нютона вперед:', newton_equal_nodes(table8_x, table8_y, x2))
        print('Полином Нютона назад:', newton_equal_nodes(table8_x, table8_y, x3))
else:
    print("Неверный ввод. Для ввода с клавиаутуры выберите k, для ввода из файла f.")
