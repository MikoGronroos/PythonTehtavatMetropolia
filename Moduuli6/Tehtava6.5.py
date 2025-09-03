import random

lista = []

for i in range(20):
    value = random.randint(1,100)
    lista.append(value)
    print(value)

def poistaParittomat(listaLukuja):
    newLista = []
    for i in range(len(listaLukuja)):
        if float(listaLukuja[i]) % 2 == 0:
            newLista.append(listaLukuja[i])
    return newLista

print("----------")

newNewLista = poistaParittomat(lista)

for i in range(len(newNewLista)):
    print(newNewLista[i])
