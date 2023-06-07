#cargar en listas los nombres y fechas de nacimiento de varias personas, 
#luego recorrerlo y mostrar los nombres de los mayores de edad.

nombres = []
fechasNacimientos = ["1991-01-01", "1996-06-03","1999-01-01","2006-04-02","2006-06-03"]
mayoresEdad = []

for x in range(len(fechasNacimientos)):
    nombre = input("Ingrese un nombre(Escriba '.' para dejar de cargar): ")
    if nombre == ".":
        break
    nombres.append(nombre)

for i in range(len(fechasNacimientos)):
    fechaAcual = 2023
    fecha = fechasNacimientos[i].split("-")
    fechaToInt = int(fecha[0])
    edad = fechaAcual - fechaToInt
    if edad >= 18:
        mayoresEdad.append(nombres[i])

for nombre in mayoresEdad:
    print(nombre)
