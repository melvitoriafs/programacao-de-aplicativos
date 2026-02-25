valor_da_compra = float(input("digite o valor total "))
cupom = input("digite o nome do cupom ")

desconto = valor_da_compra * 0.10
total = valor_da_compra - desconto


if cupom == "DEV10":  
   print ("novo valor: " , total)
else:
    print ("cupom inválido. valor original: R$" , valor_da_compra)



