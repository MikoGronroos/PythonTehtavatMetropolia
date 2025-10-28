class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        self.kerros += 1
        print(self.kerros)
        return

    def kerros_alas(self):
        self.kerros -= 1
        print(self.kerros)
        return

    def siirry_kerrokseen(self, kerros):
        while True:
            if kerros < self.kerros and self.kerros > self.alin:
                self.kerros_alas()
            elif kerros > self.kerros and self.kerros < self.ylin:
                self.kerros_ylos()
            else:
                break
        return

class Talo:

    hissit = []

    def __init__(self, alin, ylin, hissienLukumaara):
        self.alin = alin
        self.ylin = ylin
        self.hissienLukumaara = hissienLukumaara
        for i in range(hissienLukumaara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissi, kerros):
        ajettavaHissi = self.hissit[hissi]
        ajettavaHissi.siirry_kerrokseen(kerros)

    def palohalytys(self):
        for i in range(self.hissienLukumaara):
            self.aja_hissia(i, self.alin)

t = Talo(1,10,2)

t.aja_hissia(0, 5)
print("-----")
t.aja_hissia(1, 2)
print("-----")
t.aja_hissia(1, 0)
print("-----")
t.aja_hissia(0, 10)
print("-----")
t.palohalytys()
