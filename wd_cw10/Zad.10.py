import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
b = np.cos(x)
c = np.sin(x)+2
a = np.sin(x)*(-1)
plt.subplot(2, 1, 1)
plt.plot(x, s, label='sin(x)')
plt.plot(x, b, label='cos(x)')

# etykiety osi
plt.xlabel('x')
plt.ylabel('sin(x) i cos(x')

# tytuł wykresu
plt.title("Wykres sin(x) i cos(x)")

# umieszczamy legendę na wykresie
plt.legend()

plt.annotate('max wartosc sin(x)', xy=(1.70, 1), xytext=(7, 1.5), arrowprops=dict(facecolor='black'))

plt.subplot(2, 1, 2)

plt.plot(x, c, label='sin(x)')
plt.plot(x, a, label='sin(x)')
plt.plot(x, b, label='cos(x)')

plt.xlabel('x')
plt.ylabel('sin(x) i cos(x')

plt.title("Wykres sin(x), sin(x) i cos(x)")

plt.legend()


plt.annotate('max wartosc sin(x)', xy=(1.70, 3), xytext=(7, -4), arrowprops=dict(facecolor='black'))
plt.annotate('max wartosc cos(x)', xy=(6.5, 1), xytext=(12, -3), arrowprops=dict(facecolor='black'))

plt.show()