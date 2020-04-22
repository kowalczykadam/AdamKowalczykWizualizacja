class parzyste:
    """Iterator zwracający wartości o parzystych indeksach"""
    def __init__(self, data):
        self.data = data
        self.max = len(data)
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index = self.index + 1
        if self.index == self.max:
            raise StopIteration
        if self.index % 2 == 0:
            return self.data[self.index]
    
imie = "Reks"
it = parzyste(imie)
for element in it:
    print(element)