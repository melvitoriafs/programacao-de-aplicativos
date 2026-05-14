def criar_arquivo():
    open('habitos.txt', 'w').close()


def cadastrar_habito():
    inserir = input("Digite um novo hábito: ")
    with open('habitos.txt', 'a')as f:
        f.write(inserir + '\n')
    print("Novo hábito adicionado ")

def revisar_mural():
    with open('habitos.txt', 'r')as f:
        revisados = f.readlines()

        i = 0
        for revisado in revisados:
            print(f"{i} - {revisado.strip()}")
            i += 1

def editar():
    revisar_mural()
    idx = int(input("Digite o id do hábito que deseja mudar: "))
    novo_habito = input("Novo hábito: ")

    with open('habitos.txt', 'r')as f:
        linhas = f.readlines()

    linhas[idx] = novo_habito + '\n'

    with open('habitos.txt', 'w')as f:
        f.writelines(linhas)
        print("Hábitos atualizados ") 

def deletar():
    ler()
    idx = int(input("Digite o id do hábito que deseja excluir: "))
    with open('habitos.txt', 'r')as f:
        linhas = f.readlines()
    del linhas[idx]
    with open('habitos.txt', 'w')as f:
        f.writelines(linhas)
    print("Hábitos removido ")

while True: 
    print("\n1- Adicionar")
    print("\n2- Ver todos")
    print("\n3- Editar")
    print("\n4- Excluir")
    print("\n5- Sair   ")

    opcao = input("Escolha: ")
    
    if opcao == '1': cadastrar_habito()
    elif opcao == '2': revisar_mural()
    elif opcao == '3': editar()
    elif opcao == '4': deletar()
    elif opcao == '5': 
        print("Programa encerrado ")
        break


