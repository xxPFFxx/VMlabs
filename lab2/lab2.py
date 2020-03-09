# Метод правых прямоугольников
def rectangle_right(number, lower, higher, n):
    h = (higher - lower) / n
    s = 0
    x = lower + h
    for i in range(n):
        s += f(number, x)
        x += h
    return h * s


# Метод левых прямоугольников
def rectangle_left(number, lower, higher, n):
    h = (higher - lower) / n
    s = 0
    x = lower
    for i in range(n):
        s += f(number, x)
        x += h
    return h * s


# Метод средних прямоугольников
def rectangle_mid(number, lower, higher, n):
    h = (higher - lower) / n
    s = 0
    x = lower + h / 2
    for i in range(n):
        s += f(number, x)
        x += h
    return h * s


def find_n_left(number, lower, higher, n, accuracy):
    h = (higher - lower) / n
    i0 = rectangle_left(number, lower, h, n)
    for i in range(12):
        n *= 2
        i1 = rectangle_left(number, lower, h, n)
        if abs(i1 - i0) <= accuracy:
            print("Значение методом левых прямоугольников:", i1)
            print("Число разбиений для достижения заданной точности:", n)
            return
        i0 = i1
    return -1


def find_n_right(number, lower, higher, n, accuracy):
    h = (higher - lower) / n
    i0 = rectangle_right(number, lower, h, n)
    for i in range(12):
        n *= 2
        i1 = rectangle_right(number, lower, h, n)
        if abs(i1 - i0) <= accuracy:
            print("Значение методом правых прямоугольников:", i1)
            print("Число разбиений для достижения заданной точности:", n)
            return
        i0 = i1
    return -1


def find_n_mid(number, lower, higher, n, accuracy):
    h = (higher - lower) / n
    i0 = rectangle_mid(number, lower, h, n)
    for i in range(12):
        n *= 2
        i1 = rectangle_mid(number, lower, h, n)
        if 1/3*abs(i1 - i0) <= accuracy:
            print("Значение методом средних прямоугольников:", i1)
            print("Число разбиений для достижения заданной точности:", n)
            return
        i0 = i1
    return -1


def f(number, x):
    if number == 1:
        return 2 * x ** 3 + 3
    elif number == 2:
        return 3 * x ** 4 - 4 * x ** 3 + 2 * x ** 2
    elif number == 3:
        return 7 * x ** 2 - 5 * x + 2
    elif number == 4:
        return 5 * x ** 5 - 9 * x ** 3 + 8 * x


def solve(number, lower, higher, accuracy):
    n = 4
    new_n_left = find_n_left(number, lower, higher, n, accuracy)
    if new_n_left == -1:
        print("Заданная точность не достигнута (метод левых прямоугольников)")
    new_n_right = find_n_right(number, lower, higher, n, accuracy)
    if new_n_right == -1:
        print("Заданная точность не достигнута (метод правых прямоугольников)")
    new_n_mid = find_n_mid(number, lower, higher, n, accuracy)
    if new_n_mid == -1:
        print("Заданная точность не достигнута")


functions = ['y=2x^3+3', 'y=3x^4-4x^3+2x^2', 'y=7x^2-5x+2', 'y=5x^5-9x^3+8x']
for i in range(len(functions)):
    print(str(i + 1) + ".", functions[i])
number = int(input("Выберите номер функции (1-4):\n"))
lower = int(input("Введите нижний предел:\n"))
higher = int(input("Введите верхний предел:\n"))
accuracy = float(input("Введите точность:\n"))
solve(number, lower, higher, accuracy)
