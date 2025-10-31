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

class Sahkoauto(Auto):
    def __init__(self, tunnus, nopeus, kapasiteetti):
        Auto.__init__(self, tunnus, nopeus)
        self.kapasiteetti = kapasiteetti
    

class Polttomoottoriauto(Auto): 
    def __init__(self, tunnus, nopeus, tankki):
        Auto.__init__(self, tunnus, nopeus)
        self.tankki = tankki

auto1 = Sahkoauto("ABC-15", 180, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 32.3)

auto1.kiihdyta(180)
auto2.kiihdyta(165)

auto1.kulje(3)
auto2.kulje(3)

print(f"{auto1.kuljettuMatka}, {auto2.kuljettuMatka}")
