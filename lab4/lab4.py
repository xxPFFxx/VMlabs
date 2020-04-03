import matplotlib.pyplot as plt
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
    sxx += elem**2
sxy = 0
for i in range(n):
    sxy += x[i]*y[i]
a = (sxy*n - sx*sy)/(sxx*n - sx*sx)
b = (sxx*sy - sx*sxy)/(sxx*n - sx*sx)
# print(a,b)
# for i in range(n):
#     print(a*x[i]+b, a*x[i]+b-y[i])
# ylin = [a*x[i]+b for i in range(n)]
# plt.plot(x,ylin)
# plt.grid(True)
# plt.show()
s = 0
for i in range(n):
    s += (a*x[i]+b-y[i])**2
print(s)
