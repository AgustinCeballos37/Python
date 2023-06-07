#Tengo una lista con nombres y otra paralela con direcciones completas
# (calle y número). 
#Mostrar cada calle y la cantidad de personas que vive en cada una.
#Ejemplo: 
#nombres = ['Ana', 'José', 'Lisa', 'Juan']
#direcciones = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']
# 	La salida sería:
#	Mitre 1
#9 de Julio 2
#Alvear 1
#	(Saqué lo de los nombres porque se hacía bastante más difícil)

nombres = ['Ana', 'José', 'Lisa', 'Juan']
direccionesCompletas = ['Mitre 1234', '9 de Julio 345', 'Alvear 999', '9 de Julio 11']
calles = []
contador = []
for direccion in direccionesCompletas:
    calle = direccion.split()[0]
    encontrado = False #forma de saber si el contador inicio

    for i in range(len(calles)):
        if calles[i] == calle:
            contador[i] += 1  
            encontrado = True 
            break

    if not encontrado: #inicializamos los valores para trabajar
        calles.append(calle)  
        contador.append(1)  


for i in range(len(calles)):#recorremos para guardar los valores luego mostrarlos
    calle = calles[i]
    cantidadPersonas = contador[i]
    print(calle, cantidadPersonas)
