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

def alterar_tabelas(nova_razao_social=None, novo_creci=None, novo_bairro=None, novo_id_construtora=None):
    conexao = sqlite3.connect('sistema_imobiliariaa.db')
    cursor = conexao.cursor()

    try:
        if nova_razao_social is not None:
            cursor.execute("SELECT id FROM construtoras ORDER BY id DESC LIMIT 1")
            id_c = cursor.fetchone()[0]
            cursor.execute(f"UPDATE construtoras SET razao_social = '{nova_razao_social}', creci_juridico = {novo_creci} WHERE id = {id_c}")
            
            cursor.execute("SELECT id FROM imobiliarias ORDER BY id DESC LIMIT 1")
            id_i = cursor.fetchone()[0]
            cursor.execute(f"UPDATE imobiliarias SET bairro = '{novo_bairro}', id_construtora = {novo_id_construtora} WHERE id = {id_i}")
            
            conexao.commit()
            return "Tabelas alteradas!"

       
        id_construtora = int(input("Qual é o ID da construtora: "))
        cursor.execute(f"SELECT * FROM construtoras WHERE id = {id_construtora}")
        if not cursor.fetchone():
            print("Construtora não encontrada!")
            return
            
        nova_razao_social = input("Qual a nova razão social: ")
        novo_creci = int(input("Qual o novo CRECI jurídico: "))
        cursor.execute(f"UPDATE construtoras SET razao_social = '{nova_razao_social}', creci_juridico = {novo_creci} WHERE id = {id_construtora}")

        id_imobiliaria = int(input("Qual é o ID da imobiliária: "))
        cursor.execute(f"SELECT * FROM imobiliarias WHERE id = {id_imobiliaria}")
        if not cursor.fetchone():
            print("Imobiliária não encontrada!")
            return

        novo_bairro = input("Qual o novo bairro: ")
        novo_id_construtora = int(input("Qual o novo ID da construtora: "))
        cursor.execute(f"UPDATE imobiliarias SET bairro = '{novo_bairro}', id_construtora = {novo_id_construtora} WHERE id = {id_imobiliaria}")
        
        conexao.commit()
        return "Tabelas alteradas!"

    except ValueError:
        print("Digite os números corretamente!")
    except sqlite3.Error as erro:
        print("Erro:", erro)
    finally:
        conexao.close()


def excluir(id_construtora=None, id_imobiliaria=None):
    try:
        conexao = sqlite3.connect("sistema_imobiliariaa.db")
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        if id_construtora is None:
            listar_tabelas()
            id_imobiliaria = int(input("Qual ID da imobiliária deseja deletar primeiro: "))
            cursor.execute(f"DELETE FROM imobiliarias WHERE id = {id_imobiliaria}")
            
            id_construtora = int(input("Qual ID da construtora deseja deletar agora: "))
            cursor.execute(f"DELETE FROM construtoras WHERE id = {id_construtora}")
        
        else:
            cursor.execute(f"DELETE FROM imobiliarias WHERE id = {id_imobiliaria}")
            cursor.execute(f"DELETE FROM construtoras WHERE id = {id_construtora}")

        conexao.commit()
        return "Construtora excluída!"

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
assert alterar_tabelas ("green", 1234, "jardim mg", 2) == "Tabelas alteradas!"
assert excluir (3, 4) == "Construtora excluída!" , "Imobiliária excluída!"


print("Testes realizados com sucesso! ")
 
