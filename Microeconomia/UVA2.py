from sympy import *
from matplotlib import pyplot

import sympy as sy
import numpy as np
import matplotlib as plt

# Etiquetas del grafico
x_label = "Q"
y_label = "P"

# Definir que x es un simbolo
# x = Symbol('x')

#Qd = input("Ingrese función de demanda: /n")
#Qo = input("Ingrese función de oferta: /n")

# Definir las funciones
def Qd(x):
#    return 5-0.1*x
    return 100-15*x
def Qo(x):
#    return -4+0.2*x
    return 50+10*x

temp1 = Qd(0)
temp2 = Qo(0)
temp3a = Qd(x)
temp3 = solve(temp3a)

# Nuevas ecuaciones
temp3_Qd = Qd(x)
temp_b_Qd = solve(temp3_Qd)
b_Qd = int(temp_b_Qd[0])
m_Qd = -0.1*x
# print (b_Qd[0],m_Qd)
# print (temp_b_Qd)

def nQd(x):
    return b_Qd + m_Qd

# print (nQd(x))

temp3_Qo = Qo(x)
temp_b_Qo = solve(temp3_Qo)
b_Qo = temp_b_Qo[0]
m_Qo = +0.2*x
print (b_Qd,m_Qd)
print (temp_b_Qd)
asa = b_Qo+m_Qo

def nQo(x):
    return asa
    return 0.2*x -5

print (asa)
print (Qo(1))
print (nQo(1))

print ("Función de oferta       : ",Qo(x),"//",nQo(1))

# Calcular Precio Equilibrio
q = Qd(x)+-1*(Qo(x))
# Valor P*
p_equil_temp = solve(q)
p_equil = p_equil_temp[0]
# Valor Q*
q_equil = Qd(p_equil)

# Imprimir las funciones
print ("Función de demanda      : ",Qd(x),"//",nQd(1))
print ("Función de oferta       : ",Qo(x),"//",nQo(1))

# Valor x, que en nuestro caso es P
print ("Calcular punto de equilibrio, igualar Qd y Qo")
print (Qd(x)," = ",Qo(x))
print ("Ecuacion simplificada   : ",q)
print ("Precio Equilibrio (P*)  : ",p_equil)
print ("Cantidad Equilibrio (Q*): ",q_equil)

# Calcular los limites del grafico
x_lim = Qo(0)+10
y_lim = Qd(0)+10

print (x_lim,y_lim)

x_graph = range(0, 110)

# Graficar ambas funciones.
pyplot.plot(x_graph, [nQd(i) for i in x_graph])
pyplot.plot(x_graph, [nQo(i) for i in x_graph])

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
#pyplot.xlim(0, x_lim)
#pyplot.ylim(0, y_lim)
pyplot.xlim(0, 110)
pyplot.ylim(0, 10)

# Definir titulo del grafico
pyplot.title("Oferta y Demanda")

# Definir etiquetas ejes
pyplot.xlabel(x_label)
pyplot.ylabel(y_label)

# Agregar leyenda al grafico
pyplot.legend(("Demanda","Oferta"), loc="upper right")

# Agregar P*,Q*
pyplot.text(p_equil,q_equil,"Punto de equilibrio")

# Agregar etiqueta al grafico
# pyplot.text(5,10,"punto")

# Guardar gráfico como imágen PNG.
#pyplot.savefig("output.png")

# Mostrarlo.
pyplot.show()
