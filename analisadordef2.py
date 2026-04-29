nome = "Carlos"
lista_vendas = [1200, 1500, 1100, 1900]
meta_mensal = 1400
soma = 0

for numero in lista_vendas:
        soma += numero
        media = soma / 4

def analisar_vendas(nome, lista_vendas, meta_mensal):
    if media >= meta_mensal:
        return "bateu a meta!"
    else:
        return "não bateu a meta!"
    
final = analisar_vendas(nome, lista_vendas, meta_mensal)
print(f"O vendedor {nome} teve média de {media} e {final}")