import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def criar():
cursor.execute('''
                CREATE TABLE IF NOT EXISTS professores(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                matéria TEXT,
                idade INTEGER,
                cpf TEXT UNIQUE NOT NULL
                salário TEXT,
                escola TEXT
                )''')

nome_professor = input("Digite o nome do professor: ")
telefone_professor = input("Digite o telefone do professor: ")
materia_professor = input("Digite a matéria do professor: ")
idade_professor = int(input("Digite a idade do professor: "))
cpf_professor = input("Digite o cpf do professor: ")
salario_professor = input("Digite o salário: ")
escola_professor = input("Digite a escola: ")

comando_inserir = (f'''
                    INSERT INTO professores (nome_professor, telefone_professor, materia_professor, idade_professor, cpf_professor, salario_professor, escola_professor)
                    VALUES ('{nome_professor})', '{telefone_professor}', '{materia_professor}', '{idade_professor}', '{cpf_professor}', '{salario_professor}', '{escola_professor}')''')
                    
