import json

def cadastrar_aluno():
cpf = int(input("Diigte seu cpf: "))
nome_completo = input("Digite seu nome completo: ")
telefone = int(Input("Digite seu telefone: "))
turma = int(input("Digite sua turma: "))
idade = int(input("Digite seu nome "))

sistema = { "cpf" : cpf
            "nome completo" : nome_completo,
            "telefone" : telefone,
            "turma" : turma,
            "idade" : idade
}

def criar():
    with open('dados.json','w')as arquivo:
        