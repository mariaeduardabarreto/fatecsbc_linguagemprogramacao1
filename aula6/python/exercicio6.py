# Versão 1
valor = float(input("Valor: "))
desconto = float(input("Desconto (%): "))
final = valor - (valor * desconto / 100)
print("Final:", final)

# Versão 2
def aplicar_desconto(valor, desconto):
    return valor - (valor * desconto / 100)

valor = float(input("Valor: "))
desconto = float(input("Desconto (%): "))
print("Final:", aplicar_desconto(valor, desconto))
