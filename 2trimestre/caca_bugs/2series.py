import sqlite3

def cadastrar_series(nome_serie, id_escola):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")
   
    try:
        cursor.execute(
            "INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",
            (nome_serie, id_escola)
        )

        conexao.commit()
        print("Série cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: escola inexistente!")

    finally:
        conexao.close()


cadastrar_series("2º Ano", 1)

#não estava verificando as chaves diferentes, foi adicionado "cursor.execute("PRAGMA foreign_keys = ON")"