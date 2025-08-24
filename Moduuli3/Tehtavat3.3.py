sukupuoli = input("Anna biologinen sukupuolesi: ")
hemoglobiini = int(input("Anna hemoglobiini: "))

if sukupuoli == "Nainen":
    if hemoglobiini < 117:
        print("Pieni")
    elif hemoglobiini > 175:
        print("Suuri")
    else:
        print("Hyvä")
elif sukupuoli == "Mies":
    if hemoglobiini < 134:
        print("Pieni")
    elif hemoglobiini > 195:
        print("Suuri")
    else:
        print("Hyvä")