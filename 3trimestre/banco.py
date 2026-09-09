import sqlite3


def criar_banco():
    conexao = sqlite3.connect("gestao_escolar.db")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS escolas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS turmas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                id_escola INTEGER NOT NULL,
                FOREIGN KEY (id_escola) REFERENCES escolas(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_turma INTEGER NOT NULL,
                FOREIGN KEY (id_turma) REFERENCES turmas(id)
            )
        """)

        conexao.commit()
        print("Banco de dados conectado com sucesso!")

    except sqlite3.Error as e:
        print("Erro do SQLite:", e)

    finally:
        conexao.close()
