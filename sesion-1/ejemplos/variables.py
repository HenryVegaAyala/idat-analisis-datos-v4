# 1. Texto simple -> string
negocio = "Café python"

# 2. Texto con comilla simple -> string
eslogan = 'El mejor café de la ciudad'

# 3. Número entero -> int
sillas_disponibles = 20

# 4. Número decimal -> float
precio_cafe = 2.50

# 5. Valor booleano -> bool (Verdadero)
esta_abierto = True

# 6. Valor booleano -> bool (Falso)
hay_descuento = False

# 7. Textos largos
direccion = "Av. proceres con la residencial la cruceta, Surco, 540"

# 8. Un número como texto
codigo_postal = "500"

# 9. Variables vacias
proxima_oferta = None

# 10. Caracteres especiales en texto
emoji_cafe = "☕"

# Variable concatenada
concatenar_v1 = negocio + " - " + eslogan
print(concatenar_v1)

concatenar_v2 = f"{negocio} - {eslogan}"
print(concatenar_v2)

print(f"Ejemplo 1-10: Bienvenido a {concatenar_v2} {emoji_cafe}")