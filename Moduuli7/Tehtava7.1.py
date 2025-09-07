lista = [(3,4,5), (6,7,8), (9,10,11),(12,1,2)]
vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")

numero = int(input("Anna numero: "))


for i in range(len(lista)):
    if numero in lista[i]:
        print(vuodenajat[i])
        break

