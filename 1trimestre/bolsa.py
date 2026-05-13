media_escolar = float(input("digite sua media "))
renda_familiar = float(input("digite sua renda "))
escola_publica = input("é de escola publica? sim/nao ")

if media_escolar >= 8.0 and (renda_familiar <= 2.000 or escola_publica == "sim"):
    print("voce ganhou a bolsa")
else: 
    print("nao atende os requisitos")

