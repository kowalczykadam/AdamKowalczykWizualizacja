produkty={"Mleko": "l",
"Maka": "kg",
"Jablka": "sztuki",
"Marchewki": "sztuki"
}
lista=[key  for (key, value) in produkty.items() if value == "sztuki"]
print(lista)

