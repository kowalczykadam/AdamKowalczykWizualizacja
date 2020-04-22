def parzyste(data):
    for index in range(0, len(data), 1):
        if index % 2 == 0:  
            yield data[index]


gen = parzyste("Feliks")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
