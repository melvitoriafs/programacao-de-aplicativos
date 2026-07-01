import sqlite3 

# O aluno criou a conexão fora das funções para "facilitar".
# Por que isso quebra o sistema quando usamos multiplos arquivos (módulos)?
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSER INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit()
