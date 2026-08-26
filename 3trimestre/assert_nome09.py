assert buscar_nome([], "Ana") == False         
assert buscar_nome(["Ana"], "Ana") == True   
assert buscar_nome(["Ana", "João"], "Maria") == False
assert tem_senha_valida("") == False            
assert tem_senha_valida("12345678") == True     
assert tem_senha_valida("abc123") == False  

# buscar o nome em uma lista vazia, o resultado é False,
# pois a lista não contém nenhum nome.
