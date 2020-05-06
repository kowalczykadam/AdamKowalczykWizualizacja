import numpy as np
x = np.arange(6).reshape(2,3)
a = np.sin(x)
y = np.arange(6).reshape(2,3)
b = np.cos(y)
c = a+b
print(c)