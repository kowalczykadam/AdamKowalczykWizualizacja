import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30, 0.1)
s = np.sin(x)
b = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, b, label='cos(x)')

# etykiety osi
plt.xlabel('x')
plt.ylabel('sin(x) i cos(x')

# tytuł wykresu
plt.title("Wykres sin(x) i cos(x)")

# umieszczamy legendę na wykresie
plt.legend()

plt.show()