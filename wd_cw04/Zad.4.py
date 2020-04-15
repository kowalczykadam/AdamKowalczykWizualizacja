class NaZakupy:

    def __init__(self, x, y, z, a):
        self.nazwa_produktu = x
        self.ilosc = y
        self.jednostka_miary = z
        self.cena_jed = a
    
    def wyswietl_produkt(self):
        return self.nazwa_produktu,self.ilosc, self.jednostka_miary, self.cena_jed
    
    def ile_produktu(self):
        return self.ilosc, self.jednostka_miary
        
    def ile_kosztuje(self):
        return self.cena_jed * self.ilosc
    
ziemniak = NaZakupy("ziemniak", 5, "kg", 10)

print(ziemniak.wyswietl_produkt())
print(ziemniak.ile_produktu())
print(ziemniak.ile_kosztuje())

