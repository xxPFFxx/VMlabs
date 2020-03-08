def output_nev(a_start, b_start, x):
    print("Вектор невязок:")
    for i in range(len(x)):
        s = 0
        for j in range(len(x)):
            s += a_start[i][j] * x[j]
        print("r" + str(i + 1), "=", "{:.20f}".format(b_start[i] - s))


def output_x(x):
    for i in range(len(x)):
        print("x" + str(i + 1), "=", x[i])


def output_matrix(a, b):
    print("Треугольная матрица (включая преобразованный столбец B):")
    for i in range(len(a)):
        for j in range(len(a[i])):
            print("{:20f}".format(a[i][j]), end=" ") #{:20.2f}, если покрасивее вывод нужен
        print("|{:20f}".format(b[i]), end="")
        print()


def find_determinant(a, rev):
    det = 1
    for i in range(len(a)):
        det *= a[i][i]
    print("Было", rev, "перестановок")
    return det if rev % 2 == 0 else -det


def solve(a, b, n):
    a_start = a
    b_start = b
    rev = 0
    for i in range(n - 1):
        if a[i][i] == 0:
            out = False
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    out = True
                    break
            if not out:
                print("Система не имеет решений или имеет бесконечно много")
                return
        l = i
        for m in range(i + 1, n):
            if abs(a[m][i]) > abs(a[l][i]):
                l = m
        if l != i:
            for j in range(i, n):
                a[i][j], a[l][j] = a[l][j], a[i][j]
            rev += 1
            b[i], b[j] = b[j], b[i]
        for k in range(i + 1, n):
            c = a[k][i] / a[i][i]
            a[k][i] = 0
            for j in range(i + 1, n):
                a[k][j] -= c * a[i][j]
            b[k] -= c * b[i]
    x = []
    det = find_determinant(a, rev)
    if det == 0:
        print("Система не имеет решений или имеет бесконечно много")
        return
    for i in range(n - 1, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += a[i][j] * x[j - i - 1]  # При j=i+1 нам нужен x[0], j=i+2 x[1], поэтому x[j-i-1]
        x.insert(0, (b[i] - s) / a[i][i])  # Поскольку мы вычисляем переменные с конца, новое значение ставим в начало
    print("Определитель равен", det)
    output_matrix(a, b)
    output_x(x)
    output_nev(a_start, b_start, x)


cycle = 'c'
while cycle != 'q':
    a = []
    b = []
    fk = input("Вы желаете вводить с клавиатуры или из файла? k - с клавиатуры, f - из файла, q - выйти из программы\n")
    if fk == 'k':
        try:
            n = int(input("Введите размерность матрицы:\n"))
        except ValueError:
            print("n должно быть числом")
            continue
        print("Введите коэффициенты и свободные члены:")
        print("***Должно быть введено", n, "строк по", n + 1, "значений***")
        flag_not_n_elements_in_string_keyboard = False
        flag_elements_not_numbers_keyboard = False
        for i in range(n):
            s = input().split()
            if len(s) != n + 1:
                print("В каждой строке должно быть по", n + 1, "значений, вы ввели", len(s))
                flag_not_n_elements_in_string_keyboard = True
                break
            try:
                a.append([float(elem) for elem in s[:-1]])
                b.append(float(s[-1]))
            except ValueError:
                print("Все элементы должны быть числами")
                flag_elements_not_numbers_keyboard = True
                break
        if flag_not_n_elements_in_string_keyboard or flag_elements_not_numbers_keyboard:
            continue
        solve(a, b, n)
    elif fk == 'f':
        flag_not_n_elements_in_string_file = False
        flag_elements_not_numbers_file = False
        src = input("Введите абсолютный или относительный путь к файлу\n")
        try:
            with open(src) as file:
                try:
                    n = int(file.readline())
                except ValueError:
                    print("n должно быть числом")
                    continue
                for line in file:
                    s = line.split()
                    if len(s) != n + 1:
                        print("В каждой строке должно быть по", n + 1, "значений")
                        flag_not_n_elements_in_string_file = True
                        break
                    try:
                        a.append([float(elem) for elem in s[:-1]])
                        b.append(float(s[-1]))
                    except ValueError:
                        print("Все элементы должны быть числами")
                        flag_elements_not_numbers_file = True
                        break
            if flag_not_n_elements_in_string_file or flag_elements_not_numbers_file:
                continue
            solve(a, b, n)
        except FileNotFoundError:
            print("Неверный путь к файлу")
    elif fk == 'q':
        break
    else:
        print("Неверный ввод, введите f,k или q")
    cycle = input("Закончить программу или продолжить? q - выйти, c - продолжить\n")
