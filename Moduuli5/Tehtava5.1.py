import random

noppia = int(input("Amount of noppas: "))
summa = 0
for x in range(noppia):
    number = random.randint(1,6)
    summa += number
print(summa)
