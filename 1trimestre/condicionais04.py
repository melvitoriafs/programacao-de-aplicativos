temperatura = float(input("digite a temperatura: "))
if temperatura >= 80:
   print ("PERIGO! desligando servidor por superaquecimento!")
elif temperatura >= 50 < 80:
    print ("Alerta: ventoinhas ligadas no maximo!")
elif temperatura < 50:
    print ("Temperatura estavel. sistema operando normalmente")