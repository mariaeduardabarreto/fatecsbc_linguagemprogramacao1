# Entrada
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade em estoque: "))
preco = float(input("Digite o preço do produto: "))

# Validação
if quantidade < 0:
    print("Erro: A quantidade não pode ser negativa. Tente novamente.")
else:
    # Saída
    print("\nProduto cadastrado com sucesso!")
    print("Nome:", nome)
    print("Quantidade:", quantidade)
    print("Preço: R$", preco)
