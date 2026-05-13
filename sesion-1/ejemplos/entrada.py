# Ingreso de variables mediante consola

contrasena_input = input("Ingrese una contraseña: ")
contrasena_db = "123456"

# Cuando es doble igual es comparativa -> "=="
# Cuando es signo de exclamacion es diferente -> "!="
if contrasena_db == contrasena_input:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")