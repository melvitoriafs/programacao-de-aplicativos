senha = input("digite sua senha ")
numero = int(input("digite o número de tentativa "))
token = input("possui token especial VIP? s/n ")

if (senha == "admin123") and (numero % 3 == 0 or token == "s"):
    print (f"tentativa n°{numero}: ACESSO CONCEDIDO ")
else:
    print (f"tentativa n°{numero}: ACESSO BLOQUEADO POR PROTOCOLO ")

