temperatura = float(input("Ingrese la temperatura del reactor en °C: "))
presion = float(input("Ingrese la presión del reactor en bar: "))
refrigerante = float(input("Ingrese el nivel de refrigerante (en %): "))

estado_base = ""

if temperatura > 800 and presion > 500:
    estado_base = "CRÍTICO"
elif (600 <= temperatura <= 800) or (300 <= presion <= 500):
    estado_base = "ALERTA"
else:
    estado_base = "NORMAL"

estado_final = ""

if refrigerante < 50:
    if estado_base == "NORMAL":
        estado_final = "ALERTA"
    elif estado_base == "ALERTA":
        estado_final = "CRÍTICO"
    elif estado_base == "CRÍTICO":
        estado_final = "CRÍTICO" 
else:
    estado_final = estado_base

print(f"Estado: {estado_final}")