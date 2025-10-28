class Julkaisu:
    nimi = ""
    

class Kirja(Julkaisu):
    kirjoittaja = ""
    sivumaara = 0
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.nimi = nimi
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
    def tulostaTiedot(self):
        print(f"{self.nimi}")
        print(f"{self.kirjoittaja}, {self.sivumaara}")

class Lehti(Julkaisu):
    paatoimittaja = ""
    def __init__(self, nimi, paatoimittaja):
        self.nimi = nimi
        self.paatoimittaja = paatoimittaja

    def tulostaTiedot(self):
        print(f"{self.nimi}")
        print(f"{self.paatoimittaja}")


aku = Lehti("Aku Ankka", "Aki Hyyppä")
hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku.tulostaTiedot()

hytti.tulostaTiedot()
