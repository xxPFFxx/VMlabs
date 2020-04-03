import matplotlib.pyplot as plt
from math import *
from lab1 import lab1


def sko(fi, y):
    res = 0
    for i in range(len(fi)):
        res += (fi[i] - y[i]) ** 2
    return sqrt(res/n)

x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
y = [2.46, 3.29, 4.23, 5.43, 6.98, 8.96, 11.51, 14.78, 18.95, 24.31, 31.25]
plt.plot(x,y)
plt.grid(True)
# plt.show()

# Линейная функция
n = len(x)
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
plt.plot(x,ylin)
plt.grid(True)
# plt.show()
slin = 0
for i in range(n):
    slin += (ylin[i] - y[i]) ** 2
# print(slin)
print(sko(ylin,y))

# Квадратичная функция
sxxx = sum([elem ** 3 for elem in x])
sxxxx = sum([elem ** 4 for elem in x])
sxxy = sum([y[i] * x[i] ** 2 for i in range(n)])
a0, a1, a2 = lab1.solve([[n, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]], [sy, sxy, sxxy], 3)
# for i in range(n):
#     print(a2*x[i]**2+a1*x[i]+a0, a2*x[i]**2+a1*x[i]+a0 - y[i])
ypol = [a2 * x[i] ** 2 + a1 * x[i] + a0 for i in range(n)]
plt.plot(x,ypol)
plt.grid(True)
# plt.show()
spol = 0
for i in range(n):
    spol += (ypol[i] - y[i]) ** 2
# print(spol)
print(sko(ypol,y))

# Экспоненциальная функция
sxy = sum([log(y[i]) * x[i] for i in range(n)])
sy = sum([log(y[i]) for i in range(n)])
a = exp((sxy * n - sx * sy) / (sxx * n - sx * sx))
b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
# for i in range(n):
#     print(a*exp(b*x[i]), a*exp(b*x[i]) - y[i])
yexp = [a * exp(b * x[i]) for i in range(n)]
plt.plot(x,yexp)
plt.grid(True)
# plt.show()
sexp = 0
for i in range(n):
    sexp += (yexp[i] - y[i]) ** 2
# print(sexp)
print(sko(yexp,y))

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
print(sko(ylog,y))

# Степенная функция
sx = sum([log(elem) for elem in x])
sy = sum([log(elem) for elem in y])
sxx = sum([(log(elem)) ** 2 for elem in x])
sxy = sum([log(y[i]) * log(x[i]) for i in range(n)])
a = exp((sxy * n - sx * sy) / (sxx * n - sx * sx))
b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
#for i in range(n):
#    print(a*x[i]**b, a*x[i]**b - y[i])
ystep = [a*x[i]**b for i in range(n)]
plt.plot(x,ystep)
plt.grid(True)
#plt.show()
sstep = 0
for i in range(n):
    sstep += (ystep[i] - y[i]) ** 2
#print(sstep)
print(sko(ystep,y))