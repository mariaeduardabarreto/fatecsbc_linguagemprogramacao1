# Versão 1
n = int(input("Número: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)

# Versão 2
def gerar_tabuada(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)

n = int(input("Número: "))
gerar_tabuada(n)
