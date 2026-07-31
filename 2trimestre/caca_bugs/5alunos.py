import sqlite3

def vincular_aluno_turma():
    nome = input("Nome do aluno: ")
    try:
        id_turma = int(input("Digite o ID numérico da turma: "))
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO alunos (nome, id_turma) VALUES (?, ?)",
            (nome, id_turma)
        )
        conexao.commit()
    except ValueError:
        print("Erro: Digite apenas números!")
    except sqlite3.Error:
        print("Erro no banco de dados!")
    finally:
        conexao.close()
vincular_aluno_turma()
# adicionou o except ValueError para tratar entradas inválidas, ajustou o nome da coluna
# para id_turma e ajustando o comando INSERT para inserir os dados corretamente.