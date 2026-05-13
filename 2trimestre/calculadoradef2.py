nome = input("Digite seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))
idade = int(input("Digite sua idade: "))
categoria = ""

def gerar_relatorio_saude(nome, peso, altura, idade, categoria):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        categoria = "Baixo Peso!"
    elif imc == 18.5 and imc < 24.9:
        categoria = "Normal!"
    elif imc == 25 and imc <29.9:
        categoria = "Sobrepeso!"
    elif imc >= 30:
        categoria = "Obesidade!"
    print(f"Paciente de nome '{nome}', idade: {idade}, altura: {altura}. De acordo com os cálculos você está com {categoria}")

calculo = gerar_relatorio_saude(nome, peso, altura, idade, categoria)