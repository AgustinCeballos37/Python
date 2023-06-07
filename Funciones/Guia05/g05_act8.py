nombres = []
def cargaUsuarios():
    escape = 0
    while escape != 1:
        user = input("Ingrese un nombre('salir' para escapar): ")
        if user == "salir":
            escape = 1
            break
        else:
            nombres.append(user)

def buscadorUsuarios():
    nameToFind = input("Ingrese el nombre a buscar: ")
    for name in range(len(nombres)):
        if nombres[name] == nameToFind:
            return name
cargaUsuarios()
posicion = buscadorUsuarios()
print(f"La posicion del nombre es:",posicion, "o",(posicion+1),"Si no te gusta arrancar a contar del 0")
