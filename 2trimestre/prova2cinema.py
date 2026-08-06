import sqlite3

def cadastrar_cinemas():
    conexao = sqlite3.connect('sistema_cinema.db')
    cursor = conexao.cursor()

    cursor.execute('''
                CREATE TABLE  IF NOT EXISTS cinemas (
                id INTEGER UNIQUE PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
            ''')
    
    try:
        nome_cinema = input("Digite o nome do cinema: ")
        nome_cidade = input("Digite o nome da cidade: ")

        comando_inserir = (F'''
                            (INSERT INTO cinemas (nome, cidade))
                            VALUES ('{nome_cinema}', '{nome_cidade}')''')
    except ValueError as erro:
        print("Digite apenas o nome!")

    except sqlite3.IntegrityError as erro:
        print("Erro! Informações cadastradas")
        
    finally:
        conexao.commit()
        print("Cinema cadastrado!")
     
        conexao.close()

def cadastrar_salas():
    