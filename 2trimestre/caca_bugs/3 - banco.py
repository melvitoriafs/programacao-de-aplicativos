import sqlite3

def criar_tabelas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT
            )
        ''')
    
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS series (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_serie TEXT,
                id_escola INTERGER,
                FOREIGN KEY (id_escola)REFERENCES escolas (id)
            )
        ''')

    conexao.commit()
    conexao.close()

# estava dando erro porque estava puxando uma referencia de umna tabela que nao existe

