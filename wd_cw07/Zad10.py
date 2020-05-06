import numpy as np
b = np.arange(81).reshape(9,9)
print(b)
print(b.shape)
# spłaszczenie macierzy b
c = b.ravel()
print(c)
print(c.shape)
# transpozycja macierzy b
d = b.T
print(d)
print(d.shape)