import sqlite3


def cadastrar_escolas():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        nome = input("Insira o nome da escola: ")
        cidade = input("Informe a cidade: ")

        cursor.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )

        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.Error as e:
        print("Erro ao cadastrar escola:", e)

    finally:
        conexao.close()


def listar_escolas():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM escolas")
        escolas = cursor.fetchall()

        print("\n===== ESCOLAS =====")

        if not escolas:
            print("Nenhuma escola cadastrada.")
        else:
            for escola in escolas:
                print(f"ID: {escola[0]}")
                print(f"Nome: {escola[1]}")
                print(f"Cidade: {escola[2]}")
                print("-------------------")

    except sqlite3.Error as e:
        print("Erro ao listar escolas:", e)

    finally:
        conexao.close()


def atualizar_escolas():
    listar_escolas()

    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        id_escola = int(input("Digite o ID da escola: "))
        novo_nome = input("Digite o novo nome: ")
        nova_cidade = input("Digite a nova cidade: ")

        cursor.execute(
            """
            UPDATE escolas
            SET nome = ?, cidade = ?
            WHERE id = ?
            """,
            (novo_nome, nova_cidade, id_escola)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            print("Escola atualizada com sucesso!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.Error as e:
        print("Erro ao atualizar escola:", e)

    finally:
        conexao.close()


def excluir_escolas():
    listar_escolas()

    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    try:
        id_escola = int(input("Digite o ID da escola: "))

        cursor.execute(
            "DELETE FROM escolas WHERE id = ?",
            (id_escola,)
        )

        conexao.commit()

        if cursor.rowcount == 0:
            print("Escola não encontrada.")
        else:
            print("Escola excluída com sucesso!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.IntegrityError:
        print("Não é possível excluir esta escola porque ela possui turmas.")

    except sqlite3.Error as e:
        print("Erro ao excluir escola:", e)

    finally:
        conexao.close()
