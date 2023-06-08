
def cargaUsuarios():
    nombres = []
    escape = 0
    while escape != 1:
        user = input("Ingrese un nombre('salir' para escapar): ")
        if user == "salir":
            escape = 1
            break
        else:
            nombres.append(user)
    return nombres

def buscadorUsuarios():
    nombres = cargaUsuarios()
    nameToFind = input("Ingrese el nombre a buscar: ")
    for name in range(len(nombres)):
        if nombres[name] == nameToFind:
            return name


posicion = buscadorUsuarios()
print(f"La posicion del nombre es:",posicion, "o",(posicion+1),"si no te gusta arrancar a contar del 0")
