# Versão 1
a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))

if a == b == c:
    print("Equilátero")
elif a == b or a == c or b == c:
    print("Isósceles")
else:
    print("Escaleno")

# Versão 2
def classificar_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
        return "Isósceles"
    else:
        return "Escaleno"

print(classificar_triangulo(a, b, c))
