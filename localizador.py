cidades = ["São Paulo" , "Rio de Janeiro" ,  "Curitiba" , "Belo Horizonte"]
usuario = input("Digite o nome de uma cidade ")

if usuario in cidades:
    posicao = cidades.index (usuario)
    print (f"A cidade {usuario} está na posição {posicao}")
else:
    print (f"A cidade {usuario} não tem posição")
