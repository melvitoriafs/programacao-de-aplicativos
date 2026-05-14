def criar_arquivo():
    open('viagens.txt', 'w').close()

def criar():
    lugar = input("Sugere algum lugar: ")
    with open('viagens.txt', 'a')as f:
        f.write(lugar + '\n')
    print("Lugares cadastrados ")

def ler():
    with open('viagens.txt', 'r')as f:
        destinos = f.readlines()

        i = 0 
        for destino in destinos:
            print(f"{i} - {destino.strip()}")
            i += 1

def atualizar():
    ler()
    idx = int(input("Digite o id do lugar que deseja alterar: "))
    novo_lugar = input("Novo lugar: ")

    with open('viagens.txt', 'r')as f:
        linhas = f.readlines()

    linhas[idx] = novo_lugar + '\n'

    with open('viagens.txt', 'w')as f:
        f.writelines(linhas)
        print("Lugares atualizados ")

def deletar():
    ler()
    idx = int(input("Digite o id do lugar que deseja excluir: "))
    with open('viagens.txt', 'r')as f:
        linhas = f.readlines()
    del linhas[idx]
    with open('viagens.txt', 'w')as f:
        f.writelines(linhas)
    print("Lugar removido ")

while True: 
    print("\n1- Adicionar destino")
    print("\n2- Listar sugestões")
    print("\n3- Editar sugestão")
    print("\n4- Remover sugestão")
    print("\n5- Sair   ")
    opcao = input("\nEscolha: ")

    if opcao == '1': criar()
    elif opcao == '2': ler()
    elif opcao == '3': atualizar()
    elif opcao == '4': deletar()
    elif opcao == '5': 
        print("Programa encerrado ")
        break






