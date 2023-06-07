nombres = []
sexos = []

def cargaUsuarios():
    escape = 0
    while escape != 1:
        user = input("Ingrese un nombre: ")
        nombres.append(user)
        sexo = input("Ingrese sexo: ")
        sexos.append(sexo)
        escape = int(input("Seguir cargando(1 para no) "))

def mostrarMujeres():
    for x in range(len(nombres)):
        if sexos[x] == "femenino":
            print(nombres[x])

cargaUsuarios()
mostrarMujeres()