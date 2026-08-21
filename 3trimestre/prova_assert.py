import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
   

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


def cadastrar_construturas(razao_social, creci_juridico):
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()
   
    try:

        comando_inserir = f'''
                        INSERT INTO construtoras (razao_social, creci_juridico)
                        VALUES ('{razao_social}', '{creci_juridico}') '''

        cursor.execute(comando_inserir)
        conexao.commit()


        return "Construtora cadastrada!"

    except ValueError:
        print("Digite o CRECI apenas com números!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()


def cadastrar_imobiliarias(bairro, id_construtora):
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()
    
    try:
        comando_inserir = f'''
                        INSERT INTO imobiliarias (bairro, id_construtora)
                        VALUES ('{bairro}', '{id_construtora}')'''

        cursor.execute(comando_inserir)
        conexao.commit()

        return "Imobiliária cadastrada!"

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
        conexao.commit()
        return "Dados listados"

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

            return "Construtora alterada!"

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

            return "Imobiliária alterada!"

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
        return "Construtora excluída!"

        id_imobiliaria = int(input("Qual ID da imobiliária deseja deletar: "))

        cursor.execute(f'''
            DELETE FROM imobiliarias
            WHERE id = {id_imobiliaria}''')
        conexao.commit()
        return "Imobiliária excluída!"

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
                nome = input("Digite um nome: ")
                creci = int(input("Digite o creci: "))
                cadastrar_construturas(nome, creci)
                bairro = input("Digite o bairro: ")
                id_construtora = int(input("Digite o id da construtora: "))
                cadastrar_imobiliarias(bairro, id_construtora)

            elif opcao == "2":
                listar_tabelas()

            elif opcao == "3":
                nova_razao_social = input("Qual a nova razão social: ")
                novo_creci = int(input("Qual o novo CRECI jurídico: "))
                novo_bairro = input("Qual o novo bairro: ")
                novo_id_construtora = int(input("Qual o novo ID da construtora: "))
                alterar_tabelas(nova_razao_social, novo_creci, novo_bairro, novo_id_construtora)

            elif opcao == "4":
                id_construtora = int(input("Qual ID da construtora deseja deletar: "))
                id_imobiliaria = int(input("Qual ID da imobiliária deseja deletar: "))
                excluir(id_construtora, id_imobiliaria)
            elif opcao == "5":
                print("Programa encerrado!")
                break
            else:
                print("Opção inválida!")
    except ValueError:
        print("Digite apenas número!!")

# menu()

assert cadastrar_construturas ("blue", 123) ==  "Construtora cadastrada!"
assert cadastrar_imobiliarias ("jardim mga", 2) == "Imobiliária cadastrada!"
assert listar_tabelas () == "Dados listados"
assert alterar_tabelas ("green", 1234, "jardim mg", 2) == "Construtora alterada!", "Imobiliária alterada!"
assert excluir (3, 4) == "Construtora excluída!" , "Imobiliária excluída!"


print("Testes realizados com sucesso! ")
 
