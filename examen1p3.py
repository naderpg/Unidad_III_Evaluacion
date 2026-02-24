ingreso = float(input("Ingrese su ingreso anual: "))
edad = int(input("Ingrese su edad: "))
dependientes = int(input("Ingrese el número de dependientes: "))

ingreso_gravable = ingreso - (dependientes * 1000)

if ingreso_gravable < 0:
    ingreso_gravable = 0

impuesto_base = 0

if ingreso_gravable <= 10000:
    impuesto_base = 0
elif ingreso_gravable <= 50000:
    impuesto_base = (ingreso_gravable - 10000) * 0.10
else:
    impuesto_base = 4000 + ((ingreso_gravable - 50000) * 0.20)

if edad > 65:
    descuento = impuesto_base * 0.05
    impuesto_final = impuesto_base - descuento
else:
    impuesto_final = impuesto_base


if impuesto_final.is_integer():
    print(f"Impuesto: {int(impuesto_final)}")
else:
    print(f"Impuesto: {impuesto_final}")