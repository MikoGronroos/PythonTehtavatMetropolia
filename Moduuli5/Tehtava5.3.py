luku = int(input("Annappa luku: "))
onAlkuluku = True
for x in range(luku):
    numero = x + 1
    if float(luku) % numero == 0 and (numero != 1 and numero != luku):
        onAlkuluku = False
        break

print("On alkuluku" if onAlkuluku else "Ei ole alkuluku")


