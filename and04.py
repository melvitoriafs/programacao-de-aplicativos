usuario = input("digite o seu nome ")
codigo = int(input("digite o codigo "))

if usuario == "admin" and codigo == 999:
    print ("acesso ao servidor liberado. sistema online ")
else:
    print ("falha na autenticaçâo. alerta de segurança ligado! ")