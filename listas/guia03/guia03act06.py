#Ingresar nombres en una lista, luego buscar un nombre y de encontrarlo decir en qué posición está.

nombres = []

while True:
    nombre = input("ingrese un nombre: \n")
    if nombre == ".":
        break
    nombres.append(nombre)
buscador = input("Ingrese el termino a buscar:\n")
for x in range(len(nombres)):
    if nombres[x] == buscador:
        print("posicion en el array: ",x + 1)