def convertir_moneda(monto, tipo_de_cambio = 3.80, conversion_soles = True):

    if conversion_soles:
        resultado = monto / tipo_de_cambio # Si conversion_soles es verdadero el monto a ingresar es dolares y lo convertire a soles
    else:
        resultado = monto * tipo_de_cambio # Si conversion_soles es falso el monto a ingresar es soles y lo convertire a dolares


    return resultado

monto_total_soles = convertir_moneda(100, 3.85, False)
print(f"Monto en soles: {monto_total_soles}")

monto_total_dolares = convertir_moneda(200, 3.60, True)
print(f"Monto en dolares: {monto_total_dolares}")