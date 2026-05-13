garrafas = int(input("digite o número total de garrafas que passaram pela esteira hoje "))

if  garrafas == 500:
    print ("HORA DA LIMPEZA: Para máquina imediatamente ")
    print ("CONTROLE DE QUALIDADE: Retire a amostra para o teste ")

elif garrafas % 100 == 0: 
    print ("CONTROLE DE QUALIDADE: Retire a amostra para o teste ")

elif garrafas % 500 == 0: 
    print ("HORA DA LIMPEZA: Parar máquina imediatamente ")

else:
    print (f"Produção em dia. Garrafa número {garrafas} processada ")
