def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"

assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14) == "Frio"
assert classificar_temperatura(15) == "Agradável"   #limite inferior
assert classificar_temperatura(20) == "Agradável"
assert classificar_temperatura(25) == "Agradável"   #limite superior
assert classificar_temperatura(26) == "Quente"
