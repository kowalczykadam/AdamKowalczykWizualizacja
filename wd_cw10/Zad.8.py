import numpy as np
import matplotlib.pyplot as plt
import random

def rzucaj(n):
    wektor = []
    for i in range(0,n):
        suma = 0
        for i in range(0,2):
            x = random.randint(1,6)
            suma +=x
        wektor.append(suma)
    print(wektor)
    plt.hist(wektor, bins=n, facecolor='g', alpha=0.75, density=False)
    plt.xlabel('Suma')
    plt.ylabel('ile razy')
    plt.title('ile razy wystepuje suma')
    plt.grid(True)
    plt.show()
    
rzucaj(100)