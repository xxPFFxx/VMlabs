def linear_interpolation(massx, massy, x):
    for i in range(1, len(massx)):
        if massx[i-1] <= x <= massx[i]:
            a = (massy[i]-massy[i-1])/(massx[i]-massx[i-1])
            b = massy[i-1] - a*massx[i-1]
            return a*x + b


inp = input("Вы желаете вводить с клавиатуры(k) или из файла(f)?\n")
if inp == 'k':
    pass
elif inp == 'f':
    path = input("Введите путь до файла с исходными данными:\n")
    with open (path, 'r') as f:
        table4_x = list(map(float, f.readline().split()))
        table4_y = list(map(float, f.readline().split()))
        x1, x4 = map(float, f.readline().split())
        table8_x = list(map(float, f.readline().split()))
        table8_y = list(map(float, f.readline().split()))
        x2, x3 = map(float, f.readline().split())
        print('Линейная интерполяция:', linear_interpolation(table4_x,table4_y,x1))
else:
    print("Неверный ввод. Для ввода с клавиаутуры выберите k, для ввода из файла f.")