import sqlite3
conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_aluno TEXT,
    idade INTEGER,
    curso TEXT,
    email TEXT,
    cpf_aluno TEXT UNIQUE
);
""")
conexao.commit()

try:
    print("\n--- ALUNOS CADASTRADOS ---")
    cursor.execute("SELECT * FROM alunos;")
    linhas = cursor.fetchall()
    
    if not linhas:
        print("Nenhum aluno cadastrado ainda.")
    else:
        for linha in linhas:
            print(f"ID: {linha[0]} | Nome: {linha[1]} | CPF: {linha[5]}")

        print("\n--- ALTERAÇÃO DE DADOS ---")
        id_alterar = int(input("Digite o ID do aluno que deseja alterar: "))
   
        cursor.execute("SELECT id FROM alunos WHERE id = ?", (id_alterar,))
        if cursor.fetchone() is None:
            print("Erro: ID não encontrado no banco de dados.")
        else:
            novo_nome = input("Digite o novo nome do aluno: ")
            novo_cpf = input("Digite o novo CPF do aluno: ")

            comando_alterar = '''
                UPDATE alunos 
                SET nome_aluno = ?, cpf_aluno = ? 
                WHERE id = ?
            '''
            
            cursor.execute(comando_alterar, (novo_nome, novo_cpf, id_alterar))

            conexao.commit()
            print(f"\nSucesso! Os dados do aluno com ID {id_alterar} foram atualizados.")

except sqlite3.IntegrityError:
    print("\nErro: Este CPF já está cadastrado para outro aluno (o CPF deve ser único).")
except ValueError:
    print("\nErro: Por favor, digite um número válido para o ID.")
