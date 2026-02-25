nome = input("digite o seu nome? ")
altura = float(input("digite a sua altura? "))

if altura < 1.50: 
    print ("desculpe, você não tem a altura miníma " , nome)
elif altura > 1.50: 
    print ("acesso liberado! dirvita-se na queda livre" , nome)