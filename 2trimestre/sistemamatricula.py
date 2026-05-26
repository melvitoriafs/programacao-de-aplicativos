import json
import os

sistema_matricula = 'alunos.json'

def cadastrar():
    if os.path.exists(sistema_matricula):
        with open(sistema_matricula, 'r', encoding='utf-8')as f:
            alunos = json.load(f)
    else:
        alunos = []

novo_aluno = {
    "id" : int(input("id: ")),
    "nome completo" : input("nome completo: "),
    "telefone" : input("telefone: "),
    "turma" : input("turma: "),
    "idade" : int(input("idade: ")),
    "cpf" : input("cpf: ")
}

    alunos.append(novo_aluno)

    with open(sistema_matricula, 'w', encoding='utf-8' )as f:
        json.dump(alunos, f, indent=4, ensure_ascii=False)
    print("Aluno cadastrado! ")

def listar():
    if os.path.exists(sistema_matricula):
        with open(sistema_matricula, 'r', encoding='utf-8')as f:
            alunos = json.load(f)
    else:
        alunos = []
        

