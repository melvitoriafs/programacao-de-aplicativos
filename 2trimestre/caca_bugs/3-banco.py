import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        ''')
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT NOT NULL,
                id_escola INTEGER,
                FOREIGN KEY (id_escola)REFERENCES escolas (id)
            )
        ''')

    conexao.commit()
    conexao.close()
    print("Tabela criado com sucesso!")
criar_tabelas()
# estava dando erro porque estava puxando uma referencia de uma tabela que não existe

