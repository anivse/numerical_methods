import matplotlib.pyplot as plt
import numpy as np
import math
import sympy
from sympy import Symbol

def my_func(x):
    return (math.sin(x**2))**0.5

def func_values(func, xlist):
   return [func(x) for x in xlist]

#равномерная сетка
def uniform_grid (xmin, xmax, count):
    h = (xmax-xmin)/count
    x = xmin
    xlist = [0]*count
    i = 0
    while i < count:
        xlist[i] = xmin + h*i
        i += 1

    return xlist

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



counts = [0] * 4
counts[0] = 3
counts[1] = 5
counts[2] = 7
counts[3] = 10
xmin = -1.5
xmax = 1.5
count = 5
unilist = uniform_grid(xmin, xmax, 300)
cheblist = chebyshev_grid(xmin, xmax, 300)
xlist = uniform_grid(xmin, xmax, 300)
ylist = func_values(my_func, xlist)
result_uni_lagrange = [0]*300
result_cheb_lagrange = [0]*300
k = 0
f1 = plt.figure()
while True:
    count = counts[k]
    i = 0
    while i < 300:
        result_uni_lagrange[i] = uniform_grid_lagrange(xlist[i], xmin, xmax, count)
        i += 1
    plt.plot(xlist, result_uni_lagrange, linewidth=0.55, linestyle='--')
    k += 1
    if count == 10:
        break
plt.plot(xlist, ylist, linewidth=0.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph functions and Lagrange polynomials, uniform grid')
plt.legend(['n=3', 'n=5', 'n=7', 'n=10','graph func'], fontsize=5)
plt.show()


k = 0
f2 = plt.figure()
while True:
    count = counts[k]
    i = 0
    while i < 300:
        result_cheb_lagrange[i] = cheb_grid_lagrange(xlist[i], xmin, xmax, count)
        i += 1
    plt.plot(xlist, result_cheb_lagrange, linewidth=0.55, linestyle='--')
    k += 1
    if count == 10:
        break
plt.plot(xlist, ylist, linewidth=0.7)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph functions and Lagrange polynomials, chebyshev grid')
plt.legend(['n=3', 'n=5', 'n=7', 'n=10','graph func'], fontsize=5)
plt.show()


# xmin = -1.5
# xmax = 1.5
# count = 5
# unilist = uniform_grid(xmin, xmax, 300)
# cheblist = chebyshev_grid(xmin, xmax, 300)
#
# xlist = uniform_grid(xmin, xmax, 300)
# ylist = func_values(my_func, xlist)
#
# result_uni_lagrange = [0]*300
# result_cheb_lagrange = [0]*300
# i = 0
# while i < 300:
#     result_uni_lagrange[i] = uniform_grid_lagrange(xlist[i], xmin, xmax, count)
#     i += 1
#
# i = 0
# while i < 300:
#     #result_cheb_lagrange[i] = lagrange(cheblist[i], cheblist, cheb_ylist)
#     result_cheb_lagrange[i] = cheb_grid_lagrange(xlist[i], xmin, xmax, count)
#     i += 1
#
#
#
# fig1 = plt.figure()
# plt.plot(xlist, ylist, linewidth=0.4)
# plt.plot(xlist, result_uni_lagrange, linewidth=0.4, linestyle='--')
# #plt.plot(xlist, result_cheb_lagrange, linewidth=0.4, linestyle='--')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Graph functions and Lagrange polynomials, n=5')
# #plt.title('Graph functions ')
# plt.legend(['Graph functions', 'Uniform grid', 'Chebyshev grid'], fontsize=5)
# plt.show()


# xmin = 700**0.5*math.pi**0.5
# xmax = 701**0.5*math.pi**0.5
# step = 0.01
# error_uniform_list = [0] * int((xmax-xmin)/step+1)
# error_cheb_list = [0]*int((xmax-xmin)/step+1)
#
#
# error_uni = [0] * 100
# error_cheb = [0] * 100
# counts = list(range(1, 101))
#
# count = 1
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
#     error_uni[count - 1] = np.amax(error_uniform_list)
#     error_cheb[count - 1] = np.amax(error_cheb_list)
#
#     count += 1
#
# fig2 = plt.figure()
# plt.semilogy(counts, error_uni, linewidth=0.5)
# plt.semilogy(counts, error_cheb, linewidth=0.5)
# plt.xlabel('Number of grid splits')
# plt.ylabel('Max error')
# plt.title('Error in [sqrt(700pi);sqrt(701pi)]')
# plt.legend(['Uniform grid', 'Chebyshev grid'], fontsize=5)
# plt.show()
#
