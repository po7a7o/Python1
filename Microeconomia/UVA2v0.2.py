from sympy import *
from matplotlib import pyplot

import sympy as sy
import numpy as np
import matplotlib as plt

# Definir que x es un simbolo
x = Symbol('x')

# Definir las funciones
#Qd = input("Ingrese función de demanda: /n")
#Qo = input("Ingrese función de oferta: /n")
def Qd(x):
    return 100-15*x
#    return 5-0.1*x
def Qo(x):
#    return -4+0.2*x
    return 50+10*x

def f_etiquetar_grafico():
    # Etiquetas del grafico
    x_label = "Q"
    y_label = "P"
    # Calcular maximos x e y
    x_graph = range(-200, 200)

def f_calculo_funciones():
    # Nuevas ecuaciones
    temp3_Qd = Qd(x)
    temp_b_Qd = solve(temp3_Qd)
    b_Qd = int(temp_b_Qd[0])
    # print (b_Qd[0],m_Qd)
    # print (temp_b_Qd)

    def nQd(x):
        return -0.06*x+b_Qd

    # print (nQd(x))

    temp3_Qo = Qo(x)
    temp_b_Qo = solve(temp3_Qo)
    b_Qo = temp_b_Qo[0]

    def nQo(x):
        return 0.1*x+b_Qo
    #    return 0.2*x -5
    # Calcular Precio Equilibrio
    q = Qd(x)+-1*(Qo(x))
    # Valor P*
    p_equil_temp = solve(q)
    p_equil = p_equil_temp[0]
    # Valor Q*
    q_equil = Qd(p_equil)

    # Calculo elasticidades
    EPd = sy.diff(Qd(x))*(p_equil/q_equil)
    EPo = sy.diff(Qo(x))*(p_equil/q_equil)

def f_imprimir_datos():
    # Imprimir las funciones
    print ("Función de demanda              : ",Qd(x),"//",nQd(x))
    print ("Función de oferta               : ",Qo(x),"//",nQo(x))

    # Valor x, que en nuestro caso es P
    print ("Calcular punto de equilibrio, igualar Qd y Qo")
    print (Qd(x)," = ",Qo(x))
    print ("Ecuacion simplificada           : ",q)
    print ("Precio Equilibrio (P*)          : ",p_equil)
    print ("Cantidad Equilibrio (Q*)        : ",q_equil)
    print ("Elasticidad Precio de la Demanda: %.2f" % EPd)
    print (EPd_desc, "%.2f" % EPd)
    print ("Elasticidad Precio de la Oferta : %.2f" % EPo)
    print (EPo_desc, "%.2f" % EPo)


f_etiquetar_grafico()
f_calculo_funciones()

if EPd < 1:
    EPd_desc = "Inelástica - Ante un aumento de un 1% del precio, la cantidad demandada va a disminuir un "
elif EPd == 1:
    EPd_desc = ""
else:
    EPd_desc = "Elástica - "

if EPo < 1:
    EPo_desc = "Inelástica - Ante un aumento de un 1% del precio, la cantidad ofrecida va a aumenta un "
elif EPo == 1:
    EPo_desc = ""
else:
    EPo_desc = "Elástica - "

f_imprimir_datos()

max_y = b_Qd + 5
if Qd(0) >= Qo(0):
    max_x = Qd(0) +10
else:
    max_x = Qo(0)+5

# Graficar ambas funciones.
pyplot.plot(x_graph, [nQd(i) for i in x_graph],'o--',label='Funcion de demanda')
pyplot.plot(x_graph, [nQo(i) for i in x_graph],'x-', label='Funcion de oferta')

# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")

# Limitar los valores de los ejes.
#pyplot.xlim(0, x_lim)
#pyplot.ylim(0, y_lim)
pyplot.xlim(0, max_x)
pyplot.ylim(0, max_y)

# Definir titulo del grafico
pyplot.title("Oferta y Demanda")

# Definir etiquetas ejes
pyplot.xlabel(x_label)
pyplot.ylabel(y_label)

# Agregar leyenda al grafico
pyplot.legend(loc="best")

# Agregar P*,Q*

des = "Punto de equilibrio x="+str(q_equil)+" e y="+str(p_equil)
pyplot.text(q_equil,p_equil,des)
# pyplot.text(q_equil,p_equil,"Punto de equilibrio x=",q_equil," e y=",p_equil)

# Guardar gráfico como imágen PNG.
#pyplot.savefig("output.png")

# Elasticidad Precio de la demanda


# Mostrarlo.
pyplot.show()
