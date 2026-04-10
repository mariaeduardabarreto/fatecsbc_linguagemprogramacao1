def exibir_cabecalho():
    print("====== SORVETERIA DO DENER ======")


def verificar_estoque_critico(quantidade):
    if quantidade < 5:
        return " [REPOSIÇÃO NECESSÁRIA]"
    return ""


nomes = []
quantidades = []

while True:
    exibir_cabecalho()
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Produto: ")
        qtd = int(input("Quantidade: "))

        nomes.append(nome)
        quantidades.append(qtd)

    elif opcao == "2":
        print("\nRelatório:")

        for i in range(len(nomes)):
            aviso = verificar_estoque_critico(quantidades[i])
            print(f"Produto: {nomes[i]} | Estoque: {quantidades[i]}{aviso}")

    elif opcao == "3":
        break
