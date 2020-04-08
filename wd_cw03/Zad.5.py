
def proste(a1=0, b1=0, x=0, a2=0, b2=0):
    if(a1==a2):
        print("Proste sa rownolegle")
        return 0
    elif(a1 * a2 == -1):
        print("Proste sa prostopadle")
        return 0
    else:
        print("Proste nie sa rownolegle ani prostopadle")
        return 0

print(proste(a1=1, a2=1))
print(proste(a1=1, a2=-1))
print(proste(a1=3))

