import matplotlib.pyplot as plt
import numpy as np
import math

def my_func(x):
    return (math.sin(x**2))**0.5

def func_values(func, xlist):
   return [func(x) for x in xlist]

#равномерная сетка
def uniform_grid (xmin, xmax, count):
    h = (xmax-xmin)/(count-1)
    xlist = [0]*count
    i = 0
    while i < count:
        xlist[i] = xmin + h*i
        i += 1

    return xlist


# Структура, описывающая сплайн на каждом сегменте сетки
class Spline:
    def __init__(self, a, b, c, d, x):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.x = x


def spline(x, y, n):
    # Инициализация массива сплайнов
    splines = [Spline(0, 0, 0, 0, 0) for _ in range(0, n)]
    for i in range(0, n):
        splines[i].x = x[i]
        splines[i].a = y[i]

    splines[0].c = splines[n - 1].c = 0.0


    alpha = [0.0 for _ in range(0, n - 1)]
    beta = [0.0 for _ in range(0, n - 1)]

    for i in range(1, n - 1):
        hi = x[i] - x[i - 1]
        hi1 = x[i + 1] - x[i]
        A = hi
        C = 2.0 * (hi + hi1)
        B = hi1
        F = 6.0 * ((y[i + 1] - y[i]) / hi1 - (y[i] - y[i - 1]) / hi)
        z = (A * alpha[i - 1] + C)
        alpha[i] = -B / z
        beta[i] = (F - A * beta[i - 1]) / z

    for i in range(n - 2, 0, -1):
        splines[i].c = alpha[i] * splines[i + 1].c + beta[i]

    for i in range(n - 1, 0, -1):
        hi = x[i] - x[i - 1]
        splines[i].d = (splines[i].c - splines[i - 1].c) / hi
        splines[i].b = hi * (2.0 * splines[i].c + splines[i - 1].c) / 6.0 + (y[i] - y[i - 1]) / hi
    return splines


# Вычисление значения интерполированной функции в произвольной точке
def interpolate(splines, x):

    n = len(splines)
    s = Spline(0, 0, 0, 0, 0)

    if x <= splines[0].x:
        s = splines[0]
    elif x >= splines[n - 1].x:
        s = splines[n - 1]
    else:
        i = 0
        j = n - 1
        while i + 1 < j:
            k = i + (j - i) // 2
            if x <= splines[k].x:
                j = k
            else:
                i = k
        s = splines[j]

    dx = x - s.x
    return s.a + (s.b + (s.c / 2.0 + s.d * dx / 6.0) * dx) * dx;

xmin = -(math.pi/2)**0.5
xmax = (math.pi/2)**0.5
count = 3
xlist = uniform_grid(xmin, xmax, 300)
ylist = func_values(my_func, xlist)

x = uniform_grid(xmin, xmax, count)
y = func_values(my_func, x)

splines = spline(x, y, len(x))

xresult = uniform_grid(xmin, xmax, 300)
yresult = [0] * 300
i = 0
while i < 300:
    yresult[i] = interpolate(splines, xresult[i])
    i += 1

