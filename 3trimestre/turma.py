
import sqlite3


def cadastrar_turmas():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        nome_turma = input("Insira o nome da turma: ")
        id_escola = int(input("Informe o ID da escola: "))

        cursor.execute(
            """
            INSERT INTO turmas (nome_turma, id_escola)
            VALUES (?, ?)
            """,
            (nome_turma, id_escola)
        )

        conexao.commit()
        print("Turma cadastrada com sucesso!")

    except ValueError:
        print("O ID da escola deve ser um número.")

    except sqlite3.IntegrityError:
        print("A escola informada não existe.")

    except sqlite3.Error as e:
        print("Erro ao cadastrar turma:", e)

    finally:
        conexao.close()


def listar_turmas():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM turmas")
        turmas = cursor.fetchall()

        print("\n===== TURMAS =====")

        if not turmas:
            print("Nenhuma turma cadastrada.")
        else:
            for turma in turmas:
                print(f"ID: {turma[0]}")
                print(f"Turma: {turma[1]}")
                print(f"ID da escola: {turma[2]}")
                print("-------------------")

    except sqlite3.Error as e:
        print("Erro ao listar turmas:", e)

    finally:
        conexao.close()


def atualizar_turmas():
    listar_turmas()

    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        id_turma = int(input("Digite o ID da turma: "))
        novo_nome = input("Digite o novo nome da turma: ")
        nova_escola = int(input("Digite o novo ID da escola: "))

        cursor.execute(
            """
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            """,
            (novo_nome, nova_escola, id_turma)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            print("Turma atualizada com sucesso!")

    except ValueError:
        print("Os IDs devem ser números.")

    except sqlite3.IntegrityError:
        print("A escola informada não existe.")

    except sqlite3.Error as e:
        print("Erro ao atualizar turma:", e)

    finally:
        conexao.close()


def excluir_turmas():
    listar_turmas()

    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        id_turma = int(input("Digite o ID da turma: "))

        cursor.execute(
            "DELETE FROM turmas WHERE id = ?",
            (id_turma,)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Turma não encontrada.")
        else:
            print("Turma excluída com sucesso!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.IntegrityError:
        print("Não é possível excluir esta turma porque ela possui alunos.")

    except sqlite3.Error as e:
        print("Erro ao excluir turma:", e)

    finally:
        conexao.close()
