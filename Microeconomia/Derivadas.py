from sympy import *
import sympy as sy

x = Symbol('x')
#fx = (2*x**3-4*x)
fx = input("Ingrese funcion: /n")
dx = diff(fx)
print (dx)
