import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)

# wykres f(x) = 1/x
plt.plot(x, 1/x, label='f(x) = 1/x')

# etykiety osi
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')

# tytuł wykresu
plt.title("Wykres f(x) = 1/x")

# legenda
plt.legend()

plt.show()