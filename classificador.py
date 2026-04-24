nota = int(input("digite uma nota de 0 a 10 "))

def avaliar_desempenho (nota):
    if nota >= 9:
        print("Excelente")
    elif nota >= 7:
        print("Bom")
    elif nota >5:
        print("Regular")
    else:
        print("Insuficiente")

avaliar_desempenho(nota)
