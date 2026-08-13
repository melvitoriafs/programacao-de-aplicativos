import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_imobiliaria.db')
    cursor = conexao.cursor()

    try:
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS construtoras (
                    id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                    razao_social TEXT NOT NULL,
                    creci_juridico INTEGER
                    )
                    ''' )

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
    conexao = sqlite3.connect('sistema_imobiliaria.db')
    cursor = conexao.cursor()

    try:
        razao_social = input("Digite a razão social (nome) da imobiliária: ")
        creci_juridico = int(input("Digite o creci juridíco apenas com números: "))
        
        comando_inserir = f'''
                            (INSERT INTO construtoras (razao_social, creci_juridico))
                            VALUES ('{razao_social}', '{creci_juridico}')'''
        cursor.execute(comando_inserir)
        conexao.commit()

        print("Construtora cadastrada!")

    except ValueError:
        print("Digite o CRECI apenas com números!")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()
cadastrar_construturas()
def cadastrar_imobiliarias():
    conexao = sqlite3.connect('sistema_imobiliaria.db')
    cursor = conexao.cursor()

    try:
        bairro = input("Digite o bairro: ")
        id_construtora = int(input("Digite o ID da construtora: "))

        comando_inserir = f'''
                            (INSERT INTO imobiliarias (bairro, id_construtora))
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
cadastrar_imobiliarias()

def listar_tabelas():
    conexao = sqlite3.connect('sistema_imobiliaria.db')
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
    
            


