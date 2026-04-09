numero_secreto = 7
tentativa = 0

while tentativa != numero_secreto:
    tentativa = int(input("Tente adivinhar: "))

    if tentativa > numero_secreto:
        print("Tente menor!")
    elif tentativa < numero_secreto:
        print("Tente maior!")

print("Parabéns!")
