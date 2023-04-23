import matplotlib.pyplot as plt
import numpy as np
import math

#
# xx = 1
#
# def my_ddfunc(x, u, v):
#     return (- (2 * x + 2) * v * x + u * x + 1) / (x**2 * (2 * x + 1))
#
# def answer(x):
#     return 1/x
#
# def EulerCauchy(xmin, xmax, N, ddfunc, umin, vmin):
#     h = (xmax - xmin) / N
#     xlist = [0] * (N + 1)
#     i = 0
#     while i < (N+1):
#         xlist[i] = xmin + h * i
#         i += 1
#     upred = [0] * (N + 1)
#     vpred = [0] * (N + 1)
#     u = [0] * (N + 1)
#     v = [0] * (N + 1)
#
#     upred[0] = umin
#     vpred[0] = vmin
#     u[0] = umin
#     v[0] = vmin
#     i = 1
#     j = 1
#     while (i < (N + 1)):
#         upred[i] = u[i - 1] + h * v[i - 1]
#         vpred[i] = v[i - 1] + h * ddfunc(xlist[i - 1], u[i - 1], v[i - 1])
#         u[j] = u[j - 1] + h / 2 * (v[j - 1] + vpred[j])
#         v[j] = v[j - 1] + h / 2 * (ddfunc(xlist[j - 1], u[j - 1], v[j - 1]) + ddfunc(xlist[j], upred[j], vpred[j]))
#         i += 1
#         j += 1
#
#     return u
#
#
# def Adams(xmin, xmax, N, ddfunc, umin, vmin):
#     h = (xmax - xmin) / N
#     xlist = [0] * (N + 1)
#     i = 0
#     while i < (N+1):
#         xlist[i] = xmin + h * i
#         i += 1
#
#     upred = [0] * (N + 1)
#     vpred = [0] * (N + 1)
#     u = [0] * (N + 1)
#     v = [0] * (N + 1)
#
#     upred[0] = umin
#     vpred[0] = vmin
#     u[0] = umin
#     v[0] = vmin
#
#     i = 1
#     while (i < (N + 1)):
#         #eulercauchy#
#
#         upred[i] = u[i - 1] + h / 1 * v[i - 1]
#         vpred[i] = v[i - 1] + h / 1 * ddfunc(xlist[i - 1], u[i - 1], v[i - 1])
#         u[i] = u[i - 1] + h / 2 * (v[i - 1] + vpred[i])
#         v[i] = v[i - 1] + h / 2 * (ddfunc(xlist[i - 1], u[i - 1], v[i - 1]) + ddfunc(xlist[i], upred[i], vpred[i]))
#
#
#         if (N > 1):
#             # adams#
#
#             upred[i + 1] = u[i] + h / 2 * (3 * v[i] - v[i - 1])
#             vpred[i + 1] = v[i] + h / 2 * (3 * ddfunc(xlist[i], u[i], v[i]) - ddfunc(xlist[i - 1], u[i - 1], v[i - 1]))
#             u[i + 1] = u[i] + h / 2 * (v[i] + vpred[i + 1])
#             v[i + 1] = v[i] + h / 2 * (ddfunc(xlist[i], u[i], v[i]) + ddfunc(xlist[i + 1], upred[i + 1], vpred[i + 1]))
#
#
#         i += 2
#
#     return u
#
# def iterations(eps , xmin, xmax,ddfunc, umin, vmin, method):
#     S2N = method(xmin, xmax, 1, ddfunc, umin, vmin)
#     SN = method(xmin, xmax, 2, ddfunc, umin, vmin)
#     h = (xmax - xmin) / 2
#     n = 2
#     N = 2
#     while (math.fabs(S2N[int(N/2)] - SN[N]) / 3 > eps):
#         N *= 2
#         S2N = SN
#         SN = method(xmin, xmax, N, ddfunc, umin, vmin)
#         h = (xmax - xmin) / N
#         n += 1
#
#     print(SN[N])
#     return n, h, math.fabs(xx-SN[N])/xx
#
#
# xmin = 0.2
# xmax = 1.0
# umin = 5
# vmin = -25
# power = range(-1, -11, -1)
# result_iter_euler = [0] * 10
# result_h_euler = [0] * 10
# result_iter_adams = [0] * 10
# result_h_adams = [0] * 10
# eps = [0] * 10
# i = 0
# # while i < 10:
# #     result_euler = iterations(10**(power[i]), xmin, xmax, my_ddfunc, umin, vmin, EulerCauchy)
# #     result_adams = iterations(10 ** (power[i]), xmin, xmax, my_ddfunc, umin, vmin, Adams)
# #     result_iter_euler[i] = result_euler[0]
# #     result_h_euler[i] = result_euler[1]
# #     result_iter_adams[i] = result_adams[0]
# #     result_h_adams[i] = result_adams[1]
# #     eps[i] = 10**(power[i])
# #     i += 1
# #
# # fig1 = plt.figure()
# # plt.semilogx(eps, result_iter_euler, linewidth=0.5)
# # plt.semilogx(eps, result_iter_adams, linewidth=0.5)
# # plt.ylabel('Number of iteration')
# # plt.xlabel('eps')
# # plt.legend(['EulerCauchy', 'Adams'])
# # plt.title('Convergence of the method')
# # plt.show()
# # fig2 = plt.figure()
# # plt.loglog(result_h_euler, eps, linewidth=0.5)
# # plt.loglog(result_h_adams, eps, linewidth=0.5)
# # plt.xlabel('h')
# # plt.ylabel('eps')
# # plt.legend(['EulerCauchy', 'Adams'])
# # plt.title('Step dependence on eps')
# # plt.show()
#
#
#
# data_error = [0] * 25
# result_error = [0] * 25
# j = 0
# while j < 25:
#     result_error[j] = iterations(10 ** (-8), xmin, xmax, my_ddfunc, umin, vmin, Adams)[2]
#     data_error[j] = (- 25 - vmin) / 25
#     j += 1
#     vmin -= 0.02
#
# # data_error = [0.000000000000000000000, 0.000799999999999982, 0.00159999999999996, 0.00239999999999994, 0.003199999999999931, 0.003999999999999915, 0.004799999999999898, 0.005599999999999889, 0.006399999999999863, 0.00719999999999984, 0.00799999999999983, 0.008799999999999813, 0.00959999999999979, 0.01039999999999977, 0.01119999999999976, 0.011999999999999744, 0.01279999999999972, 0.01359999999999971, 0.01439999999999969, 0.01519999999999967, 0.01599999999999966, 0.01679999999999964, 0.017599999999999626, 0.018399999999999608, 0.0191999999999995]
# # result_error = [6.087814918842582e-09, 0.001563272968032717, 0.00212655202378132, 0.00368983107971522, 0.004253110135615924, 0.005816389191440134, 0.005937966824724236, 0.006794294730310321, 0.007550622635897449, 0.00806950541477328, 0.00893278447067698, 0.009719606352656791, 0.01475934258233284, 0.01932262163822033, 0.03388590069411726, 0.038944917974994802, 0.04101245880578289, 0.04575757378616548, 0.04913901691744974, 0.05270229597335888, 0.05526557502916033, 0.05982885408500685, 0.062439213314093409, 0.06995541219676408, 0.07451869125260061]
#
# fig3 = plt.figure()
# plt.plot(data_error, result_error, linewidth=0.5)
# plt.xlabel('Relative error of input data')
# plt.ylabel('Relative error of result')
# plt.title('Method stability')
# plt.show()





