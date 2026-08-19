def eh_par(numero):
    return numero % 2 == 0
assert eh_par(4) == True
assert eh_par(7) == False
assert eh_par(0) == True
assert eh_par(-2) == True
print("Todos os testes passaram com sucesso!")