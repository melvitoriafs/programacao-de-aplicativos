poder_de_ataque = int(input("digite os pontos "))
poder_de_defesa = int(input("digite os pontos ")) 
dano = poder_de_ataque - poder_de_defesa

if dano <= 0: 
    print ("o vilão bloqueou o ataque! dano= 0 ")
elif dano > 0: 
    print ("ataque crítico! você causou dano ao vilão de" , dano)