estoque = []
menu = 0

def adicionar_produto(nome, estoque):
    estoque.append(nome)


def listar_produtos(estoque):
    for item in estoque:
        indice = estoque.index(item)
        print(f"Posição {indice} nome {item}")


def atualizar_produto(nome, novo_nome, estoque):
    indice = estoque.index(nome)
    estoque[indice] = novo_nome


def remover_produto(nome, estoque):
    indice = estoque.index(nome)
    estoque.pop(indice)


def exibir_menu(menu):
    while menu != 5:
        print("MENU")
        print("1, Adicionar produtos ao estoque")
        print("2, Listar produtos")
        print("3, Atualizar produtos")
        print("4, Remover produtos")
        print("5, Sair")

        menu = int(input("Digite a opção desejada: "))
        
        if menu == 1:
            nome = input("Digite o nome dos produtos para adicionar ao estoque: ")
            adicionar_produto(nome, estoque)
        
        elif menu == 2:
            listar_produtos(estoque)

        elif menu == 3:
            nome = input("Digite o nome do item que é para alterar: ")
            novo_nome = input("Digite o nome que é para colocar no lugar do anterior: ")
            atualizar_produto(nome, novo_nome, estoque)

        elif menu == 4:
            nome = input("Digite o nome do item que deseja remover: ")
            remover_produto(nome, estoque)

        elif menu == 5:
            print("Encerrando o programa")
            break
    
exibir_menu(menu)