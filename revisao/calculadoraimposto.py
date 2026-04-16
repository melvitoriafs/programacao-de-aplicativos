salarios = [2000, 2750, 4400, 1800, 1000]
for s in salarios:
    if s <= 2000.00:
        imposto = s * 0.10
        sobra = s - imposto
        percentual = "10%"
    elif s > 2000:
        imposto = s * 0.20
        sobra = s - imposto
        percentual = "20%"


    print(f"O Salário {s} foi cobrado {percentual} de imposto")