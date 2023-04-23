import matplotlib.pyplot as plt
import numpy as np
import math

def p(x):
    return x * (2 * x + 1)

def q(x):
    return (2 * x + 2)

def r(x):
    return -1

def f(x):
    return 1 / x

def answer(x):
    return 1 / x
x0 = 0.2
y0 = 5
xn = 1
yn = 1

def FiniteDifferenceMethod(p, q, r, f, x0, y0, xn, yn, N):
    h = (xn - x0) / N
    X = [0] * (N + 1)
    i = 0
    while i < (N+1):
       X[i] = x0 + h * i
       if(i!=0 and i!=N):
          print (p(X[i]), q(X[i]), r(X[i]), f(X[i]))
       i += 1


    B = [0] * (N - 1) # диагональ над главной
    C = [0] * (N - 1) # главная диагональ
    A = [0] * (N - 1) # диагональ под главной

    print(N)

    A[0] = 0
    B[N - 2] = 0

    F = [0] * (N - 1)
    Y = [0] * (N + 1)
    Y[0] = y0
    Y[N] = yn
#коэффициенты СЛАУ
    i = 0
    while (i < N - 1):
        if (i != 0 and i != N - 2):
            F[i] = h ** 2 * f(X[i + 1])
            C[i] = (h ** 2 * r(X[i + 1]) - 2 * p(X[i + 1]))
            A[i] = (p(X[i + 1]) - q(X[i + 1]) * h / 2)
            B[i] = (p(X[i + 1]) + q(X[i + 1]) * h / 2)
        if (i == 0):
            F[i] = h ** 2 * f(X[i + 1]) - (p(X[i + 1]) - q(X[i + 1]) * h / 2) * y0
            C[i] = (h ** 2 * r(X[i + 1]) - 2 * p(X[i + 1]))
            B[i] = (p(X[i + 1]) + q(X[i + 1]) * h / 2)
        if (i == N-2):
            F[i] = h ** 2 * f(X[i + 1]) - (p(X[i + 1]) + q(X[i + 1]) * h / 2) * yn
            C[i] = (h ** 2 * r(X[i + 1]) - 2 * p(X[i + 1]))
            A[i] = (p(X[i + 1]) - q(X[i + 1]) * h / 2)

        i += 1
        #print(i)

# метод прогонки

    A, B, C, F = tuple(map(lambda k_list: list(map(float, k_list)), (A, B, C, F)))

    print(A, B, C, F)

    alpha = [-B[0] / C[0]]
    beta = [F[0] / C[0]]
    n = len(F)
    x = [0] * n

    for i in range(1, n):
        alpha.append(-B[i] / (A[i] * alpha[i - 1] + C[i]))
        beta.append((F[i] - A[i] * beta[i - 1]) / (A[i] * alpha[i - 1] + C[i]))

    x[n - 1] = beta[n - 1]

    for i in range(n - 1, 0, -1):
        x[i - 1] = alpha[i - 1] * x[i] + beta[i - 1]

    print(x)

    j = 1
    while j < N:
        Y[j] = x[j - 1]
        j += 1

    return Y

#равномерная сетка
def uniform_grid (xmin, xmax, count):
    h = (xmax-xmin)/(count)
    xlist = [0]*(count+1)
    i = 0
    while i <= count:
        xlist[i] = xmin + h*i
        i += 1

    return xlist

def func_values(func, xlist):
   return [func(x) for x in xlist]

def iterations(eps , p, q, r, f, x0, y0, xn, yn):
    S2N = FiniteDifferenceMethod(p, q, r, f, x0, y0, xn, yn, 2)
    SN = FiniteDifferenceMethod(p, q, r, f, x0, y0, xn, yn, 4)
    h = (xn - x0) / 4
    n = 2
    N = 4
    while (math.fabs(S2N[int(N/4)] - SN[int(N/2)]) / 3 > eps):
        N *= 2
        S2N = SN
        SN = FiniteDifferenceMethod(p, q, r, f, x0, y0, xn, yn, N)
        h = (xn - x0) / N
        n += 1

    print(SN[int(N/2)])
    return n, h, SN[int(N/2)]

result = FiniteDifferenceMethod(p, q, r, f, x0, y0, xn, yn, 10)


x = uniform_grid(x0, xn, 10)
y = func_values(answer, x)

fig = plt.figure()
plt.plot(x, y, linewidth=0.5)
plt.plot(x, result, linewidth=0.5)
plt.show()


# power = range(-1, -9, -1)
# result_iter = [0] * 8
# result_h = [0] * 8
# result_error = [0] * 8
# eps = [0] * 8
# i = 0
# while i < 8:
#     result = iterations(10**(power[i]), p, q, r, f, x0, y0, xn, yn)
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
# error = 0
# data_error = [0] * 25
# result_error = [0] * 25
# j = 0
# while j < 25:
#     result_error[i] = 5 / 3 - iterations(10**(-8), p, q, r, f, x0, y0, xn, yn - error)[2]
#     data_error[i] = error
#     j += 1
#     error += 0.01
#
# fig3 = plt.figure()
# plt.plot(data_error, result_error, linewidth=0.5)
# plt.xlabel('Relative error of input data')
# plt.ylabel('Relative error of result')
# plt.title('Method stability')
# plt.show()

N = 4000 #h=(1-0.2)/4000=0.0002
Y = FiniteDifferenceMethod(p, q, r, f, x0, y0, xn, yn, N)
X = uniform_grid(x0, xn, N)

Answer = func_values(answer, X)

Error = list(np.array(Answer) - np.array(Y))

i = 0
while (i < 4000):
    Error[i] = math.fabs(Error[i])
    i += 1
print(Error)

fig4 = plt.figure()
plt.grid()
plt.semilogy(X, Error, linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Absolute Error')
plt.title('h = 0.0002')
plt.show()