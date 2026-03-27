temps = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0 ]

for valor in temps:
    if temps > 30.0:
        print(f"ALERTA: Temperatura crítica! ({valor}°C)")
        else:
            print(f"Temperatura normal. ({valor}°C)")