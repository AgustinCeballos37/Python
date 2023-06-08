#Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 
def ingresoDeLluvia(listaDias):
    lluvia = []
    for dia in listaDias:
        print("Actualmente estamos en el día:", dia)
        cantidad = float(input("Ingrese la lluvia caída: "))
        lluvia.append(cantidad)
    return lluvia

def totalNombreLluvia(listaDias, listaLluvia):
    totalLluvia = 0
    maximo = 0
    indice = 0

    for cantidad in listaLluvia:
        totalLluvia += cantidad

    for i in range(len(listaLluvia)):
        if listaLluvia[i] > maximo:
            maximo = listaLluvia[i]
            indice = i
    diaMaximo = listaDias[indice]

    return totalLluvia, maximo, indice, diaMaximo

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

lluvia = ingresoDeLluvia(dias)
totalLluvia, maximo, indice, diaMaximo = totalNombreLluvia(dias, lluvia)

print("Total de lluvia caída:", totalLluvia, "mm")
print("Día con más lluvia:", diaMaximo, "con", maximo, "mm")