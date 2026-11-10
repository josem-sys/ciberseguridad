def comprobar_longitud(contrasena):
    return len(contrasena) >= 8 #devuelve automaticamente true o false

contrasena = "Hola1234"
print(contrasena)
print("Longitud válida de Hola1234:", comprobar_longitud(contrasena))
print("Longitud válida de Hola:", comprobar_longitud("Hola"))
