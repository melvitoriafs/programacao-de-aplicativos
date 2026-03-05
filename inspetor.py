print ("inspetor de qualidade")
comprimento = input("digite se o comprimento esta entre 10cm a 12cm, responda com s/n ")

if comprimento == "s":
    largura = input("digite se a largura esta entre 5cm ou 6cm, responda com s/n")
    if largura == "s":
       print ("peça aprovada")
    else:
        print ("reprovado, problema na largura")
else:
    print ("reprovado, problema no comprimento")
   
   


