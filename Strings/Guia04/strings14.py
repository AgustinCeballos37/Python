#Pedir dos nombres y edades respectivas y luego construir una sola cadena
# con un texto que muestre el nombre del mayor y cuanto le lleva al menor. 
#(Ejemplo:  entrada -> 'Juan' 30 'Pedro' 23 / salida -> 
#'Juan le lleva 7 años a Pedro')

nombre1 = input("Ingrese el primer nombre:\n")
edad1 = int(input("Ingrese la edad del primer nombre\n"))
nombre2 = input("Ingrese el segundo nombre:\n")
edad2 = int(input("Ingrese la edad del segundo nombre\n"))

diferenciaEdad = abs(edad1 - edad2)
if edad1 > edad2:
    print(nombre1, "le lleva", diferenciaEdad, "años a", nombre2)
else:
    print(nombre2, "le lleva", diferenciaEdad, "años a", nombre1)
