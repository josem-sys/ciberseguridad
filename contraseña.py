def comprobar_longitud(contrasena):
    return len(contrasena) >= 8 #devuelve automaticamente true o false

def comprobar_mayuscula(contrasena):
    return any(c.isupper() for c in contrasena)

contrasena = "Hola1234"
print(contrasena)
print("Longitud válida de Hola1234:", comprobar_longitud(contrasena))
print("Longitud válida de Hola:", comprobar_longitud("Hola"))

print("¿Tiene mayúsculas la contraseña?", comprobar_mayuscula(contrasena))
print("¿Tiene mayúsculas 'hola1234'?:", comprobar_mayuscula("hola1234"))
