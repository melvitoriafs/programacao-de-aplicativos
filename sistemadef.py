valor_base = int(input("digite um valor: "))
imposto_percentual = int(input("digite outro valor: "))
cupom_desconto = int(input("digite o último valor: "))


def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    imposto = valor_base + imposto_percentual
    cupom_total = imposto - cupom_desconto
    if cupom_total > 0:
    return cupom_total

calcular_preco_final = (valor_base, imposto_percentual, cupom_desconto)
print(f"o valor final é {cupom_total}")


