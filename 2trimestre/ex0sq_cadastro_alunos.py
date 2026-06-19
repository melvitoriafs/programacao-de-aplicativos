import sqlite3

conexao = sqlite3.connect('escola_nova.db')
cursor = conexao.cursor()

def criar():
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS ALUNOS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL
                    )''')

    nome_aluno = input("Digite seu nome: ")
    telefone_aluno = input("Digite seu telefone: ")
    turma_aluno = input("Digite sua turma: ")
    idade_aluno = int(input("Digite sua idade: "))
    cpf_aluno = input("Digite seu CPF: ")
    
    comando_inserir = (f'''
                        INSERT INTO alunos (nome, telefone, turma, idade, cpf)
                        VALUES ('{nome_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}')''')

    cursor.execute(comando_inserir)
    conexao.commit()
    print("Aluno cadastrado com sucesso!")

def listar():
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

def alterar():
    id_aluno = int(input("Digite o ID do aluno que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_cpf = input("Digite o novo CPF: ")

    sql = f'''
    UPDATE Alunos
    SET nome = '{novo_nome}',
        cpf = '{novo_cpf}'
    WHERE id = {id_aluno}
    '''

    cursor.execute(sql)
    conexao.commit()

    if cursor.rowcount > 0:
        print("Aluno atualizado com sucesso!")
    else:
        print("Nenhum aluno encontrado com esse ID.")

def excluir():
    listar()
    
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    if alunos:
        id_aluno = int(input("\nDigite o ID do aluno que deseja excluir: "))
        
        sql = f"DELETE FROM alunos WHERE id = {id_aluno}"
        cursor.execute(sql)
        conexao.commit()
        
        if cursor.rowcount > 0:
            print("Aluno excluído com sucesso!")
        else:
            print("Nenhum aluno encontrado com esse ID.")

def menu():
    opcao = 0
    while opcao != 5:
        print("\n---CADASTRANDO ALUNOS---")
        print("\n1-Criar ")
        print("2-Listar ")
        print("3-Alterar ")
        print("4-Excluir")
        print("5-Sair")

        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 1: criar()
        elif opcao == 2: listar()
        elif opcao == 3: alterar()
        elif opcao == 4: excluir()
        elif opcao == 5:
            conexao.close()
            print("Programa encerrado! ")
            break

menu()
