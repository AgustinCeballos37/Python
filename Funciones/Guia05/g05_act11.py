#cargar en listas los nombres y fechas de nacimiento de varias personas, 
#luego recorrerlo y mostrar los nombres de los mayores de edad.
def carga():
    nombres = []
    fechasNacimientos = []
    escape = 0
    while escape != 1:
        nombre = input("Ingrese un nombre(Escriba '.' para dejar de cargar): ")
        if nombre == ".":
            break
        nacimiento = input("Ingrese fechas de nacimiento en formato 'AAAA-MM-DD' ")
        nombres.append(nombre)
        fechasNacimientos.append(nacimiento)
    return nombres, fechasNacimientos

def calculoEdad():
    mayoresEdad = []
    nombres, fechasNacimientos = carga()
    for i in range(len(fechasNacimientos)):
        fechaAcual = 2023
        fecha = fechasNacimientos[i].split("-")
        fechaToInt = int(fecha[0])
        edad = fechaAcual - fechaToInt
        if edad >= 18:
            mayoresEdad.append(nombres[i])
    return mayoresEdad

mayoresEdad = calculoEdad()
for nombre in mayoresEdad:
    print(nombre," es mayor de edad")