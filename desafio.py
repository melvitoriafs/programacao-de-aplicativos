nome_cliente = input("digite o seu nome: ")
valor_total = float(input("digite o valor total da compra: "))
distancia_entrega = int(input("digite a distacia da entrega: "))
cupom_especial = input("possui cupom? sim/nao: ")

desconto = 0.0

if valor_total >= 1000.00 and cupom_especial == "s":
    desconto = valor_total * 0.20


elif valor_total > 500.00 and valor_total < 1000.00 and cupom_especial == "s":
    desconto = valor_total * 0.10

valor_com_desconto = valor_total - desconto

frete = 40.0


if distancia_entrega <= 50 and valor_total > 200.00:
    frete = 0.0
valor_final = valor_com_desconto + frete



print ("nome do cliente " , nome_cliente)
print ("valor total" , valor_final)
print ("valor do desconto " , cupom_especial)
print ("valor a pagar" , valor_total)
print ("distancia da entrega" , distancia_entrega)



