import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def criar():
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS professores(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    materia TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL,
                    salario REAL,
                    escola TEXT
                    )''')

    nome_professor = input("Digite o nome do professor: ")
    telefone_professor = input("Digite o telefone do professor: ")
    materia_professor = input("Digite a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("Digite o cpf do professor: ")
    salario_professor = float(input("Digite o salário: "))
    escola_professor = input("Digite a escola: ")

    comando_inserir = (f'''
                        INSERT INTO professores (nome, telefone, materia, idade, cpf, salario, escola)
                        VALUES ('{nome_professor}', '{telefone_professor}', '{materia_professor}', '{idade_professor}', '{cpf_professor}', '{salario_professor}', '{escola_professor}')''')
                        
    cursor.execute(comando_inserir)
    conexao.commit()

def listar():
    cursor.execute("SELECT * FROM professores")

    todos_professores = cursor.fetchall()

    print("-----PROFESSORES CADASTRADOS-----")

    if not todos_professores:
        print("Nenhum professor cadastrado!")

    else:
        for professor in todos_professores:
            print(f"ID: {professor[0]}")
            print(f"Nome: {professor[1]}")
            print(f"Telefone: {professor[2]}")
            print(f"Matéria: {professor[3]}")
            print(f"Idade: {professor[4]}")
            print(f"CPF: {professor[5]}")
            print(f"Salário: {professor[6]}")
            print(f"Nome escola: {professor[7]}")
            print("-" * 30)


def alterar():
    listar()
    id_professor = int(input("Digite o ID do professor que deseja alterar: "))
    novo_nome = input("Digite o novo nome: ")
    novo_cpf = input("Digite o novo CPF: ")

    sql = f'''
    UPDATE Professores
    SET nome = '{novo_nome}',
        cpf = '{novo_cpf}'
    WHERE id = {id_professor}
    '''

    cursor.execute(sql)

    conexao.commit()

    if cursor.rowcount > 0:
        print("Professor atualizado com sucesso!")
    else:
        print("Nenhum professor encontrado com esse ID.")


def excluir():

    id_professor = int(input("Digite o ID do professor que deseja excluir:"))
    sql = f"DELETE FROM Professores WHERE id = {id_professor}"

    cursor.execute(sql)
    conexao.commit
    
    if cursor.rowcount > 0:
        print("Professor excluído com sucesso! ")
    else:
        print("Nenhum aluno encontrado com esse ID ")

def menu():
    opcao = 0
    while opcao != 5:
        print("\n---CADASTRANDO PROFESSORES---")
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


