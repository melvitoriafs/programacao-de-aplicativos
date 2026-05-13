pendentes = ["relatorio.pdf", "foto.png", "planilha.xlsx"]
print (f"lista de pendentes {pendentes}")
concluidos = []

concluidos.append(pendentes[0])
pendentes.pop(0)

print("pendentes: " , pendentes)
print("concluidos: " , concluidos)

