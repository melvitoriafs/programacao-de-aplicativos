idade = int(input("digite a sua idade: "))
saldo = float(input("digite seu saldo: "))

if idade >= 18 and saldo >= 50.0: 
    print ("acesso autorizado! bem-vindo ao evento")
elif idade < 18 and saldo < 50.0:
    print ("infelimente você não cumpre os requisitos de entrada")
elif idade >= 18 and saldo < 50.0:
    print("infelimente você não cumpre os requisitos de entrada")
elif idade < 18 and saldo >= 50.0:
    print("infelimente você não cumpre os requisitos de entrada")