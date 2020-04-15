class ciag:
    wartosci = 0
    
    def wyswietl_dane(self):
        return ciag.wartosci
    
    def pobierz_elementy(self):
        print("Podaj elementy ciagu")
        ciag.wartosci = input()
    
    def pobierz_parametry(self):
        print("podaj pierwsza wartosc")
        x = input()
        print("podaj roznice")
        z = input()
        print("podaj ilosc elementow")
        y = input()
        x = int(x)
        y = int(y)
        z = int(z)
        b = y*z+x
        ciag.wartosci = [z for z in range(x, b, z)]
    
    def policz_sume(self):
        return sum(ciag.wartosci)
    
    def policz_elementy(self):
        print("podaj pierwszy element")
        a = input()
        a = int(a)
        print("podaj roznice")
        r = input()
        r = int(r)
        print("podaj jaki element policzyc")
        n = input()
        n = int(n)
        an = a+(n-1)*r
        return an
        
ciagi = ciag()

ciagi.pobierz_elementy()
print(ciagi.wyswietl_dane())
ciagi.pobierz_parametry()
print(ciagi.wyswietl_dane())
print(ciagi.policz_sume())
print(ciagi.policz_elementy())





