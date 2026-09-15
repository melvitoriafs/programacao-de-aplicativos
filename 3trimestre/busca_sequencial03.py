vetor = [5, 8, 12, 3, 9, 15, 7, 2, 10, 6]

i = 0
maior = vetor[0]
posicao = 0

while i < 10:
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

    i = i + 1

print("Maior número:", maior)
print("Posição:", posicao)

