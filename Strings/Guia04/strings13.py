#Pedir el ingreso de un nombre completo en la forma <nombre> <apellido>
# (ejemplo: Juan Pérez)
# y mostrarlo invertido y con coma <apellido>,<nombre> (ejemplo: Perez, Juan).

nombreCompleto = input("Ingrese un nombre completo en la forma <nombre> <apellido>\n")

nombreEnLista = nombreCompleto.split()
nombreInvertido = nombreEnLista[1] + ", " + nombreEnLista[0]

print(nombreInvertido)