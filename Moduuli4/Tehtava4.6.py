import random
import math

pisteidenMaara = int(input("Anna kuinka monta pistettä ammutaan: "))
i = 0
pisteitaSisalla = 0
while i < pisteidenMaara:
    i += 1
    x = float(random.uniform(-1, 1))
    y = float(random.uniform(-1, 1))
    if math.pow(x,2)+math.pow(y,2)<1:
        pisteitaSisalla += 1
pi = 4 * pisteitaSisalla / pisteidenMaara
print(pi)
