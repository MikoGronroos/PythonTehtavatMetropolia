import random

nopanSivujenMaara = int(input("Anna sivujen: "))
i = 0

def noppa(tahkot):
    return random.randint(1, tahkot)

while i != nopanSivujenMaara:
    i = noppa(nopanSivujenMaara)
    print(i)


