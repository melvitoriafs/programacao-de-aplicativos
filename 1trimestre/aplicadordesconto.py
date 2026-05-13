lista_compras = [150.0, 80.0, 200.0, 50.0] 
lista_desconto = []

def aplicar_promocao(lista_original, nova_lista):
    for item in lista_original:
        if item >= 100.0:
            desconto = item * 0.15
            novo_valor = item - desconto
            nova_lista.append(novo_valor)
    print(nova_lista)

aplicar_promocao(lista_compras, lista_desconto)