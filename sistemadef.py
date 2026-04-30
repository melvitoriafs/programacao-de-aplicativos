valor_base = int(input("Digite o valor bruto do item: "))
imposto_percentual = float(input("Digite o valor do imposto estadual: "))
cupom_desconto = float(input("Digite a porcentagem do cupom de desconto: "))

def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    valor_com_imposto = valor_base - imposto_percentual
    valor_cupom = valor_com_imposto - cupom_desconto
    if valor_cupom > valor_com_imposto:
        return 0

resultado = calcular_preco_final(valor_base, imposto_percentual, cupom_desconto)
print(resultado)

