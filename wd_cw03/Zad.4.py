
def monotonicznosc(a, b):

    if(a>0):
        return "Funkcja jest rosnaca"
    elif(a<0):
        return "Funkcja jest malejaca"
    else:
        return "Funkcja jest stala"

print(monotonicznosc(1,2))
print(monotonicznosc(-1,2))
print(monotonicznosc(0,3))
