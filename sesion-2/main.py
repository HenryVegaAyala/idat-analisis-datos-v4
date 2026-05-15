# 1. Crear una lista de productos --> string
vitrina = ["Pan", "Alfajor", "Aceite", "Mantequilla"]

# 2. Lista de números --> Int
venta_horas = [10, 20, 15, 20]

# 3. Acceder al primero elemento de una lista (indice 0)
primer_producto = vitrina[0]
print(f"Primer producto: {primer_producto}")

# 4. Acceder al ultimo elemento de una lista (indice -1)
ultimo_producto = vitrina[-1]
print(f"Ultimo producto: {ultimo_producto}")

# 5. Contar cuantos elementos hay en una lista
total_productos = len(vitrina)
print(f"Total de productos: {total_productos}")

# 6. Agregar nuevo producto a la lista
vitrina.append("Donut")
print(f"Lista de productos agregados: {vitrina}")

# 7. Cambiar o actualizar un producto de la lista
vitrina[2] = "Aceite de oliva"
print(f"Lista de productos actualizados: {vitrina}")

# 8. Eliminar producto de la lista por item
vitrina.remove("Pan")
print(f"Lista de productos actualizados: {vitrina}")

# 9. Eliminar producto de la lista por indice
del vitrina[0]
print(f"Lista de productos actualizados: {vitrina}")

# 10. Como saber que item he eliminado usando POP
producto_eliminado = vitrina.pop(1)
print(f"Vitrina despues de usar pop: {vitrina}")
print(f"Producto eliminado usando pop: {producto_eliminado}")

# 11. Verificar si existe un producto en la lista
existe_donut = "Donut" in vitrina
print(f"Existe donut: {existe_donut}")