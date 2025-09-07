lentokentat = {"EFHK": "Helsinki-Vantaa"}

while True:
    syote = input("Kirjoita (syota), (hae) tai, (lopeta)")
    if syote == "lopeta":
        break
    elif syote == "syota":
        uusiICAO = input("Anna icao: ")
        uusiNimi = input("Anna nimi: ")
        lentokentat[uusiICAO] = uusiNimi
    elif syote == "hae":
        icao = input("Anna icao: ")
        print(lentokentat[icao])
