def buscar_palavra(lista, palavra):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == palavra:
            return True

        elif palavra < lista[meio]:
            fim = meio - 1

        else:
            inicio = meio + 1

    return False


palavras = ["abacaxi", "banana", "laranja", "manga", "melancia", "uva"]

palavra = input("Digite uma palavra: ")

encontrou = buscar_palavra(palavras, palavra)

if encontrou:
    print("Palavra encontrada.")
else:
    print("Palavra não encontrada.")