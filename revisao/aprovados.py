alunos = ["mel", "lara", "maria", "manu", "artur"]
notas = [80, 70, 100, 99, 55]

for nota in notas:

    if nota >= 60:
        indice = notas.index(nota)
        print(alunos[indice])
print(f"nota atual: {alunos} ")