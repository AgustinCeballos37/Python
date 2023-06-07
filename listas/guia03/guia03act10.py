#Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída y el nombre del día que más llovió. 
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
lluvia = []
totalLluvia = 0
maximo = 0
indice = 0

for dia in dias:
    print("actualmente estamos en el dia: ", dia)
    cantidad = float(input("Ingrese la lluvia caída: "))
    lluvia.append(cantidad)

for cantidad in lluvia:
    totalLluvia += cantidad

for i in range(len(lluvia)):
    if lluvia[i] > maximo:
        maximo = lluvia[i]
        indice = i
dia_maximo = dias[indice]


print("Total de lluvia caída: ,", totalLluvia ,"mm")
print("Día con más lluvia: ", dia_maximo,"con",maximo,"mm")

