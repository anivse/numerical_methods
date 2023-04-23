import matplotlib.pyplot as plt
import numpy as np
import math

def my_func(x):
    return (math.sin(x**2))**0.5

def func_values(func, xlist):
   return [func(x) for x in xlist]

def uniform_grid (xmin, xmax, count):
    h = (xmax-xmin)/(count-1)
    xlist = [0]*count
    i = 0
    while i < count:
        xlist[i] = xmin + h*i
        i += 1

    return xlist

def Simpson (func, a, b):
    return (b - a) / 6 * (func(a) + 4 * func((a + b) / 2) + func(b))

def Gauss3 (func, a, b):
    return (b - a) / 18 * (5 * func((a + b) / 2 - 0.6**0.5 * (b - a) / 2) + 8 * func((a + b) / 2) + 5 * func((a + b) / 2 + 0.6**0.5 * (b - a) / 2))

def number_of_iterations(eps ,func ,a , b, method):
    S2N = method(func, a, b)
    SN = method(func, a, a + (b-a)/2) + method(func, a + (b-a)/2, b)
    n = 2
    N = 4
    q = 15
    if(method == Gauss3):
        q = 31
    while (math.fabs(S2N-SN) / q > eps):
        h = (b-a) / N
        S2N = SN
        i = 0
        SN = 0
        while (i < N):
            SN += method(func, a + h*i, a + h*(i+1))
            i += 1
          #  print(i)
        N *= 2
        n += 1
        # if (eps == 10 ** (-15)):
           # print(SN)
        #print(N)

    return n

def epsilon(numberiter ,func ,a , b, method):
    S2N = method(func, a, b)
    SN = method(func, a, a + (b-a)/2) + method(func, a + (b-a)/2, b)
    n = 2
    N = 4
    eps = [0] * (numberiter-1)
    q = 15
    if (method == Gauss3):
        q = 31
    while (n <= numberiter):
        h = (b-a) / N
        S2N = SN
        i = 0
        SN = 0
        while (i < N):
            SN += method(func, a + h*i, a + h*(i+1))
            i += 1
           # print(i)
        eps[n - 2] = math.fabs(S2N-SN) / q
        N *= 2
        n += 1
        #print(N)

    return eps


a1 = -0.5
b1 = 0.01
a2 = 0.5
b2 = 1.01
power = range(-1, -16, -1)
result1 = [0] * 15
result2 = [0] * 15
result3 = [0] * 15
result4 = [0] * 15
eps = [0] * 15
i = 0

# while i < 15:
#     result1[i] = number_of_iterations(10**(power[i]), my_func, a1, b1, Gauss3)
#     result2[i] = number_of_iterations(10**(power[i]), my_func, a2, b2, Gauss3)
#     result3[i] = number_of_iterations(10 ** (power[i]), my_func, a1, b1, Simpson)
#     result4[i] = number_of_iterations(10 ** (power[i]), my_func, a2, b2, Simpson)
#     eps[i] = 10**(power[i])
#     i += 1
#
# fig1 = plt.figure()
# plt.semilogx(eps, result1, linewidth=0.5)
# plt.semilogx(eps, result2, linewidth=0.5)
# plt.semilogx(eps, result3, linewidth=0.5)
# plt.semilogx(eps, result4, linewidth=0.5)
# plt.xlabel('eps')
# plt.ylabel('Number of iterations')
# plt.title('Dependence of the number of iterations on the specified accuracy')
# plt.legend(['Gauss3[-0.01; 0.5]', 'Gauss3[0.5;1.01]','Simpson[-0.01; 0.5]', 'Simpson[0.5;1.01]' ], fontsize=5)
# plt.show()



error1 = epsilon(25, my_func, a1, b1, Gauss3)
error2 = epsilon(25, my_func, a2, b2, Gauss3)
error3 = epsilon(25, my_func, a1, b1, Simpson)
error4 = epsilon(25, my_func, a2, b2, Simpson)
numbersiter = range(2, 26)

fig2 = plt.figure()
plt.semilogy(numbersiter, error1, linewidth=0.5)
plt.semilogy(numbersiter, error2, linewidth=0.5)
plt.semilogy(numbersiter, error3, linewidth=0.5)
plt.semilogy(numbersiter, error4, linewidth=0.5)
plt.xlabel('Number of iteration')
plt.ylabel('eps')
plt.title('Convergence of the method')
plt.legend(['Gauss3[-0.01; 0.5]', 'Gauss3[0.5;1.01]','Simpson[-0.01; 0.5]', 'Simpson[0.5;1.01]'], fontsize=5)
plt.show()
