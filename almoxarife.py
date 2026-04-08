usuario = ["joao", "maria", "livia", "nicolas"]
usuario = []

print ("1 - adicionar usuario")
print ("2 - entrar (login)")
print ("3 - sair")

opcao = input("escolha uma opção ")
while opcao != "3":
    if opcao == "1":
        usuario = input("digite o nome de usuario ")
        senha = int(input("digite a senha "))

        if usuario in usuarios:
            print("usuario já existe ")
        else:
            usuarios[usuario] = senha
            print("usuario cadastrado com sucesso! ")
        
        opcao = input("escolha uma opção ")

    elif opcao == "2":
        usuario = input("usuario: ")
        senha = input("senha: ")

        if usuario in usuarios and usuarios[usuario] == senha:
            print(f"bem vindo, {usuario}!")
        else:
            print("usuario ou senha incorretos! ")
        
        opcao = input("escolha uma opção ")

    elif opcao == "3":
        print("saindo do sistema...")

    else:
        print("opção inválida! tente novamente ")
    
print("saindo do sistema... ")