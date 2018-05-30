from IPython.display import IFrame
IFrame('http://mathesaurus.sourceforge.net/', width=1000, height=350)

import numpy as np

mi_primer_array = np.arange(0., 1000.)
mi_primer_array

from IPython.display import IFrame
IFrame('http://docs.scipy.org/doc/numpy/user/basics.types.html', width=1000, height=350)

print (np.array([128], dtype=np.int8))
print (np.array([128], dtype=np.int32))

import numpy as np
random_array = np.array(np.random.random((4, 3)), dtype=np.float16)
print (random_array)
print (random_array.dtype)

random_array = np.array(np.random.random((4, 3)), dtype=np.float64)
print (random_array)
print (random_array.dtype)

random_array = np.array(np.random.random((4, 3)), dtype=np.int8)
print (random_array)
print (random_array.dtype)

mi_primer_array = np.arange(0, 1000)
mi_primer_array

mi_otro_array = np.array([1, 2, 3, 4, 5, 6, 7])
mi_otro_array

# Por qué usar numpy array sobre listas de python?
import numpy as np

mi_lista = range(0, 1000)
%%timeit
sum(mi_lista)

%%timeit
np.sum(mi_primer_array)

# Creando Matrices Básicas
mi_array_con_ceros = np.zeros((10, 10))
mi_array_con_ceros

mi_array_con_unos = np.ones((4, 6))
mi_array_con_unos

mi_identidad = np.identity((10))
mi_identidad

a = np.arange(0, 20)
a

random_array = np.random.random((4, 3))
random_array

mi_array = np.arange(0, 100)
mi_array.shape = (10, 10)#.reshape((10, 10))
print (mi_array)
print (mi_array.shape)

print (mi_array.dtype)
print (mi_array.ndim)

b = np.linspace(0, 5, 100)
print (b)
print (b.astype(np.int))

# Moviendonos dentro de un NumPy array

from IPython.display import Image
Image(filename="./images/slice.png")

# Algebral Lineal con NumPy
from numpy.linalg import inv, qr
from numpy.linalg import *
x = np.random.random((5, 5))

#print inv(x)
print (qr(x))

from numpy import linalg

print (linalg.eigvals(x))
print (linalg.eig(x))
print (linalg.solve)


# Estadística con NumPy y SciPy
tmp_array = 10 * np.sin(a)
tmp_array_2 = 10 * np.cos(a)
print (tmp_array)
np.sort(tmp_array)
np.median(tmp_array)

np.average(tmp_array)

np.std(tmp_array) #recordar nanmean nanstd nanvar

np.min(tmp_array)

np.max(tmp_array)

np.cov(tmp_array_2, tmp_array)

np.correlate(np.arange(10), np.arange(5, 15))

from IPython.display import IFrame
IFrame('http://docs.scipy.org/doc/scipy/reference/stats.html', width=1000, height=350)

from scipy.stats import distributions as dis
import matplotlib.pyplot as plt

rand_array = dis.norm.rvs(size=100)
plt.plot(rand_array)

c = np.linspace(-5, 5, 100)

pdf = dis.norm.pdf(c) # Probability density func
plt.plot(pdf)

cdf = dis.norm.cdf(c) #cumulative distribution function
plt.plot(cdf)
dis.norm.cdf

ppf = dis.norm.ppf(c) #Percent point fuction
plt.plot(ppf)

random_array = dis.poisson.rvs(1.0, size=100)
plt.plot(random_array)

ppf = dis.poisson.ppf(c, 2.0) # Percent point func
plt.plot(ppf)
