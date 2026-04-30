rua = int(input("digite o número da rua: "))
numero = int(input("digite seu número: "))
bairro = input("digite o bairro: ")
cidade = input("digite a cidade: ")
cep = int(input("digite o cep: "))

def gerar_etiqueta(rua, numero, bairro, cidade, cep):
    return f"Rua {rua}, N° {numero}, Bairro {bairro}, cep {cep} e cidade {cidade}"

informacoes = gerar_etiqueta(rua, numero, bairro, cidade, cep)
print(informacoes)
