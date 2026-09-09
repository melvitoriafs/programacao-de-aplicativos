from banco import criar_banco
from escola import cadastrar_escolas, listar_escolas, atualizar_escolas, excluir_escolas
from turma import cadastrar_turmas, listar_turmas, atualizar_turmas, excluir_turmas
from aluno import cadastrar_alunos, listar_alunos, atualizar_alunos, excluir_alunos


def menu():
    criar_banco()

    opcao = 0

    while opcao != 13:

        print("\n1 - Cadastrar escola")
        print("2 - Listar escola")
        print("3 - Atualizar escola")
        print("4 - Excluir escola")

        print("-------------------")

        print("5 - Cadastrar turmas")
        print("6 - Listar turmas")
        print("7 - Atualizar turmas")
        print("8 - Excluir turmas")

        print("-------------------")

        print("9 - Cadastrar alunos")
        print("10 - Listar alunos")
        print("11 - Atualizar alunos")
        print("12 - Excluir alunos")

        print("-------------------")

        print("13 - Sair")
        print("-------------------")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            cadastrar_escolas()

        elif opcao == 2:
            listar_escolas()

        elif opcao == 3:
            atualizar_escolas()

        elif opcao == 4:
            excluir_escolas()

        elif opcao == 5:
            cadastrar_turmas()

        elif opcao == 6:
            listar_turmas()

        elif opcao == 7:
            atualizar_turmas()

        elif opcao == 8:
            excluir_turmas()

        elif opcao == 9:
            cadastrar_alunos()

        elif opcao == 10:
            listar_alunos()

        elif opcao == 11:
            atualizar_alunos()

        elif opcao == 12:
            excluir_alunos()

        elif opcao == 13:
            print("Programa encerrado...")

        else:
            print("Opção inválida!")


menu()
