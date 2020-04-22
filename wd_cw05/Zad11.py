def fibonacci(n):
    a = 0 
    b = 1
    for i in range(n):
        a, b = b, a + b
        yield a
        
gen = fibonacci(6)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))