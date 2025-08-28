number = ""

number = int(input("Anna numero"))

pienin = number
isoin = number


while True:
    number = input("Anna numero: ")
    if number == "":
        break
    if isoin < int(number):
        isoin = int(number)
    if pienin > int(number):
        pienin = int(number)

print(f"{isoin},{pienin}")