fig = plt.figure()
plt.plot(xlist, ylist, linewidth=0.5)
plt.plot(xresult, yresult, linewidth=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph function and natural cubic spline, n = 3')
plt.legend(['Graph function', 'Natural Cubic Spline'], fontsize=5)
plt.show()


# xmin = 700**0.5*math.pi**0.5
# xmax = 701**0.5*math.pi**0.5
# step = 0.01
# error_list = [0] * int((xmax-xmin)/step+1)
#
# error = [0] * 98
# counts = list(range(3, 101))
#
# count = 3
# while count <= 100:
#     i = 0
#     value = xmin
#
#     x = uniform_grid(xmin, xmax, count)
#     y = func_values(my_func, x)
#     splines = spline(x, y, count)
#
#     while value < xmax-0.01:
#         value = xmin + step * i
#         error_list[i] = math.fabs(my_func(value) - interpolate(splines, value))
#         i += 1
#         print('s')
#
#     error[count - 3] = np.amax(error_list)
#     count += 1

fig2 = plt.figure()
#plt.semilogy(counts, error, linewidth=0.5)
# plt.xlabel('Number of grid splits')
# plt.ylabel('Max error')
# plt.title('Error in [sqrt(700pi);sqrt(701pi)]')
# plt.legend(['Uniform grid', 'Chebyshev grid'], fontsize=5)
#plt.show()








#сетка Чебышева
def chebyshev_grid (xmin, xmax, count):
    cheblist = [0]*count
    i = 0
    while i < count:
        cheblist[i] = math.cos(math.pi*(2*i+1)/(2*count))
        i += 1

    i = 0

    while i < count:
        cheblist[i] = (xmax-xmin) * cheblist[i]/2 + (xmin+xmax)/2
        i += 1
    return cheblist



#полином Лагранжа
def lagrange(x, xlist, ylist):
    degree = len(xlist)-1
    polynom = 0
    i = 0
    basics = 0
    while i <= degree:
        basics = 1
        j = 0
        while j <= degree:
            if i != j:
                basics = basics*(x-xlist[j])/(xlist[j]-xlist[i])
            j += 1
        polynom = polynom + basics * ylist[i]
        i += 1
    return polynom


def uniform_grid_lagrange(x, xmin, xmax, count):
    degree = count - 1
    polynom = 0
    i = 0
    basics = 1
    h = (xmax - xmin) / count
    while i <= count:
        basics = 1
        j = 0
        while j <= count:
            if i != j:
                basics = basics * (x - (xmin + h*j)) / ((xmin+h*i) - (xmin+h*j))
            j += 1
        y = my_func(xmin+h*i)
        polynom = polynom + basics * y
        i += 1
    return polynom

def cheb_grid_lagrange(x, xmin, xmax, count):
    degree = count - 1
    polynom = 0
    i = 0
    basics = 1
    h = (xmax - xmin) / count
    while i <= count:
        basics = 1
        j = 0
        while j <= count:
            if i != j:
                basics = basics * (x - ((xmin+xmax)/2 + (xmax-xmin)/2 * math.cos((2*j+1)*math.pi/(2*(count+1))))) / ((xmin + xmax) / 2 + (xmax - xmin) / 2 * math.cos((2 * i + 1) * math.pi / (2 * (count + 1))) - ((xmin + xmax) / 2 + (xmax - xmin) / 2 * math.cos((2 * j + 1) * math.pi / (2 * (count + 1)))))
            j += 1
        y = my_func((xmax + xmin) / 2 + (xmax - xmin) / 2 * math.cos((2 * i + 1) * math.pi / (2 * (count + 1))))
        polynom = polynom + basics * y
        i += 1
    return polynom



# xmin = 700**0.5*math.pi**0.5
# xmax = 701**0.5*math.pi**0.5
# step = 0.01
# error_uniform_list = [0] * int((xmax-xmin)/step+1)
# error_cheb_list = [0]*int((xmax-xmin)/step+1)
#
#
# error_uni = [0] * 98
# error_cheb = [0] * 98
# counts = list(range(3, 101))
#
# count = 3
# while count <= 100:
#     i = 0
#     value = xmin
#
#     while value < xmax-0.01:
#         value = xmin + step * i
#         error_uniform_list[i] = math.fabs(my_func(value) - uniform_grid_lagrange(value, xmin, xmax, count))
#         i += 1
#         print('u')
#
#     j = 0
#     value = xmin
#     while value < xmax-0.01:
#         value = xmin + step * j
#         error_cheb_list[j] = math.fabs(my_func(value) - cheb_grid_lagrange(value, xmin, xmax, count))
#         j += 1
#         print('c')
#
#     error_uni[count - 3] = np.amax(error_uniform_list)
#     error_cheb[count - 3] = np.amax(error_cheb_list)
#
#     count += 1

# plt.semilogy(counts, error, linewidth=0.5)
# plt.semilogy(counts, error_uni, linewidth=0.5)
# plt.semilogy(counts, error_cheb, linewidth=0.5)
# plt.xlabel('Number of grid splits')
# plt.ylabel('Max error')
# plt.title('Error in [sqrt(700pi);sqrt(701pi)]')
# plt.legend(['Natural cubic splines', 'Uniform grid', 'Chebyshev grid'], fontsize=5)
# plt.show()

