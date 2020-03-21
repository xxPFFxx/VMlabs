# f(x) : x^3−1.89x^2−2x+1.76=0
x2 = -1.15624  # (интервал изоляции: [-2;-1])
x3 = 0.629971  # (интервал изоляции: [0;1])
x1 = 2.41627  # (интервал изоляции: [2;3])


def f(x):
    # return x**3 - x + 4
    return x ** 3 - 1.89 * x ** 2 - 2 * x + 1.76


def second_derivative(x):
    # return 6 * x
    return 6 * x - 3.78


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
l1 = int(input("Введите левую границу\n"))
r1 = int(input("Введите правую границу\n"))
e1 = float(input("Введите точность\n"))
if l1 <= x1 <= r1:
    if f(l1) * second_derivative(l1) > 0:
        hords.append(r1)
        i = 0
        print(i, l1, r1, hords[i], f(l1), f(r1), f(hords[i]), '-')
        while True:
            hords.append(l1 - f(l1) * (hords[i] - l1) / (f(hords[i]) - f(l1)))
            i += 1
            print(i, l1, hords[i-1], hords[i], f(l1), f(hords[i-1]), f(hords[i]), abs(hords[i] - hords[i - 1]))
            if abs(hords[i] - hords[i - 1]) <= e1 or abs(f(hords[i])) <= e1:
                break
    else:
        hords.append(l1)
        i = 0
        print(i, l1, r1, hords[i], f(l1), f(r1), f(hords[i]), '-')
        while True:
            hords.append(hords[i] - f(hords[i]) * (r1 - hords[i]) / (f(r1) - f(hords[i])))
            i += 1
            print(i, hords[i-1], r1, hords[i], f(hords[i-1]), f(r1), f(hords[i]), abs(hords[i]-hords[i-1]))
            if abs(hords[i] - hords[i - 1]) <= e1 or abs(f(hords[i])) <= e1:
                break