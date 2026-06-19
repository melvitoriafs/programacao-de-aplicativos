import sqlite3
conexao = sqlite3.connect('escola_nova.db')
cursor = conexao.cursor()

cursor.execute('''
                    ALTER TABLE professores ADD COLUMN endereco_professor

''')

conexao.commit()
conexao.close()