produtos = []

while True:
    print("\n1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        quantidade = int(input("Quantidade: "))
        preco = float(input("Preço: "))

        if quantidade < 0:
            print("Erro: quantidade negativa!")
        else:
            produtos.append((nome, quantidade, preco))

    elif opcao == "2":
        for p in produtos:
            print(p)

    elif opcao == "3":
        break
