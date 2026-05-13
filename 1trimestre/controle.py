autorizados = ["alice" , "bob" , "carlos" ]
usuario = input("digite o nome de um pesquisador ")

if usuario in autorizados:
    print (f"Acesso permitido! O pesquisador {usuario} está na posição", autorizados.index(usuario))

    lista = input("deseja  remover esse pesquisador da lista? sim ou não ")
    if lista == "sim":
        autorizados.remove(usuario)
        print (F"lista atualizada {autorizados} ")
    
    else:
        print ("acesso encerrado")

else:
    print(f"Acesso negado! O pesquisador {usuario} não foi encontrado ")

    cadastrar = input("deseja cadastrar esse novo pesquisador? (sim/não) ")
    if cadastrar == "sim":
        autorizados.append("usuario")




