import random

class Kilpailu():
    def __init__(self, nimi, pituus, autoLista):
        self.nimi = nimi
        self.pituus = pituus
        self.autoLista = autoLista
    def tunti_kuluu(self):
        for i in range(len(self.autoLista)):
            self.autoLista[i].kiihdyta(random.randint(-10, 15))
            self.autoLista[i].kulje(1)
        return
    def tulosta_tilanne(self):
        for i in range(len(self.autoLista)):
            print(f"{self.autoLista[i].Rekisteritunnus}")
            print(f"{self.autoLista[i].Huippunopeus}")
            print(f"{self.autoLista[i].TamanhetkinenNopeus}")
            print(f"{self.autoLista[i].kuljettuMatka}")
        print(f"---------------------------")


    def kilpailu_ohi(self):
        for i in range(len(self.autoLista)):
            if self.autoLista[i].kuljettuMatka >= self.pituus:
                return True
        return False

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
#kilpailuKaynnissa = True

#while kilpailuKaynnissa:
#    for i in range(len(lista)):
#        lista[i].kiihdyta(random.randint(-10, 15))
#        lista[i].kulje(1)
#        if lista[i].kuljettuMatka >= 10000:
#            kilpailuKaynnissa = False
#            break

kilpailu = Kilpailu("Suuri romuralli", 8000, lista)

tunti = 0

while True:
    kilpailu.tunti_kuluu()
    if kilpailu.kilpailu_ohi():
        break
    if tunti >= 10:
        kilpailu.tulosta_tilanne()
        tunti = 0
    tunti += 1

kilpailu.tulosta_tilanne()
