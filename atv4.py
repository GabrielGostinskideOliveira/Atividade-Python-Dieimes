compras = []

while True:
 
    print("1 - Inserir item na lista")
    print("2 - Apagar item da lista")
    print("3 - Listar itens da lista")
    print("4 - Sair")
 
    op = int(input("Digite a opção desejada: "))

    if op == 1:
        item = input("Digite o item que deseja inserir na lista: ")
        compras.append(item)
        print("Item inserido com sucesso!")
    elif op == 2:
        item = input("Digite o item que deseja apagar da lista: ")
        try:
            compras.remove(item)
            print("Item removido com sucesso!")
        except ValueError:
            print("Item não encontrado na lista!")
    elif op == 3:
        print("Itens na lista de compras:")
        for item in compras:
            print("-", item)
    elif op == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente!")
