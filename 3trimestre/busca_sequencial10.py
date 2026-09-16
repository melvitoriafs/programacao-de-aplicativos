def busca_sequencial(vetor, numero):
    i = 0
    comparacoes = 0

    while i < len(vetor):
        comparacoes = comparacoes + 1

        if vetor[i] == numero:
            return i, comparacoes

        i = i + 1

    return -1, comparacoes


def busca_binaria(vetor, numero):
    inicio = 0
    fim = len(vetor) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2

        comparacoes = comparacoes + 1

        if vetor[meio] == numero:
            return meio, comparacoes

        elif numero < vetor[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    return -1, comparacoes


vetor = []

numero = 1

while numero <= 100:
    vetor.append(numero)
    numero = numero + 1


valores = [10, 50, 95]

i = 0

while i < len(valores):
    numero = valores[i]

    posicao_sequencial, comparacoes_sequencial = busca_sequencial(vetor, numero)

    posicao_binaria, comparacoes_binaria = busca_binaria(vetor, numero)

    print("Número procurado:", numero)

    print("Busca sequencial:")
    print("Posição:", posicao_sequencial)
    print("Comparações:", comparacoes_sequencial)

    print("Busca binária:")
    print("Posição:", posicao_binaria)
    print("Comparações:", comparacoes_binaria)

    i = i + 1








