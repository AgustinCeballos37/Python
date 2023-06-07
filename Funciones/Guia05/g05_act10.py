#Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
lluvia = []

def ingresoDeLluvia(listaDias):
    for dia in listaDias:
        print("actualmente estamos en el dia: ", dia)
        cantidad = float(input("Ingrese la lluvia caída: "))
        lluvia.append(cantidad)

def totalNombreLluvia():
    totalLluvia = 0
    maximo = 0
    indice = 0
    for cantidad in lluvia:
        totalLluvia += cantidad

    for i in range(len(lluvia)):
        if lluvia[i] > maximo:
            maximo = lluvia[i]
            indice = i
    diaMaximo = dias[indice]
    print("Total de lluvia caída: ", totalLluvia ,"mm")
    print("Día con más lluvia: ", diaMaximo,"con",maximo,"mm")

ingresoDeLluvia(dias)
totalNombreLluvia()