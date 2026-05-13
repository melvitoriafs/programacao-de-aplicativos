pergunta = input("digite uma senha: ")

def senha_valida (senha):

    while len(senha) < 6:
        senha = input("digite sua senha: ")
    print("Senha cadastrada com sucesso!")
senha_valida(pergunta)
    