def testfunc(x,y):
    return (2*x*y+3)/(x**2)


def Adams(xmin, xmax, N, umin):
    h = (xmax - xmin) / N
    xlist = [0] * (N + 1)
    i = 0
    while i < (N+1):
        xlist[i] = xmin + h * i
        i += 1
    upred = [0] * (N + 1)
    u = [0] * (N + 1)
    upred[0] = umin
    u[0] = umin
    i = 1
    print("New Itreation")
    print(N)
    while (i < (N + 1)):
        upred[i] = u[i - 1] + h * testfunc(xlist[i-1], u[i-1])
        u[i] = u[i - 1] + h / 2 * (testfunc(xlist[i - 1], u[i - 1]) + testfunc(xlist[i], upred[i]))

        if (N > 1):
        # adams #
           upred[i + 1] = u[i] + h / 2 * (3 * testfunc(xlist[i], u[i]) - testfunc(xlist[i - 1], u[i - 1]))
           u[i + 1] = u[i] + h / 2 * (testfunc(xlist[i + 1], upred[i + 1]) + testfunc(xlist[i], u[i]))

        print(upred[i])
        print(u[i])
        if (N > 1):
           print(upred[i + 1])
           print(u[i + 1])
        i += 2


    return u

def iterations(eps , xmin, xmax, umin):
    S2N = Adams(xmin, xmax, 1,  umin )
    SN = Adams(xmin, xmax, 2,  umin)
    h = (xmax - xmin) / 2
    n = 2
    N = 2
    while (math.fabs(S2N[int(N/2)] - SN[N]) / 3 > eps):
        N *= 2
        S2N = SN
        SN = Adams(xmin, xmax, N, umin)
        h = (xmax - xmin) / N
        n += 1

    return  SN[N]

eps=10**(-2)
xmin = 1
xmax = 2
umin = -1
n = iterations(eps, xmin, xmax, umin)