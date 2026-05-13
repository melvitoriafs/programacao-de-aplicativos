frutas = ["Abacaxi","Açaí","Morango","Goiaba","Jabuticaba", "Tangerina"]
busca = input("digite a fruta que deseja na lista: ")

def esta_na_lista(frutas, buscar):
    for item in frutas:
        if item == buscar:
            return "encontrado!"
    return "não encontrado!"

mensagem = esta_na_lista(frutas, busca)
print(mensagem)
