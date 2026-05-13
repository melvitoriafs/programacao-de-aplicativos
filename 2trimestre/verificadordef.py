numero = int(input("digite um número: "))

def eh_par(numero):
    if numero % 2 == 0:
        return "O número é par"
    else:
        return "O número é impar"

par_impar = eh_par(numero)
print(par_impar) 