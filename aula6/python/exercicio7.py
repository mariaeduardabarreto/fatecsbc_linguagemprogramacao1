# Versão 1
nota = int(input("Nota: "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("E")

# Versão 2
def classificar_nota(n):
    if n >= 90:
        return "A"
    elif n >= 80:
        return "B"
    elif n >= 70:
        return "C"
    elif n >= 60:
        return "D"
    else:
        return "E"

nota = int(input("Nota: "))
print(classificar_nota(nota))
