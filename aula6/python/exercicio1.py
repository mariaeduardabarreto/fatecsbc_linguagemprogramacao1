# Versão 1 (Procedural)
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")

# Versão 2 (Função)
def verificar_paridade(n):
    if n % 2 == 0:
        print("Par")
    else:
        print("Ímpar")

numero = int(input("Digite outro número: "))
verificar_paridade(numero)
