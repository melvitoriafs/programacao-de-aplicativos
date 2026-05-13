funcionario = str(input("digite o seu cargo "))
codigo = int(input("digite o codigo "))
botao = input("botão pressionando? sim/nao ")
equipamento = input("equipamento de proteção EPI completo? sim/nao ")

if (funcionario == "engenheiro" or "tecnico" ) and codigo == "1234" or botao == "sim":
    print ("acesso liberado")
else:
    print ("acesso negado")