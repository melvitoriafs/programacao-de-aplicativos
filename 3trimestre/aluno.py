import sqlite3


def cadastrar_alunos():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        nome = input("Insira o nome do aluno: ")
        idade = int(input("Informe a idade do aluno: "))
        id_turma = int(input("Informe o ID da turma: "))

        cursor.execute(
            """
            INSERT INTO alunos (nome, idade, id_turma)
            VALUES (?, ?, ?)
            """,
            (nome, idade, id_turma)
        )

        conexao.commit()
        print("Aluno cadastrado com sucesso!")

    except ValueError:
        print("Idade e ID da turma devem ser números.")

    except sqlite3.IntegrityError:
        print("A turma informada não existe.")

    except sqlite3.Error as e:
        print("Erro ao cadastrar aluno:", e)

    finally:
        conexao.close()


def listar_alunos():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM alunos")
        alunos = cursor.fetchall()

        print("\n===== ALUNOS =====")

        if not alunos:
            print("Nenhum aluno cadastrado.")
        else:
            for aluno in alunos:
                print(f"ID: {aluno[0]}")
                print(f"Nome: {aluno[1]}")
                print(f"Idade: {aluno[2]}")
                print(f"ID da turma: {aluno[3]}")
                print("-------------------")

    except sqlite3.Error as e:
        print("Erro ao listar alunos:", e)

    finally:
        conexao.close()


def atualizar_alunos():
    listar_alunos()

    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        id_aluno = int(input("Digite o ID do aluno: "))
        novo_nome = input("Digite o novo nome: ")
        nova_idade = int(input("Digite a nova idade: "))
        nova_turma = int(input("Digite o novo ID da turma: "))

        cursor.execute(
            """
            UPDATE alunos
            SET nome = ?, idade = ?, id_turma = ?
            WHERE id = ?
            """,
            (novo_nome, nova_idade, nova_turma, id_aluno)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            print("Aluno atualizado com sucesso!")

    except ValueError:
        print("ID e idade devem ser números.")

    except sqlite3.IntegrityError:
        print("A turma informada não existe.")

    except sqlite3.Error as e:
        print("Erro ao atualizar aluno:", e)

    finally:
        conexao.close()


def excluir_alunos():
    listar_alunos()

    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        id_aluno = int(input("Digite o ID do aluno: "))

        cursor.execute(
            "DELETE FROM alunos WHERE id = ?",
            (id_aluno,)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Aluno não encontrado.")
        else:
            print("Aluno excluído com sucesso!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.Error as e:
        print("Erro ao excluir aluno:", e)

    finally:
        conexao.close()
