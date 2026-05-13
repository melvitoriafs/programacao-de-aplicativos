print ("---E-COMMERCE---")

usuario = int(input("digite o seu o ID? "))
valor_compra = float(input("digite o valor da compra? "))

if usuario % 2 == 0 and valor_compra > 500.00:
    print (f"Parabéns usuário {usuario}! Você ganhou um cupom para sua compra de R$ {valor_compra} ")
else:
    print (f"Obrigado pela compra, usuário {usuario} Continue acompanhando nossas promoções ")
