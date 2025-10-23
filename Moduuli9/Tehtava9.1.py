class Auto:
    Rekisteritunnus = ""
    Huippunopeus = 0
    TamanhetkinenNopeus = 0
    kuljettuMatka = 0

    def __init__(self, tunnus, nopeus):
        self.Rekisteritunnus = tunnus
        self.Huippunopeus = nopeus

newAuto = Auto("ABC-123", 142)

print(newAuto.Rekisteritunnus)
print(f"{newAuto.Huippunopeus} km/h")
print(newAuto.TamanhetkinenNopeus)
print(newAuto.kuljettuMatka)
