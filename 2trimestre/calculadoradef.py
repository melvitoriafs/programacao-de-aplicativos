largura = ""
comprimento = ""
contador = 0

def calcular_area (largura,comprimento,contador):
    while contador != 3:
        largura = int(input("Digite a largura do local: "))
        comprimento = int(input("Digite o comprimento do local: "))
        area = largura * comprimento
        print(f"A área do terreno é: {area}")
        contador += 1
 
calcular_area(largura,comprimento,contador) 