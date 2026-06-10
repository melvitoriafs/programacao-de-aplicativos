import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS ALUNOS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno TEXT NOT NULL,
                telefone_aluno TEXT,
                turma_aluno TEXT,
                idade_aluno INTEGER,
                cpf_aluno TEXT UNIQUE NOT NULL
                )''')

nome_aluno = input("Digite seu nome: ")
telefone_aluno = input("Digite seu telefone: ")
turma_aluno = input("Digite sua turma: ")
idade_aluno = int(input("Digite sua idade: "))
cpf_aluno = input("Digite seu CPF: ")

comando_inserir = (f'''
                    INSERT INTO alunos (nome_aluno, telefone_aluno, turma_aluno, idade_aluno, cpf_aluno )
                    VALUES ('({nome_aluno})', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}')''')

cursor.execute(comando_inserir)
conexao.commit()
conexao.close()



