import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 21)

# wykres f(x) = 1/x
plt.plot(x, 1/x, 'g:>', label='f(x) = 1/x')

# etykiety osi
plt.xlabel('x')
plt.ylabel('f(x)')

# tytuł wykresu
plt.title("Wykres funkcji f(x) dla x [1,20]")

# [xmin, xmax, ymin, ymax]
plt.axis([0, 20, 0, 1])

# legenda
plt.legend()

plt.show()