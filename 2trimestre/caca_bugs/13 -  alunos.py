import sqlite3

def verficar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    #PORQUE O SEGUNDO PRINT NÃO MOSTRA ABSOLUTAMENTE NADA NO CONSOLE?
    print("Primeiro print:", cursor.fetchall())
    print("Segundo print:", cursor.fetchall())

    conexao.close()

