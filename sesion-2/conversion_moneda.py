def convertir_moneda(monto, tipo_cambio=3.80, de_dolares_a_soles=True):
    """
    Convierte montos entre dólares y soles.

    Parámetros:
    - monto: cantidad a convertir
    - tipo_cambio: valor del dólar respecto al sol
    - de_dolares_a_soles:
        True  -> convierte de dólares a soles
        False -> convierte de soles a dólares
    """

    if de_dolares_a_soles:
        resultado = monto * tipo_cambio
    else:
        resultado = monto / tipo_cambio

    return round(resultado, 2)


# Convertir de soles a dólares
monto_total_dolares = convertir_moneda(100, 3.85, False)
print(f"Monto en dólares: ${monto_total_dolares}")


# Convertir de dólares a soles
monto_total_soles = convertir_moneda(200, 3.60, True)
print(f"Monto en soles: S/ {monto_total_soles}")