compras = []
produtos = input("digite seu produto: ")

while produtos != "fila":
    compras = compras + [produtos]
    produtos = input("digite o nome de um produto(ou 'fim' para finalizar a compra) ")

    print("lista de produtos: ")
    for item in compras:
        print(f"{item}")