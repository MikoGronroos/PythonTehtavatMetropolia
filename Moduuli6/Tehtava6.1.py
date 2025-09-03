import random

noppanumero = 0

def noppa():
    return random.randint(1,6)

while noppanumero != 6:
    noppanumero = noppa()
    print(noppanumero)

