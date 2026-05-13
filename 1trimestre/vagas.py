vagas = ["livre" , "ocupado" , "livre" , "ocupado"]
numero = int(input("digite o número de 0 a 3 "))

if 0 <= numero < 3:
    if numero % 2 == 0 and vagas [numero] == "livre":
        print (f"vaga {numero} autorizada para estacionar")
    else:
        print (f"vaga {numero} indisponível ou fora das regras ")
else:
    print ("indice inválido")