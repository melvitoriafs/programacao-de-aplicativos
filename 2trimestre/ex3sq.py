import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

id_aluno = int(input("Digite o ID do aluno que deseja excluir: "))

sql = f"DELETE FROM Alunos WHERE id = {id_aluno}"

cursor.execute(sql)
conexao.commit()

if cursor.rowcount > 0:
    print("Aluno excluído com sucesso!")
else:
    print("Nenhum aluno encontrado com esse ID.")

conexao.close()
