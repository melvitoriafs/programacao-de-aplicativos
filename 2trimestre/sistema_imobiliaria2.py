import sqlite3


def criar_tabelas():
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS construtoras (
                id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                razao_social TEXT NOT NULL,
                creci_juridico INTEGER
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS imobiliarias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bairro TEXT NOT NULL,
                id_construtora INTEGER,
                FOREIGN KEY (id_construtora) REFERENCES construtoras(id)
            )
        ''')

        conexao.commit()
        print("Tabelas criadas com sucesso!")

    except sqlite3.Error as erro:
        print("Erro ao criar as tabelas:", erro)

    finally:
        conexao.close()


criar_tabelas()


def cadastrar_construturas():
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()

    try:
        razao_social = input("Digite a razão social (nome) da construtora: ")
        creci_juridico = int(input("Digite o CRECI jurídico apenas com números: "))

        comando_inserir = f'''
                        INSERT INTO construtoras (razao_social, creci_juridico)
                        VALUES ('{razao_social}', '{creci_juridico}') '''

        cursor.execute(comando_inserir)
        conexao.commit()

        print("Construtora cadastrada!")

    except ValueError:
        print("Digite o CRECI apenas com números!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def cadastrar_imobiliarias():
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()

    try:
        bairro = input("Digite o bairro: ")
        id_construtora = int(input("Digite o ID da construtora: "))

        comando_inserir = f'''
                        INSERT INTO imobiliarias (bairro, id_construtora)
                        VALUES ('{bairro}', '{id_construtora}')'''

        cursor.execute(comando_inserir)
        conexao.commit()

        print("Imobiliária cadastrada!")

    except ValueError:
        print("Digite o ID apenas com números!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def listar_tabelas():
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()

    try:

        cursor.execute("SELECT * FROM construtoras")
        construtoras = cursor.fetchall()

        for construtora in construtoras:
            print(f"ID: {construtora[0]}")
            print(f"Razão Social: {construtora[1]}")
            print(f"CRECI Jurídico: {construtora[2]}")

        cursor.execute("SELECT * FROM imobiliarias")
        imobiliarias = cursor.fetchall()

        for imobiliaria in imobiliarias:
            print(f"ID: {imobiliaria[0]}")
            print(f"Bairro: {imobiliaria[1]}")
            print(f"ID da Construtora: {imobiliaria[2]}")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()

def alterar_tabelas():
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()

    try:
        id_construtora = int(input("Qual é o ID da construtora: "))

        cursor.execute(f'''SELECT * FROM construtoras WHERE id = {id_construtora}''')
        construtora = cursor.fetchone()

        if not construtora:
            print("Não encontrado!")
        else:
            nova_razao_social = input("Qual a nova razão social: ")
            novo_creci = int(input("Qual o novo CRECI jurídico: "))

            comando = f'''
                UPDATE construtoras 
                SET razao_social = '{nova_razao_social}',
                creci_juridico = {novo_creci}
                WHERE id = {id_construtora}'''

            cursor.execute(comando)
            conexao.commit()

            print("Construtora alterada!")

        id_imobiliaria = int(input("Qual é o ID da imobiliária: "))

        cursor.execute(f'''SELECT * FROM imobiliarias WHERE id = {id_imobiliaria}''')
        imobiliaria = cursor.fetchone()

        if not imobiliaria:
            print("Não encontrado!")
        else:
            novo_bairro = input("Qual o novo bairro: ")
            novo_id_construtora = int(input("Qual o novo ID da construtora: "))

            comando = f'''
                UPDATE imobiliarias
                SET bairro = '{novo_bairro}',
                id_construtora = {novo_id_construtora}
                WHERE id = {id_imobiliaria} '''

            cursor.execute(comando)
            conexao.commit()

            print("Imobiliária alterada!")

    except ValueError:
        print("Digite os números corretamente!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()

def excluir():
    try:
        conexao = sqlite3.connect("sistema_imobiliariaa.db")
        cursor = conexao.cursor()

        listar_tabelas()

        id_construtora = int(input("Qual ID da construtora deseja deletar: "))

        cursor.execute(f'''
            DELETE FROM construtoras
            WHERE id = {id_construtora} ''')
        conexao.commit()
        print("Construtora excluída!")

        id_imobiliaria = int(input("Qual ID da imobiliária deseja deletar: "))

        cursor.execute(f'''
            DELETE FROM imobiliarias
            WHERE id = {id_imobiliaria}''')
        conexao.commit()
        print("Imobiliária excluída!")

    except ValueError:
        print("Digite apenas números!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()

def menu():
    try:
        while True:
            print("1 - Cadastrar")
            print("2 - Listar")
            print("3 - Alterar")
            print("4 - Excluir")
            print("5 - Sair")

            opcao = input("Digite uma opção: ")
            if opcao == "1":
                cadastrar_construturas()
                cadastrar_imobiliarias()
            elif opcao == "2":
                listar_tabelas()
            elif opcao == "3":
                alterar_tabelas()
            elif opcao == "4":
                excluir()
            elif opcao == "5":
                print("Programa encerrado!")
                break
            else:
                print("Opção inválida!")
    except ValueError:
        print("Digite apenas número!!")
menu()