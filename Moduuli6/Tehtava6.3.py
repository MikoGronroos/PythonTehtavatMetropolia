newGallons = 0


def laskeGallonitLitroiksi(gallons):
    return gallons * 3.785

while True:
    newGallons = float(input("Anna gallonat: "))
    if newGallons < 0:
        break
    litrat= laskeGallonitLitroiksi(newGallons)
    print(litrat)
