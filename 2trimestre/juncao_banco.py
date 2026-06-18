import sqlite3
conexao = sqlite.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
   
    FOREIGN KEY 