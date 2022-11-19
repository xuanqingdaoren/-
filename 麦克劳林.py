from sympy import *
x = symbols('x')
f = (1-x)/(1-x+x**2)
for i in range(7):
    f = diff(f,x)
    print(f)