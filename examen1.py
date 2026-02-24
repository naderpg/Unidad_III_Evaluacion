
señal = input("Ingrese la señal actual (verde, amarillo, rojo): ").strip().lower()

distancia = float(input("Ingrese la distancia a la próxima estación en km: "))

obstaculo_input = input("¿Hay un obstáculo en la vía? (True/False): ").strip().lower()

obstaculo = obstaculo_input == "true" or obstaculo_input == "si"

velocidad = 0

if obstaculo:
    velocidad = 0
else:

    if señal == "verde":
        if distancia > 5:
            velocidad = 100
        else:
            velocidad = 80
            
    elif señal == "amarillo" or señal == "amarilla":
        if distancia > 3:
            velocidad = 50
        else:
            velocidad = 30
            
    elif señal == "rojo" or señal == "roja":
        velocidad = 0
        
    else:
        print("Error: Señal ingresada no válida.")


print(f"Velocidad: {velocidad} km/h")