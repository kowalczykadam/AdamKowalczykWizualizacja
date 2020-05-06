import numpy as np
# macierz całkowita
a = np.arange(3, dtype=np.int32)
print(a)
# macierz zmiennoprzecinkowa
b = np.linspace(1,2,3)
print(b)
print(a.dot(b))
