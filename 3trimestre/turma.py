
import sqlite3
conexao = None
conexao = sqlite3.connect('gestao_escolar.db')
cursor = conexao.cursor()


def cadastrar_turmas():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        nome_turma = input("Insira a turma: ")
        id_escola = int(input("Informe o id da escola que deseja cadastrar: "))
        comando_inserir = "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)"

        cursor.execute(comando_inserir, (nome_turma, id_escola))
        conexao.commit()
        print("Cadastro concluido!")

    except ValueError as e:
        print("Digite apenas nomes! ", e)
    except sqlite3.IntegrityError as e:
        print("Erro! Informações já cadastradas! ", e)

    finally:
        if conexao:
            conexao.commit() 
            conexao.close()


def listar_turmas():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM turmas")

        info_turmas = cursor.fetchall()

        print(">>> TURMAS CADASTRADASTRADAS <<<")

        if not info_turmas:
            print("Nenhuma informação encontrada!")

        else:
            for inf in info_turmas:
                print(f"ID: {inf[0]}")
                print(f"Turma: {inf[1]}")
                print(f"ID escola: {inf[2]}")
 


    except sqlite3.Error as e:
        print("Erro do sqlite: ", e)


def atualizar_turmas():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()
    listar_turmas()

    try:
        id_turmas = int(input("Insira o id da turma que deseja alterar: "))
        nova_turma = input("Informe a turma nova: ")
        cursor.execute("UPDATE turmas SET nova_turma = ? WHERE id = ?", (id_turmas))

        conexao.commit()
        print("Turma atualizada com sucesso!")

    except sqlite3.Error as e:
        print("Não foi possivel atualizar!", e)


def excluir_turmas():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()
    listar_turmas()

    try:
        id_turmas = int(input("Informe o id da turma que deseja excluir: "))
        cursor.execute("DELETE FROM turmas WHERE id = ?", (id_turmas,))


        conexao.commit()
        print("Turma deletada com sucesso!")

    except sqlite3.Error as e:
            print("Erro: Turma não deletada.", e)








