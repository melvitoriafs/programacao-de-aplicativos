saldo_inicial = 1000.0
print ("1-deposito")
print ("2-saque")
print ("3-extrato")
menu = input("escolha 1 para deposito, escolha 2 para saque, escolha 3 para extrato: ")

if menu == "1":
    valor = float(input("digite o valor "))
    if valor > 0.00:
        total = valor + saldo_inicial
        print ("o valor total do saldo foi " , total)

elif menu == "2": 
    valor = float(input("digite o valor "))
    if valor > 0 and (valor <= saldo_inicial or valor == 100.0):
       print ("saque realizado " )

elif menu == "3":
    print ("seu saldo atual é " , saldo_inicial)






