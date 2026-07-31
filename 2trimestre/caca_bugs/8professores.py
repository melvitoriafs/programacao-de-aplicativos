import sqlite3

def cadastrar_professor(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT UNIQUE NOT NULL
        )
    """)

    conexao.commit()
    print("Tabela criada com sucesso")
    conexao.close()
cadastrar_professor("Ines moreira", 33333)

# o erro era por que o cpf não estava unique e ele só pode ser unico 
# para não dar erro tem que colocar unique no cpf


