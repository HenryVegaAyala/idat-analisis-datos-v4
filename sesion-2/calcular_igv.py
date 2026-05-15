def calcular_precio_final(precio_base):
    igv = 0.18
    impuesto = precio_base * igv
    total = impuesto + precio_base
    return total

producto_a = calcular_precio_final(100)
print("El precio final del producto A es:", producto_a)

producto_b = calcular_precio_final(120)
print("El precio final del producto B es:", producto_b)