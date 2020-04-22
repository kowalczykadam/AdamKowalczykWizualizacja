class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
imie = "Reks"
it = Wspak(imie)
for element in it:
    print(element)

liczby = "123456"
l = Wspak(liczby)
for element in l:
    print(element)