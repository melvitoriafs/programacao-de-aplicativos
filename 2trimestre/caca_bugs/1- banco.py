import sqlite3

def inicializar_banco():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT
            nome TEXT NOT NULL
        )
    ''')

# O banco não está salvando as alterações. Por quê?
# Está faltando o conexão.commit() e tem que chamar a função
    conexao.commit()
    conexao.close()

chamada = inicializar_banco()
print(chamada)
