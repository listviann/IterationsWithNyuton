#-*- coding: cp1251 -*-
from sympy import sqrt, diff
from sympy.abc import x
from sympy.functions.elementary.exponential import exp

def check_kantorovich_condition(func, _x, _x0):
    b = abs(1 / diff(func, _x).subs(_x, _x0))
    n = abs(func.subs(_x, _x0) / diff(func, _x).subs(_x, _x0))
    k = abs(diff(func, _x, 2).subs(_x, _x0))
    h = b * n * k
    if h <= 0.5:
        a_h = (1 - sqrt(1 - 2 * h)) * n / h
        return a_h <= 0.5
    return 0

def calculate(func, _x, _x0):
    e = 0.001
    x_n = _x0
    k = 0
    max_k = 1000
    while k <= max_k:
        k += 1
        x_n1 = x_n - func.subs(_x, x_n) / diff(func, _x).subs(_x, x_n)
        if abs(x_n1 - x_n) <= e:
            break
        x_n = x_n1
    return x_n, k



def check_final(func, _x):
    temp = func.subs(x, _x)
    print("\nВыражение в проверке равно: ", temp)


expression = x**2 * exp(2*x) - 1
root = 0.5

if not check_kantorovich_condition(expression, x, root):
    print("Условие сходимости кантаровича не выполнено!")
root, k = calculate(expression, x, root)
print(f"\nКорень уравнения: {root} \nКоличество итераций: {k}")
check_final(expression, root)