import random

lista = []

for i in range(10):
    value = random.randint(1,10)
    lista.append(value)
    print(value)

print("--------")

def laskeSumma(listaLukuja):
    summa = 0
    for i in range(len(listaLukuja)):
        summa = summa + listaLukuja[i]

    print(summa)

laskeSumma(lista)
