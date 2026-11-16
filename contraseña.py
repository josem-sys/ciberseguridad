from utilidades import comprobar_numero #llamar la función de utilidades.py
def comprobar_longitud(contrasena):
    return len(contrasena) >= 8 #devuelve automaticamente true o false

contrasena = "Hola1234"
print(contrasena)
print("Longitud válida de Hola1234:", comprobar_longitud(contrasena))
print("Longitud válida de Hola:", comprobar_longitud("Hola"))

print("¿Tiene números la contraseña?:", comprobar_numero(contrasena))
print("¿Tiene números 'Hola'?:", comprobar_numero("Hola"))
print("¿Tiene números 'SoloLetras'?:", comprobar_numero("SoloLetras"))
