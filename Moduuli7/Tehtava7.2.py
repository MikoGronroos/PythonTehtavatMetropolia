nimiSetti = set()

while True:
    nimi = input("Anna nimi: ")
    if nimi == "":
        break
    if nimi in nimiSetti:
        print("Nimi on jo")
    else:
        print("Nimi ei ole")
        nimiSetti.add(nimi)
   
print(nimiSetti)

