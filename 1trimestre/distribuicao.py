print ("---DIVISÃO-DE-CARGAS---")

codigo = int(input("digite o codigo "))
peso = float(input("digite o peso "))


if peso < 5 and (codigo % 10 == 0):
    print (f"pacote {codigo}: ENTREGA EXPRESSA ")
elif peso > 50:
    print (f"pacote{codigo}: CAIXA PESADA ")
else: 
    print ("informações inválidas ")