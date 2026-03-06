print ("segurança de fabrica ")
curso = input("digite se concluiu o curso de segurança, s/n ")

if curso == "s":
    instrutor = input("o instrutor esta presente na sala, s/n ")
    if instrutor == "s":
        print ("acesso liberado: operaçao iniciada ")
    else: 
         print ("acesso negado: faça o treinamento primeiro ")
else:
    print ("acesso negado: faça o treinamento primeiro ")