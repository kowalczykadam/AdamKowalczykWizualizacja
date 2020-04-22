class Material:
    
    def __init__(self, x, y, z):
        self.rodzaj = x
        self.dlugosc = y
        self.szerokosc = z
    
    def wyswietl_nazwe(self):
        return self.rodzaj
    
class Ubrania(Material):
    
    rozmiar = "M"
    kolor = "czerwony"
    dla_kogo = "Klient #4"
    
    def wyswietl_dane(self):
        return self.rozmiar, self.kolor, self.dla_kogo
    
class Sweter(Ubrania):
    rodzaj_swetra = "rozpinany"
    
    def wyswietl_dane(self):
        return self.rodzaj_swetra 
    
ubranie = Sweter("Bawelna", 130, 60)
print(ubranie.wyswietl_nazwe())
print(ubranie.rozmiar)
print(ubranie.wyswietl_dane())
    
