peso = float(input("digite seu peso (kg) "))
altura = float(input("digite sua altura (m) "))

imc = peso / (altura ** 2)

if imc > 25:
    print("voce está acima do peso ")
else:
    print("voce está abaixo do peso ")