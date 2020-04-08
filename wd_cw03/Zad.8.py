def suma(a1=1, r=1, ile_elementow=10):
    an = a1 + r*(ile_elementow-1)
    print("Suma tego ciagu to:")
    return ((a1+an)/2) * ile_elementow
    
print(suma())
