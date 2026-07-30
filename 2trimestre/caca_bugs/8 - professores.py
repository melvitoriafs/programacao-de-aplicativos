 import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("""
    DROP TABLE IF EXISTS professores
    """)

    # Cria a tabela novamente com a estrutura correta
    cursor.execute("""
    CREATE TABLE professores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL
    )
    """)

    conexao.commit()

    cursor.execute("""
    INSERT INTO professores (nome, cpf)
    VALUES (?, ?)
    """, ("Gabriel Moya", "000000"))

    conexao.commit()

    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()

    print("Lista de Professores:")
    for professor in professores:
        print(professor)

    conexao.close()

cadastrar_professor("Gabriel Moya", "000000")  

# o erro era por que o cpf não estava unique e ele só pode ser unico 
# para não dar erro tem que colocar unique no cpf


