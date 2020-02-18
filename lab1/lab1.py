def output_x(x):
    for i in range(len(x)):
        print("x" + str(i + 1), "=", x[i])


def output_matrix(a, b):
    for i in range(len(a)):
        for elem in a[i]:
            print(elem, end='\t')
        print(b[i])


def find_determinant(a, rev):
    det = 1
    for i in range(len(a)):
        det *= a[i][i]
    return det if rev % 2 == 0 else -det


def solve(a, b, n):
    rev = 0
    for i in range(n - 1):
        if a[i][i] == 0:
            out = False
            for j in range(i + 1, n):
                if a[j][i] != 0:
                    a[i], a[j] = a[j], a[i]
                    b[i], b[j] = b[j], b[i]
                    break
            if out == False:
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
    output_x(x)
    output_matrix(a, b)


cycle = 'c'
while cycle != 'q':
    a = []
    b = []
    fk = input("Вы желаете вводить с клавиатуры или из файла? k - с клавиатуры, f - из файла\n")
    if fk == 'k':
        n = int(input("Введите размерность матрицы:\n"))
        print("Введите коэффициенты и свободные члены:")
        for i in range(n):
            s = input().split()
            a.append([int(elem) for elem in s[:-1]])
            b.append(int(s[-1]))
        solve(a, b, n)
    elif fk == 'f':
        src = input("Введите абсолютный или относительный путь к файлу\n")
        with open(src) as file:
            n = int(file.readline())
            for line in file:
                s = line.split()
                a.append([int(elem) for elem in s[:-1]])
                b.append(int(s[-1]))
        solve(a, b, n)
    else:
        print("Неверный ввод")
    cycle = input("Закончить программу или продолжить? q - выйти, c - продолжить\n")
