import sqlite

def criar_banco():
    conexao = sqlite3.connect('gestao_escolar.db')
    cursor = conexao.cursor()

    cursor.execute(PRAGMA foreign_keys = ON;)
    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cidade TEXT NOT NULL,
        )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS turmas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            nome_turma TEXT NOT NULL,
            id_escola INTEGER,
            FOREING KEY (id_escola) REFERENCES escolas(id)
        ) 
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER,
            id_alunos INTEGER,
            FOREING KEY (id_turmas) REFERENCES turmas(id)
        )
        ''')
    except sqlite3.Error as e:
        print("Erro do sqlite: ",e)
      