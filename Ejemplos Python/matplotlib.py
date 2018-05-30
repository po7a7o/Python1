import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1,2,3,4], 'bo-')
plt.plot([1, 2, 3, 4], 'b^-') # con la letra indicamos color y con el siguiente la forma del marcador.
plt.ylabel('Este es el label para y') # colocando labels sobre los ejes.
plt.xlabel('Este label es para x')
plt.show()

plt.plot([1,2,3,4], [1,4,9,16], 'yo')
plt.axis([0, 6, 0, 30]) # Colocando escalas en los ejes


t = np.linspace(0., 5., num=30)

t_1, t_2, t_3 = plt.plot(t, t, 'r--', t, np.square(t), 'bs', t, t**3, 'g^')
plt.legend( (t_1, t_2, t_3), ('legend_t_1', 'legend_t_2', 'legend_t_3'), 'upper left', shadow=True)
plt.grid(True)
plt.clf()
# Con upper right, lower left, lower right

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211) # fila x columna nro plot
plt.plot(t1, np.sin(t1), 'bo-')


plt.subplot(212)
plt.plot(t, np.sqrt(t), 'g-')
plt.show()

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 50, normed=1, facecolor='y', alpha=0.75)
plt.text(120, .025, r'$\mu=100,\ \sigma=15$')
plt.title('Este es mi primer histograma')

def f(t):
    'a damped exponential'
    s1 = np.cos(2 * np.pi * t)
    e1 = np.exp(-t)
    return np.multiply(s1,e1)

t1 = np.arange(0.0, 5.0, .2)

plt.text(4., 1., r"$in \; \pi$", fontsize=18)
l = plt.plot(t1, f(t1), 'r-o')

plt.setp(l, 'markersize', 10) # cambia tamaño del marcador
#plt.setp(l, 'markerfacecolor', 'r') # cambia color de marcador

#plt.show()

spread = np.random.rand(50) * 100
center = np.ones(25) * 50
flier_high = np.random.rand(10) * 100 + 100
flier_low = np.random.rand(10) * -100
data = np.concatenate((spread, center, flier_high, flier_low), axis=0)


plt.boxplot(data)
plt.savefig('data/out.svg') # se puede guardar como png svg jpg  y se puede definir
# dpi, transparencia, etc
plt.savefig('data/out.png', dpi=600)

plt.subplot(211)
plt.imshow(np.random.rand(100,100), cmap=cm.summer)
plt.subplot(212)
plt.imshow(rand(100,100), cmap=cm.summer)

cax = plt.axes([0.85, 0.1, 0.075, 0.8])

plt.colorbar(cax=cax)


from scipy import fftpack
b = fftpack.fft2(test)
b = fftpack.fftshift(b)
b = np.abs(b)**10
b = np.log1p(b)
plt.imshow(b)

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
X, Y, Z = axes3d.get_test_data(0.1)
ax.plot_wireframe(X, Y, Z, rstride=3, cstride=3) # distancia entre las lineas
#ax.plot_surface(X, Y, Z, rstride=2, cstride=2,  cmap=cm.coolwarm)
