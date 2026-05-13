temperatura = float(input("digite a temperatura atual "))

if temperatura <= 30:
    print ("clima estavel ")
else:
    print ("alerta de calor")

umidade = float(input("digite a umidade "))

if temperatura < 30:
    print ("açao: ligar irrigaçao ")
else: 
    print ("açao: ligar apenas ventiladores ")

