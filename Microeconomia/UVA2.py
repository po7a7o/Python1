from sympy import *
from matplotlib import pyplot

import sympy as sy
import numpy as np
import matplotlib as plt

x = Symbol('x')

#Qd = input("Ingrese función de demanda: /n")
#Qo = input("Ingrese función de oferta: /n")

Qd = 100-15*x
Qo = 50+10*x

print ("Función de demanda: ",Qd)
print ("Función de oferta: ",Qo)

x_graph = range(-10, 15)

# Graficar ambas funciones.
pyplot.plot(x, [Qd(i) for i in x])
pyplot.plot(x, [Qo(i) for i in x])

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
pyplot.xlim(-10, 10)
pyplot.ylim(-10, 10)

# Guardar gráfico como imágen PNG.
#pyplot.savefig("output.png")

# Mostrarlo.
pyplot.show()
