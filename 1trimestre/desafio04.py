drone = int(input("digite o codigo "))
autorizacao = input("digite se possui autorizaçao da torre, s/n ")

if drone == 999 or autorizacao == "s":
    print ("pouso autorizado ")
    print ("------------")


bateria = int(input("digite a bateria do drone  "))
clima = input("digite se o clima está ensolarado/chuvoso ")
velocidade = int(input("digite a velocidade do vento "))

if bateria <= 10:
    print ("pouso AUTORIZADO IMEDIATAMENTE por segurança ")
    
elif bateria >= 10:
    if (clima == "ensolarado" and velocidade <= 30) or (clima == "chuvoso" and velocidade < 10):
            print ("POUSO AUTORIZADO: Iniciando descida ")
    else:
        print ("POUSO NEGADO: condições meteorológicas perigosas")
else:
    print ("erro 1: drone não identificado. Retornando à base")
