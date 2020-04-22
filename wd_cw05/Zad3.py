class Ksztalty:
    
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        return self.x * self.y

    def obwod(self):
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        self.opis = text

    def skalowanie(self, czynnik):
        self.x = self.x * czynnik
        self.x = self.y * czynnik


class Kwadrat(Ksztalty):

    def __init__(self, x):
        self.x =x
        self.y=x
    
    def __ge__(self, other):
        return self.x >= other.x
    
    def __gt__(self, other):
        return self.x > other.x
    
    def __le__(self, other):
        return self.x <= other.x
    
    def __lt__(self, other):
        return self.x < other.x
    
kw = Kwadrat(7)
kw2 = Kwadrat(6)

if kw > kw2:
    print("bok kw jest wiekszy od kw2")
if kw <= kw2:
    print("bok kw jest mniejszy lub rowny kw2")