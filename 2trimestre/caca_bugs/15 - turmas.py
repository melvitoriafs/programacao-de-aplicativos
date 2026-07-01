import sqlite3

def criar_tabela_turma():
    conexao = sqlite3.connect('sistema.escola_db')
    cursor = conexao.cursor

    #O SQLITE ACUSA O ERRO DE SINTAXE PRÓXIMO AO FOREN KEY. CADÊ O ERRO?
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS turmas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_turma TEXT,
                    id_serie,
                    FOREN KEY (id_serie) REFERENCES series(id)
                    )''')

    conexao.commit()
    conexao.close()
