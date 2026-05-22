#importar os arquivos
import json
import os

#variável
BANCO_DADOS = 'alunos.json'

#função cadastrar
def cadastrar():

    #mostra no terminal
    print("\n--- Novo Cadastro ---")

    #se o arquivo existe
    if os.path.exists(BANCO_DADOS):

        #abrindo a função de ler
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

            #ler o arquivo
            alunos = json.load(f)

    #se não, criar uma lista
    else:
        alunos = []

    #criação do objeto
    novo_aluno = { #abrindo chave
        "nome": input("Nome: "), 
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    } #fechando chave
    
    alunos.append(novo_aluno)#adicionando novo aluno

    #abrindo a função de escrever
    with open(BANCO_DADOS, 'w', encoding='utf-8') as f:

        #escreve no arquivo
        json.dump(alunos, f, indent=4, ensure_ascii=False)

     #mostra no terminal   
    print("Aluno cadastrado com sucesso!")

#função listar
def listar():

    #mostra no terminal
    print("\n--- Lista de Alunos ---")

    #se o arquivo existe
    if os.path.exists(BANCO_DADOS):

        #abrindo o arquivo para ler
        with open(BANCO_DADOS, 'r', encoding='utf-8') as f:

            #ler o arquivo
            alunos = json.load(f)
    
    else: #criar uma lista
        alunos = []

    #se não existe alunos
    if not alunos:

        #mostra no terminal
        print("Nenhum aluno cadastrado.")
        return

    #percorre item por item na lista
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")

#função atualizar
def atualizar():

    #mostra no terminal
    print("\n--- Atualizar Aluno ---")

    #se não existir, não tem aluno cadastrado e retorne
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return #retorna

    #abrindo o arquivo para ler
    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)#ler o arquivo
        
    cpf_busca = input("Digite o CPF do aluno que deseja editar: ")#pedindo para editar o cpf
    
    #percorre item por item na lista
    for aluno in alunos:
        if aluno['cpf'] == cpf_busca: #está atualizando o nome
            print(f"Editando dados de: {aluno['nome']}") #mostra no terminal
            aluno['nome'] = input(f"Novo Nome ({aluno['nome']}): ") or aluno['nome']
            aluno['telefone'] = input(f"Novo Telefone ({aluno['telefone']}): ") or aluno['telefone']
            aluno['turma'] = input(f"Nova Turma ({aluno['turma']}): ") or aluno['turma']
            aluno['idade'] = int(input(f"Nova Idade ({aluno['idade']}): ") or aluno['idade'])
            aluno['cpf'] = input(f"Novo CPF ({aluno['cpf']}): ") or aluno['cpf']
            #atualiza os dados antigos pelos novos, fornecidos pelo usuário
        
            #abrindo o arquivo para subescrever
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)#subescreve
            print("Dados atualizados com sucesso!")#mostra no terminal
            return #retorna
            
    print("Aluno não encontrado.")#mostra no terminal

#função excluir
def excluir():
    print("\n--- Excluir Aluno ---")#mostra no terminal
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:
        alunos = json.load(f)
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]
    
    if len(nova_lista) < len(alunos):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")

def menu():
    if not os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
            json.dump([], f)

    while True:
        print("\n=== SISTEMA ESCOLAR ===")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Excluir Aluno")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1': cadastrar()
        elif opcao == '2': listar()
        elif opcao == '3': atualizar()
        elif opcao == '4': excluir()
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()