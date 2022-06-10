import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
Xo = 0
n = 7
x = sp.Symbol('x')
t = sp.cos(x).series(x,Xo,n).removeO()
print(t)
t = sp.lambdify(x,t,'numpy')
xx = np.linspace(Xo -5, Xo + 5, 1000)
yc = np.cos(xx)
yt = t(xx)
plt.plot(xx,yc,xx,yt)
plt.legend(['cos(x)', 'Serie de Taylor de orden 7'])
plt.title('Serie de Taylor de $f(x) =  cos(x) $')
plt.grid(True)
plt.show()