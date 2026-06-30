import sqlite3

def criar_tabela():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # Este bloco quebra ao rodar pela primeira vez em um banco limpo. Por quê?
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_serie TEXT,
            id_escola INTEGER
            FOREIGN KEY (id_escola) REFERENCES escolas(id)
    )
''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT
        )
''')
conexao.commit()
conexao.close()