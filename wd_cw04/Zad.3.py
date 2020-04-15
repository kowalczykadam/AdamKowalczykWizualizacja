tekst = ["raz", "dwa", "trzy", "cztery"]

with open("zad3.txt", "w+") as plik:
    for line in tekst:
        plik.write(line)
        plik.write("\n")
        print(line)

