leiviska = float(input("Anna leiviskät: "))
naulut = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

kaikkiLuodit = (leiviska * 20 * 32) + (naulut * 32) + luodit

grammat = kaikkiLuodit * 13.3
jaannos = grammat % 1000
print(f"{int(grammat / 1000)}, {jaannos}")