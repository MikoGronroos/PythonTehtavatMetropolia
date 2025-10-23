import random

class Auto:
    Rekisteritunnus = ""
    Huippunopeus = 0
    TamanhetkinenNopeus = 0
    kuljettuMatka = 0

    def kiihdyta(self, muutos):
        self.TamanhetkinenNopeus += muutos
        if self.TamanhetkinenNopeus > self.Huippunopeus:
            self.TamanhetkinenNopeus = self.Huippunopeus
        if self.TamanhetkinenNopeus < 0:
            self.TamanhetkinenNopeus = 0

    def kulje(self, aika):
        if aika < 0:
            return
        self.kuljettuMatka += self.TamanhetkinenNopeus * aika

    def __init__(self, tunnus, nopeus):
        self.Rekisteritunnus = tunnus
        self.Huippunopeus = nopeus

lista = []

for i in range(10):
    lista.append(Auto(f"ABC-{i + 1}", random.randint(100,200)))
kilpailuKaynnissa = True

while kilpailuKaynnissa:
    for i in range(len(lista)):
        lista[i].kiihdyta(random.randint(-10, 15))
        lista[i].kulje(1)
        if lista[i].kuljettuMatka >= 10000:
            kilpailuKaynnissa = False
            break

for i in range(len(lista)):
    print(f"{lista[i].Rekisteritunnus}")
    print(f"{lista[i].Huippunopeus}")
    print(f"{lista[i].TamanhetkinenNopeus}")
    print(f"{lista[i].kuljettuMatka}")
    
