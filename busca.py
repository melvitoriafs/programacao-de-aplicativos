nomes = ["ana", "alice", "joao", "gustavo", "lara", "melissa" ]
verificar = input("digite seu nome de verificação: ")

if verificar in nomes:
    print(f"o nome {verificar} está na lista! ")
else:
    print(f"o nome {verificar} não foi encontrado na lista ")