def busca_binaria(vetor, numero):
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if vetor[meio] == numero:
            return meio

        elif numero < vetor[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    return -1


vetor = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

numero = int(input("Digite o número que deseja procurar: "))

posicao = busca_binaria(vetor, numero)

if posicao != -1:
    print("Número encontrado na posição:", posicao)
else:
    print("Número não encontrado.")
