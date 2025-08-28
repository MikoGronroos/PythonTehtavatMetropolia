numero = ""
lista = []
numero = input("Anna numero: ")
while numero != "":
    lista.append(int(numero))
    numero = input("Anna numero: ")

lista.sort(reverse=True)

for x in range(5):
    if x >= len(lista):
        break
    print(lista[x])

