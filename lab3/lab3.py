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


def hords_method(l1, r1, e1, output):
    hords = []

    if l1 <= x1 <= r1:
        if f(l1) * second_derivative(l1) > 0:
            hords.append(r1)
            i = 0
            while True:
                hords.append(l1 - f(l1) * (hords[i] - l1) / (f(hords[i]) - f(l1)))
                i += 1
                if abs(hords[i] - hords[i - 1]) <= e1 or abs(f(hords[i])) <= e1:
                    break
        else:
            hords.append(l1)
            i = 0
            while True:
                hords.append(hords[i] - f(hords[i]) * (r1 - hords[i]) / (f(r1) - f(hords[i])))
                i += 1
                if abs(hords[i] - hords[i - 1]) <= e1 or abs(f(hords[i])) <= e1:
                    break
    if output == 'k':
        print("Найденный корень:", hords[-1])
        print("Значение функции в корне:", f(hords[-1]))
        print("Число итераций:", i)
    elif output == 'f':
        with open('output.txt', 'w') as file:
            file.write("Найденный корень: " + str(hords[-1]))
            file.write("\nЗначение функции в корне: " + str(f(hords[-1])))
            file.write("\nЧисло итераций: " + str(i))
    else:
        print('Неверно указан режим вывода. Для вывода на консоль нажмите k, для вывода в файл f')


def secants_method(l2, r2, e2, x1, output):
    secants = []

    if f(l2) * second_derivative(l2) > 0:
        secants.append(l2)
    else:
        secants.append(r2)
    secants.append(x1)
    i = 1
    while True:
        secants.append(secants[i] - f(secants[i]) * (secants[i] - secants[i - 1]) / (f(secants[i]) - f(secants[i - 1])))
        if abs(secants[i + 1] - secants[i]) <= e2 or abs(f(secants[i + 1])) <= e2:
            break
        i += 1
    if output == 'k':
        print("Найденный корень:", secants[-1])
        print("Значение функции в корне:", f(secants[-1]))
        print("Число итераций:", i)
    elif output == 'f':
        with open('output.txt', 'a') as file:
            file.write("\nНайденный корень: " + str(secants[-1]))
            file.write("\nЗначение функции в корне: " + str(f(secants[-1])))
            file.write("\nЧисло итераций: " + str(i))


def iterations_method(l3, r3, e3, output):
    iterations = []
    iterations.append((l3 + r3) / 2)
    i = 0
    if abs(derivative_fi1(l3)) < 1 and abs(derivative_fi1(r3)) < 1:
        print(1, abs(derivative_fi1(l3)), abs(derivative_fi1(r3)))
        while True:
            iterations.append(fi1(iterations[i]))
            i += 1
            if abs(iterations[i] - iterations[i - 1]) <= e3:
                break

    elif abs(derivative_fi2(l3)) < 1 and abs(derivative_fi2(r3)) < 1:
        print(2, abs(derivative_fi1(l3)), abs(derivative_fi1(r3)))
        while True:
            iterations.append(fi2(iterations[i]))
            i += 1
            if abs(iterations[i] - iterations[i - 1]) <= e3:
                break
    elif abs(derivative_fi3(l3)) < 1 and abs(derivative_fi3(r3)) < 1:
        print(3, abs(derivative_fi1(l3)), abs(derivative_fi1(r3)))
        while True:
            iterations.append(fi3(iterations[i]))
            i += 1
            if abs(iterations[i] - iterations[i - 1]) <= e3:
                break
    else:
        print(4, abs(derivative_fi1(l3)), abs(derivative_fi1(r3)))
        while True:

            iterations.append(fi4(iterations[i], l3, r3))
            i += 1
            if abs(iterations[i] - iterations[i - 1]) <= e3:
                break
    if output == 'k':
        print("Найденный корень:", iterations[-1])
        print("Значение функции в корне:", f(iterations[-1]))
        print("Число итераций:", i)
    elif output == 'f':
        with open('output.txt', 'a') as file:
            file.write("\nНайденный корень: " + str(iterations[-1]))
            file.write("\nЗначение функции в корне: " + str(f(iterations[-1])))
            file.write("\nЧисло итераций: " + str(i))


def draw_plot():
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


draw_plot()
inp = input('Вы желаете вводить с клавиатуры(k) или из файла(f)?\n')
out = input('Вы желаете выводить на консоль(k) или в файл(f)?\n')
if inp == 'k':
    print("Метод хорд для правого корня")
    l1 = float(input("Введите левую границу\n"))
    r1 = float(input("Введите правую границу\n"))
    e1 = float(input("Введите точность\n"))
    hords_method(l1, r1, e1, out)
    print("Метод секущих для левого корня")
    l2 = float(input("Введите левую границу\n"))
    r2 = float(input("Введите правую границу\n"))
    e2 = float(input("Введите точность\n"))
    x1 = float(input("Введите x1\n"))
    secants_method(l2, r2, e2, x1, out)
    print("Метод простых итераций для центрального корня")
    l3 = float(input("Введите левую границу\n"))
    r3 = float(input("Введите правую границу\n"))
    e3 = float(input("Введите точность\n"))
    iterations_method(l3, r3, e3, out)
elif inp == 'f':
    path = input('Введите путь до файла\n')
    try:
        with open(path, 'r') as file:
            l1, r1, e1 = map(float, file.readline().split())
            hords_method(l1, r1, e1, out)
            l2, r2, e2, x1 = map(float, file.readline().split())
            secants_method(l2, r2, e2, x1, out)
            l3, r3, e3 = map(float, file.readline().split())
            iterations_method(l3, r3, e3, out)
    except FileNotFoundError:
        print('Путь к файлу с входными данными указан неверно или такого файла не существует. Проверьте корректность '
              'введенных данных:', path)
else:
    print('Неверно указан режим ввода. Для ввода с клавиатуры нажмите k, для ввода из файла f')