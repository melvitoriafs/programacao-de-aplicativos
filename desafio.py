nome_cliente = input("digite o seu nome ")
valor_total = float(input("digite o valor total da compra "))
distancia_entrega = int(input("digite a distacia da entrega "))
cupom_especial = input("digite o nome do cupom ")
frete_fixo = 40.00

if valor_total >= 1000.00 and cupom_especial == "s":
    desconto = valor_total * 0.20
    total = valor_total - desconto
    print ("parabens! você ganhou um mousepad gamar de brinde!")

elif valor_total > 500.00 and valor_total < 1000.00 and cupom_especial == "s":
    desconto = valor_total * 0.10
    total = valor_total - desconto


if distancia_entrega <= 50 and valor_total > 200.00:
    frete = 0.00
    valor_final = valor_total + frete
else:
    valor_final = valor_total + frete


print ("nome do cliente" , nome_cliente)
print ("valor total" , valor_final)
print ("valor do desconto " , cupom_especial)
print ("valor a pagar" , valor_total)


