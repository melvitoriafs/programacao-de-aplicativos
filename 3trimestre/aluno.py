import sqlite3
conexao = None
conexao = sqlite3.connect('gestao_escolar.db')
cursor = conexao.cursor()


def cadastrar_alunos():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        nome_aluno = input("Insira o nome do aluno: ")
        idade_aluno = input("Informe a idade do aluno: ")
        comando_inserir = "INSERT INTO alunos (nome, idade) VALUES (?, ?)"

        cursor.execute(comando_inserir, (nome_aluno, idade_aluno))
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


def listar_alunos():
    try:
        conexao = sqlite3.connect('gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM alunos")

        info_alunos = cursor.fetchall()


        if not info_alunos:
            print("Nenhuma informação encontrada!")

        else:
            for inf in info_alunos:
                print(f"ID: {inf[0]}")
                print(f"Nome: {inf[1]}")
                print(f"Idade: {inf[2]}")
                print(f"ID turma: {inf[3]}")



    except sqlite3.Error as e:
        print("Erro do sqlite: ", e)


def atualizar_alunos():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()
    listar_alunos()

    try:
        id_aluno = int(input("Insira o id do aluno que deseja alterar: "))
        novo_aluno = input("Informe o nome novo: ")
        cursor.execute("UPDATE alunos SET novo_aluno = ? WHERE id = ?", (novo_aluno))

        conexao.commit()
        print("Nome atualizado com sucesso!")

    except sqlite3.Error as e:
        print("Não foi possivel atualizar!", e)


def excluir_alunos():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()
    listar_alunos()

    try:
        id_alunos = int(input("Informe o id do aluno que deseja excluir: "))
        cursor.execute("DELETE FROM alunos WHERE id = ?", (id_alunos,))


        conexao.commit()
        print("Aluno deletado com sucesso!")

    except sqlite3.Error as e:
            print("Erro: Aluno não deletado.", e)
