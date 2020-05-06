import numpy as np
b = np.arange(12)
print(b)
print(b.shape)
# przeksztalacamy ja na macierz 3x4
c = b.reshape((3,4))
print(c)
print(c.shape)
# przeksztalacamy ja na macierz 4x3
d = c.reshape((4,3))
print(d)
print(d.shape)
# przeksztalcamy ja na macierz 2x6
e = c.reshape((2,6))
print(e)
print(e.shape)
#splaszczamy macierze
f = c.ravel()
print(f)
g = d.ravel()
print(g)
h = e.ravel()
print(h)