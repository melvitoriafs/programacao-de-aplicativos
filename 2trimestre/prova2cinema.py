import sqlite3

def cadastrar_cinemas():
    conexao = sqlite3.connect('sistema_cinema.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE  IF NOT EXISTS cinemas (
                id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                shopping TEXT NOT NULL
            )
            ''')
    
    try:
        nome_cinema = input("Digite o nome do cinema: ")
        shopping = input("Digite o nome do shopping: ")

        comando_inserir = (f'''
                            (INSERT INTO cinemas (nome, shopping))
                            VALUES ('{nome_cinema}', '{shopping}')''')
    except ValueError as erro:
        print("Digite apenas o nome!")

    except sqlite3.IntegrityError as erro:
        print("Erro! Informações cadastradas")
        
    finally:
        conexao.commit()
        print("Cinema cadastrado!")
     
        conexao.close()

def cadastrar_salas():
    conexao = sqlite3.connect('sistema_cinema.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS cinemas (
                id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                numero_sala INTEGER,
                capacidade INTEGER UNIQUE NOT NULL,
                id_cinema INTEGER,
                FOREIGN KEY (id_cinemas) REFERENCES cinemas(id)
                )
                ''')

    try:
        numero_sala = int(input("Digite o número da sala:"))
        capacidade = int(input("Digite a capacidade de pessoas: "))
        id_cinema = int(input("Digite o id do cinema: "))

    comando_inserir = (f'''
                        (INSERT TO cinemas(numero_sala, capacidade, id_cinema))
                        VALUES ('{nome_cinema}', '{capacidade}',{id_cinema})''')

    except ValueError as erro:
        print("Digite apenas números!")
    
    except sqlite3.IntegrityError as erro:
        print("Erro! Informações cadastradas")
    
    finally:
        conexao.close()

def listar_tabelas()
    cursor.execute("SELECT * FROM cinemas") 
    cinemas = cursor.fetchall()



