def nastepny_wyraz(an,q):
    print(an*q)
    
def wyraz_n(a1,q,n):
    print(a1*(q**(n-1)))
    
def suma(a1,q,n):
    if q==1:
        print(n*a1)
    else:
        print(a1*((1-q**n)/(1-q)))
        