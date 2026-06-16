import sqlite3

conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
novo_nome = input("Digite o novo nome: ")
novo_cpf = input("Digite o novo CPF: ")

sql = f'''
UPDATE Alunos
SET nome_aluno = '{novo_nome}',
    cpf_aluno = '{novo_cpf}'
WHERE id = {id_aluno}
'''

cursor.execute(sql)

conexao.commit()

if cursor.rowcount > 0:
    print("Aluno atualizado com sucesso!")
else:
    print("Nenhum aluno encontrado com esse ID.")

conexao.close()

