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
        "nome": input("Nome: "), #chave para nome
        "telefone": input("Telefone: "), #chave para telefone
        "turma": input("Turma: "), #chave para turma
        "idade": int(input("Idade: ")), #chave para idade
        "cpf": input("CPF: ") #chave para cpf
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
        return #retorna, e encerra

    #percorre item por item na lista
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")#mostra no terminal

#função atualizar
def atualizar():

    #mostra no terminal
    print("\n--- Atualizar Aluno ---")

    #se não existir, não tem aluno cadastrado e retorne
    if not os.path.exists(BANCO_DADOS):
        print("Nenhum aluno cadastrado no sistema.")
        return #retorna, e encerra

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
        
            #abrindo o arquivo para sobrescrever
            with open(BANCO_DADOS, 'w', encoding='utf-8') as f:
                json.dump(alunos, f, indent=4, ensure_ascii=False)#sobrescrever
            print("Dados atualizados com sucesso!")#mostra no terminal
            return #retorna, e encerra

    print("Aluno não encontrado.")#mostra no terminal

#função excluir
def excluir():
    print("\n--- Excluir Aluno ---")#mostra no terminal
    if not os.path.exists(BANCO_DADOS):#se não existir, não tem aluno cadastrado
        print("Nenhum aluno cadastrado no sistema.")#mostra no terminal
        return#retorne, e encerra

    with open(BANCO_DADOS, 'r', encoding='utf-8') as f:#abrindo o arquivo para ler
        alunos = json.load(f)#ler o arquivo
        
    cpf_busca = input("Digite o cpf do aluno que deseja remover: ")#pedindo o cpf do aluno para remover
    
    nova_lista = [a for a in alunos if a['cpf'] != cpf_busca]#cria uma nova lista excluindo o aluno que tem o cpf 
    
    if len(nova_lista) < len(alunos):#se a nova lista for maior que antiga, vai verificar
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:#abrindo o arquivo para sobrescrever
            json.dump(nova_lista, f, indent=4, ensure_ascii=False)#subscreve
        print("Aluno removido com sucesso!")#mostra no terminal
    else:#se não
        print("Aluno não encontrado.")#mostra no terminal

def menu():#função mostrar o menu
    if not os.path.exists(BANCO_DADOS):#verifica o arquivo
        with open(BANCO_DADOS, 'w', encoding='utf-8') as f:#abrindo o arquivo para sobrescrever
            json.dump([], f)#escreve com a lista vazia no arquivo

    while True:#enquanto for verdadeiro, se for falsa o loop continua
        print("\n=== SISTEMA ESCOLAR ===")#mostra no terminal 
        print("1. Cadastrar Aluno")#mostra no terminal 
        print("2. Listar Alunos")#mostra no terminal 
        print("3. Atualizar Aluno")#mostra no terminal 
        print("4. Excluir Aluno")#mostra no terminal 
        print("5. Sair")#mostra no terminal 
        
        opcao = input("Escolha uma opção: ")#pedindo para escolher uma opção
        
        if opcao == '1': cadastrar()#se o usuário pedir 1, irá cadastrar
        elif opcao == '2': listar()#se pedir 2, irá listar
        elif opcao == '3': atualizar()#se pedir 3, irá atualizar a lista
        elif opcao == '4' :excluir()#se pedir 4, irá excluir da lista
        elif opcao == '5': break #se pedir 5, quebra o loop
        else: print("Opção inválida!")#se não, opção inválida

menu()#chama a função