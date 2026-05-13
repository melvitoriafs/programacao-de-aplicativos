livros_disponiveis = ["python pro" , "banco de dados" , "redes" , "ia" , "hardware"]
livros_emprestados = []
emprestimo = input("Digite o nome do livro que deseja ")
 
if emprestimo in livros_disponiveis: 
    livros_disponiveis.remove(emprestimo)
    livros_emprestados.append(emprestimo)
else:
    print("Desculpe, este livro não está no acervo")

emprestimo2 = input ("Digite o nome do livro está devolvendo ")
if emprestimo2 in livros_emprestados:
    livros_emprestados.remove(emprestimo2)
    livros_disponiveis.append(emprestimo2)
else:
    print("Este livro não consta como emprestado ")

del livros_disponiveis[0:2]
print(f"Estado final das duas listas {livros_disponiveis} e {livros_emprestados}")

