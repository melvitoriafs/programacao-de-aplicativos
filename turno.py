ID = int(input("qual seu id? "))
temperatura = float(input("qual a temperatura? "))
tempo_uso = int(input("qual o tempo de uso? "))

if (ID % 3 == 0) and (temperatura > 40 or tempo_uso > 8):
    print(f"funcionário {ID}, você foi escalado para a manutenção preventiva hoje ")
else:
    print (f"funcionário {ID}, sua máquina opera dentro dos padrões normais ")