import random

lista = []
for i in range(0,5):
    n = random.randint(1,20)
    lista+=[n*4]
print(lista)

plik=open("liczby.txt","w+")
plik.writelines(str(lista))
plik.close()