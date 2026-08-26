def situacao_aluno(media):
 	if media >= 6:
		return "Aprovado"
	else:
		return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado" #maximo
assert situacao_aluno(5.9) == "Reprovado" #minimo
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(6.1) == "Aprovado"

print("Todos os testes passaram com sucesso!")