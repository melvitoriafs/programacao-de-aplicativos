import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute("SELECT * FROM alunos")

todos_alunos = cursor.fetchall()

print("-----ALUNOS CADASTRADOS-----")

if not todos_alunos:
    print("Nenhum aluno cadastrado!")

else:
    for aluno in todos_alunos:
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Telefone: {aluno[2]}")
        print(f"Turma: {aluno[3]}")
        print(f"Idade: {aluno[4]}")
        print(f"CPF: {aluno[5]}")
        print("-" * 30)

conexao.close()

