valor_compra = float(input("digite o valor "))
cliete = input("digite se for cliente prime sim/nao")
frete = 50.0

if valor_compra >= 500.00 or (cliente == "sim" and valor_compra > 100.00):
    print ("frete gratis, parabens ")
    frete = 0.0
    print ("valor total " , valor_compra)

valor_total = valor_compra + frete
print ("valor total" , valor_total)