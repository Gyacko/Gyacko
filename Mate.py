import matplotlib.pyplot as plt
import numpy as np

# función f(x) = 2x
def funcion_1(x):
    return 2*x

# función f(x) = x + 2
def funcion_2(x):
    return x + 2

# función f(x) = -0.5x + 3
def funcion_3(x):
    return -0.5*x + 3

# dominio de -5 a 5 con incremento de 0.1
x = np.arange(-5, 5, 0.1)

# graficamos las funciones en una misma figura
plt.plot(x, funcion_1(x), label='f(x) = 2x')
plt.plot(x, funcion_2(x), label='f(x) = + 2')
plt.plot(x, funcion_3(x), label='f(x) = -0.5x + 3')

# personalizamos la gráfica con las líneas centrales
plt.axhline(0, color='black', lw=0.5)
plt.axvline(0, color='black', lw=0.5)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráficas de algunas funciones')
plt.legend()

# mostramos la gráfica
plt.show()
