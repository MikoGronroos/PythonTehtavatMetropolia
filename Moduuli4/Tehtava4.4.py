import random

luku = random.randint(1,10)

while True:
    pelaajanLuku = int(input("Annan luku: "))
    if pelaajanLuku == luku:
        print("Oikein")
        break
    elif pelaajanLuku < luku:
        print("Liian alhainen")
    elif pelaajanLuku > luku:
        print("Liian suuri")

