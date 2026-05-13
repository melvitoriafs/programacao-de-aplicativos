media = float(input("digite sua media final: "))
presenca = int(input("digite a sua porcentagem de presenca: "))

if media >= 7.0 and presenca >= 75:
    print ("parabens! você foi aprovado ")
elif media < 7.0 and presenca < 75:
    print ("reprovado. verifique sua nota ou frequencia ")
elif media >= 7.0 and presenca < 75:
    print ("reprovado, verifique sua nota ou frequencia ")
elif media <= 7.0 and presenca <= 75: 
    print ("reprovado, verifique sua nota ou frequencia ")