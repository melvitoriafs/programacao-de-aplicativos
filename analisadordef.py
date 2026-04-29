usuario = input("digite um nome para um sistema: ")

def contar_caracteres(nome):
    while len(nome) < 5:
        print("nome de usuário muito curto ")
        nome = input("digite um nome para um sistema: ")
    print("nome aceito")

contar_caracteres(usuario)
   



        