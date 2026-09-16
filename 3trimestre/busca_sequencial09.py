def posicao_inserir(vetor, numero):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if numero < vetor[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    return inicio


vetor = [2, 5, 8, 10, 15, 20]

numero = int(input("Digite o número que deseja inserir: "))

posicao = posicao_inserir(vetor, numero)

print("O número deve ser inserido na posição:", posicao)