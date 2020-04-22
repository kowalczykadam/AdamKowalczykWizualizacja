class samogloski:
    """Iterator zwracający wartości o parzystych indeksach"""
    def __init__(self, data):
        self.data = data
        self.max = len(data)
        self.index = -1
        self.samogloski = "aeiouy"

    def __iter__(self):
        return self

    def __next__(self):
        if not isinstance(self.data, str):
            return "Argument to nie string"
        self.index = self.index + 1
        if self.index == self.max:
            raise StopIteration
        if self.data[self.index] in self.samogloski:
            return self.data[self.index] 
    
slowo = "parzyste"
it = samogloski(slowo)
for element in it:
    print(element)