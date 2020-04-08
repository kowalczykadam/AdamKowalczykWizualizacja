import numpy as np
x = np.random.randint(1,10,size=(4,4))
print(x)
lista = [x.item(i,i) for i in range(4)]
print(lista)
