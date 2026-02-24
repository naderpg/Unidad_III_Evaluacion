tipo_cliente = input("Ingrese el tipo de cliente (regular, vip, mayorista):").strip().lower()
monto_compra = float(input("Ingrese el monto de la compra:"))
hora_compra = int(input("Ingrese la hora de la compra (formato 24h, ej. 19):"))

descuento = 0

match tipo_cliente:
    case "regular":
        descuento = 5
        if monto_compra > 200:
            descuento += 5
        elif monto_compra < 50:
            descuento -= 2
        else:
            descuento += 0  
            
    case "vip":
        descuento = 10
        if monto_compra > 200:
            descuento += 5
        elif monto_compra < 50:
            descuento -= 2
        else:
            descuento += 0
            
    case "mayorista":
        descuento = 15
        if monto_compra > 200:
            descuento += 5
        elif monto_compra < 50:
            descuento -= 2
        else:
            descuento += 0
            
    case _:
        print("Error: Tipo de cliente no reconocido.")

if 18 <= hora_compra <= 21:
    descuento += 3

if descuento > 20:
    descuento = 20

print(f"Descuento final: {descuento}%")