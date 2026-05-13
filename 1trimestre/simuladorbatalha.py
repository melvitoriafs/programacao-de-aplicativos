vida_inicial = 50000
valor_dano = 0

def sofrer_dano(vida_inicial, valor_dano):
    while vida_inicial != 0:
        valor_dano = int(input("digite o dano causado:"))
        vida_inicial = vida_inicial - valor_dano
        print(f"saldo atual atualizado: {vida_inicial}")
    print("GAME OVER!")

sofrer_dano(vida_inicial,valor_dano )