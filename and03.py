nivel = int(input("digite o seu nivel "))
esferas = int(input("digite a quantidades de esferas "))

if nivel >= 20 and esferas >= 50:
    print ("habilidade super salto desbloqueada!")
elif nivel < 20 and esferas < 50:
    print ("requisitos insuficientes para nova habilidade")
elif nivel >= 20 and esferas < 50:
    print ("requisitos insuficientes para nova habilidade")
elif nivel <= 20 and esferas <= 50:
    print ("requisitos insuficientes para nova habilidade")