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
        self.kuljettuMatka = self.TamanhetkinenNopeus * aika

    def __init__(self, tunnus, nopeus):
        self.Rekisteritunnus = tunnus
        self.Huippunopeus = nopeus

newAuto = Auto("ABC-123", 142)

newAuto.kiihdyta(60)
print(newAuto.TamanhetkinenNopeus)
newAuto.kulje(1.5)
print(newAuto.kuljettuMatka)
