vuosiluku = int(input("Anna vuosiluku: "))

if vuosiluku % 100 == 0:
    if vuosiluku % 400 == 0:
        print("On karkausvuosi eka mahis")
    else:
        print("Ei ole karkausvuosi")
elif vuosiluku % 4 == 0:
    print("On karkausvuosi toka mahis")
else:
    print("Ei ole karkausvuosi")