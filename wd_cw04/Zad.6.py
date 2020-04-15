class Slowa:

    def __init__(self, x, y):
        self.slowo1 = x
        self.slowo2 = y
        
    #sprawdzi czy pierwsze podane slowo jest palindromem
    def sprawdz_czy_palindrom(self):
        x = self.slowo1[::-1]
        if x == self.slowo1:
            return "tak"
        return "nie"
    
    def sprawdz_czy_metagramy(self):
        roznice = 0
        for i in range(0,len(self.slowo1)):
            if self.slowo1[i] is not self.slowo2[i]:
                roznice +=1
        if roznice == 1:
            return "tak"
        return "nie"
    
    def sprawdz_czy_anagramy(self):
        if sorted(self.slowo1) == sorted(self.slowo2):
            return "tak"
        return "nie"
    
    def wyswietl_wyrazy(self):
        return self.slowo1, self.slowo2
    
Slowo = Slowa("kajak", "kadak")

print(Slowo.sprawdz_czy_palindrom())
print(Slowo.sprawdz_czy_metagramy())
print(Slowo.sprawdz_czy_anagramy())
print(Slowo.wyswietl_wyrazy())
