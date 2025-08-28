yritys = 0
while yritys < 5:
    tunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    if tunnus == "python" and salasana == "rules":
        print("Oikein")
        break
    else:
        print("Väärin")
    yritys += 1
