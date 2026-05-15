def convertir_soles(monto_dolares, tipo_de_cambio = 3.80):
    resultado = monto_dolares * tipo_de_cambio
    return resultado

monto_soles = convertir_soles(100)
print(f"Monto en soles: {monto_soles}")

monto_soles = convertir_soles(200, 4)
print(f"Monto en soles: {monto_soles}")