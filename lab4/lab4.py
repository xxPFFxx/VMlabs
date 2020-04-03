import matplotlib.pyplot as plt
from math import *

x = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5]
y = [2.46, 3.29, 4.23, 5.43, 6.98, 8.96, 11.51, 14.78, 18.95, 24.31, 31.25]
# plt.plot(x,y)
# plt.grid(True)
# plt.show()

n = len(x)
sx = sum(x)
sy = sum(y)
sxx = 0
for elem in x:
    sxx += elem ** 2
sxy = 0
for i in range(n):
    sxy += x[i] * y[i]
a = (sxy * n - sx * sy) / (sxx * n - sx * sx)
b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
# print(a,b)
# for i in range(n):
#     print(a*x[i]+b, a*x[i]+b-y[i])
ylin = [a*x[i]+b for i in range(n)]
# plt.plot(x,ylin)
# plt.grid(True)
# plt.show()
slin = 0
for i in range(n):
    slin += (ylin[i] - y[i]) ** 2
# print(slin)
from lab1 import lab1

sxxx = sum([elem ** 3 for elem in x])
sxxxx = sum([elem ** 4 for elem in x])
sxxy = sum([y[i] * x[i] ** 2 for i in range(n)])
a0, a1, a2 = lab1.solve([[n, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxxx]], [sy, sxy, sxxy], 3)
# for i in range(n):
#     print(a2*x[i]**2+a1*x[i]+a0, a2*x[i]**2+a1*x[i]+a0 - y[i])
ypol = [a2 * x[i] ** 2 + a1 * x[i] + a0 for i in range(n)]
# plt.plot(x,ypol)
# plt.grid(True)
# plt.show()
spol = 0
for i in range(n):
    spol += (ypol[i] - y[i]) ** 2
# print(spol)

sxy = sum([log(y[i]) * x[i] for i in range(n)])
sy = sum([log(y[i]) for i in range(n)])
a = exp((sxy * n - sx * sy) / (sxx * n - sx * sx))
b = (sxx * sy - sx * sxy) / (sxx * n - sx * sx)
# for i in range(n):
#     print(a*exp(b*x[i]), a*exp(b*x[i]) - y[i])
yexp = [a*exp(b*x[i]) for i in range(n)]
# plt.plot(x,yexp)
# plt.grid(True)
# plt.show()
sexp = 0
for i in range(n):
    sexp += (yexp[i] - y[i]) ** 2
# print(sexp)