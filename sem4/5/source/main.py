import matplotlib.pyplot as plt
import numpy as np
import math


xx = 1

def my_ddfunc(x, u, v):
    return (- (2 * x + 2) * v * x + u * x + 1) / (x**2 * (2 * x + 1))

def prelest(x, u, v):
    k1 = -0.11;
    k2 = 0.1;
    A = 3;
    if x >= 0:
        F1 = 1
    else:
        F1 = -1
    T = 0.1
    if (x - T) >= 0:
        F2 = 1
    else:
        F2 = -1
    return -k1 * v - k2 * u + A * (F1 - F2)

def answer(x):
    return 1/x

def EulerCauchy(xmin, xmax, N, ddfunc, umin, vmin):
    h = (xmax - xmin) / N
    xlist = [0] * (N + 1)
    i = 0
    while i < (N+1):
        xlist[i] = xmin + h * i
        i += 1
    upred = [0] * (N + 1)
    vpred = [0] * (N + 1)
    u = [0] * (N + 1)
    v = [0] * (N + 1)

    upred[0] = umin
    vpred[0] = vmin
    u[0] = umin
    v[0] = vmin
    i = 1
    j = 1
    while (i < (N + 1)):
        upred[i] = u[i - 1] + h * v[i - 1]
        vpred[i] = v[i - 1] + h * ddfunc(xlist[i - 1], u[i - 1], v[i - 1])
        u[j] = u[j - 1] + h / 2 * (v[j - 1] + vpred[j])
        v[j] = v[j - 1] + h / 2 * (ddfunc(xlist[j - 1], u[j - 1], v[j - 1]) + ddfunc(xlist[j], upred[j], vpred[j]))
        i += 1
        j += 1

    # j = 1
    #
    # while (j < (N + 1)):
    #     u[j] = u[j - 1] + h / 2 * (v[j - 1] + vpred[j])
    #     v[j] = v[j - 1] + h / 2 * (ddfunc(xlist[j - 1], u[j - 1], v[j - 1]) + ddfunc(xlist[j], upred[j], vpred[j]))
    #     j += 1

    return u

def iterations(eps , xmin, xmax,ddfunc, umin, vmin):
    S2N = EulerCauchy(xmin, xmax, 1, ddfunc, umin, vmin)
    SN = EulerCauchy(xmin, xmax, 2, ddfunc, umin, vmin)
    h = (xmax - xmin) / 2
    n = 2
    N = 2
    while (math.fabs(S2N[int(N/2)] - SN[N]) / 3 > eps):
        N *= 2
        S2N = SN
        SN = EulerCauchy(xmin, xmax, N, ddfunc, umin, vmin)
        h = (xmax - xmin) / N
        n += 1
        print("+")

    print(SN[N])
    return n, h, math.fabs(xx-SN[N])/xx, SN


xmin = 0.0
xmax = 50.0
umin = 0
vmin = 1000
eps = 10**(-3)
result = iterations(eps, xmin, xmax, prelest, umin, vmin)
print(result[3])
n = len(result[3])
step = (xmax - xmin)/n
X = [0] * n
i = 0
print(n)
while i < n:
    X[i] = xmin + step * i
    i += 1

fig1 = plt.figure()
plt.plot(X, result[3], linewidth=0.5)
plt.show()

# xmin = 0.2
# xmax = 1.0
# umin = 5
# vmin = -25
# power = range(-1, -11, -1)
# result_iter = [0] * 10
# result_h = [0] * 10
# result_error = [0] * 10
# eps = [0] * 10
# i = 0
# while i < 10:
#     result = iterations(10**(power[i]), xmin, xmax, my_ddfunc, umin, vmin)
#     result_iter[i] = result[0]
#     result_h[i] = result[1]
#     eps[i] = 10**(power[i])
#     i += 1
#
# fig1 = plt.figure()
# plt.semilogx(eps, result_iter, linewidth=0.5)
# plt.ylabel('Number of iteration')
# plt.xlabel('eps')
# plt.title('Convergence of the method')
# plt.show()
# fig2 = plt.figure()
# plt.loglog(result_h, eps, linewidth=0.5)
# plt.xlabel('h')
# plt.ylabel('eps')
# plt.title('Step dependence on eps')
# plt.show()
#
#
#
# data_error = [0] * 25
# result_error = [0] * 25
# j = 0
# while j < 25:
#     result_error[i] = iterations(10 ** (-8), xmin, xmax, my_ddfunc, umin, vmin)[2]
#     data_error[i] = (25 + vmin) / 25
#     j += 1
#     vmin += 0.02
#
# fig3 = plt.figure()
# plt.plot(data_error, result_error, linewidth=0.5)
# plt.xlabel('Relative error of input data')
# plt.ylabel('Relative error of result')
# plt.title('Method stability')
# plt.show()



# def testfunc(x,y):
#     return (2*x*y+3)/(x**2)
#
#
# def EulerCauchy(xmin, xmax, N, umin):
#     h = (xmax - xmin) / N
#     xlist = [0] * (N + 1)
#     i = 0
#     while i < (N+1):
#         xlist[i] = xmin + h * i
#         i += 1
#     upred = [0] * (N + 1)
#     u = [0] * (N + 1)
#     upred[0] = umin
#     u[0] = umin
#     i = 1
#     print("New Itreation")
#     print(N)
#     while (i < (N + 1)):
#         upred[i] = u[i - 1] + h * testfunc(xlist[i-1], u[i-1])
#         u[i] = u[i - 1] + h / 2 * (testfunc(xlist[i - 1], u[i - 1]) + testfunc(xlist[i], upred[i]))
#         print(upred[i])
#         print(u[i])
#         i += 1
#
#     j = 1
#
#
#     return u
#
# def iterations(eps , xmin, xmax, umin):
#     S2N = EulerCauchy(xmin, xmax, 1,  umin )
#     SN = EulerCauchy(xmin, xmax, 2,  umin)
#     h = (xmax - xmin) / 2
#     n = 2
#     N = 2
#     while (math.fabs(S2N[int(N/2)] - SN[N]) / 3 > eps):
#         N *= 2
#         S2N = SN
#         SN = EulerCauchy(xmin, xmax, N, umin)
#         h = (xmax - xmin) / N
#         n += 1
#
#     return  SN[N]
#
# eps=10**(-2)
# xmin = 1
# xmax = 2
# umin = -1
# n = iterations(eps, xmin, xmax, umin)
