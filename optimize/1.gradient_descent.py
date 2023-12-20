# -*- coding: utf-8 -*-
"""
@Time ： 2023/12/20 14:42
@Auth ： gc
"""
import matplotlib.pyplot as plt

def f(x):
    return x**2

def df(x):
    return 2*x

def gradinet_descent(eta, max_iter=10, df=df):
    x = 10
    result = []
    for i in range(max_iter):
        x = x - eta * df(x)
        result.append(x)
    return result

x = gradinet_descent(0.3)
y = [f(i) for i in x]
#
plt.plot(range(len(x)), [f(i) for i in range(len(x))])
plt.scatter(x, y)
plt.show()