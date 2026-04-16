nomes = ["mel", "lara", "maria", "lucas"]

antigo = input("Qual nome você quer mudar? ")
novo = input("Qual o novo nome? ")

posicao = 0 

for nome in nomes:
    if nome == antigo:
        nomes[posicao] = novo
    posicao = posicao + 1

print("Lista atualizada:", nomes)