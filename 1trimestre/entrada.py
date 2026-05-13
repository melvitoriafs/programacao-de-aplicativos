idade = int(input("digite a sua idade: "))
ingresso = input("possui ingresso? sim/nao: ")
lista_convidados = input("está na lista? sim/nao: ")

if (idade >= 18 and ingresso == "sim") or lista_convidados == "sim":
    print("seja bem vindo ")
else: 
    print("acesso negado ")
