import math

def laskeHinta(halkaisija, hinta):
    c = 2 * math.pi * (halkaisija / 2)
    a = c * (halkaisija / 4)
    hintaPerNeliometri = hinta / a
    return hintaPerNeliometri

ekaHalkaisija = float(input("Anna ensimmäisen halkaisija: "))
ekaHinta = float(input("Anna ensimmäinen hinta: "))

tokaHalkaisija = float(input("Anna toinen halkaisija: "))
tokaHinta = float(input("Anna toinen hinta: "))

ekaNeliometriHinta = laskeHinta(ekaHalkaisija, ekaHinta)
tokaNeliometriHinta = laskeHinta(tokaHalkaisija, tokaHinta)

if ekaNeliometriHinta < tokaNeliometriHinta:
    print("Ensimmäinen pitsa parempi")
elif tokaNeliometriHinta < ekaNeliometriHinta:
    print("Toinen pitsa parempi")
else:
    print("Molemmat yhtä hyviä")

