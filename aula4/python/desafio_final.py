nomes = []
quantidades = []

for i in range(3):
    nome = input("Produto: ")
    qtd = int(input("Quantidade: "))

    nomes.append(nome)
    quantidades.append(qtd)

print("\nRelatório:")

for i in range(3):
    if quantidades[i] < 5:
        print(f"Produto: {nomes[i]} | Estoque: {quantidades[i]} [REPOSIÇÃO NECESSÁRIA]")
    else:
        print(f"Produto: {nomes[i]} | Estoque: {quantidades[i]}")
