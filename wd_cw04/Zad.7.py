class Robaczek:
    
    def __init__(self, x, y, krok):
        self.x = x
        self.x = int(self.x)
        self.y = y
        self.y = int(self.y)
        self.krok = krok
        self.krok = int(self.krok)
        
    def idz_w_gore(self, ile_krokow):
        a = ile_krokow * self.krok
        a = int(a)
        self.y += a
    
    def idz_w_dol(self, ile_krokow):
        a = ile_krokow * self.krok
        a = int(a)
        self.y += -a
        
    def idz_w_lewo(self, ile_krokow):
        a = ile_krokow * self.krok
        a = int(a)
        self.x += -a
        
    def idz_w_prawo(self, ile_krokow):
        a = ile_krokow * self.krok
        a = int(a)
        self.x += a
    
    def pokaz_gdzie_jestes(self):
        return "x = ", self.x, "y = ", self.y
    
robak = Robaczek(0, 0, 1)

print(robak.pokaz_gdzie_jestes())
robak.idz_w_gore(1)
robak.idz_w_prawo(2)
print(robak.pokaz_gdzie_jestes())
        