#Dadas dos listas con nombres, una de varones y otra de mujeres, 
#solicitar una letra inicial y mostrar los nombres que comiencen con ella
# en ambas listas en una string concatenada con guiones.
#Ejemplo:
# mujeres = ['Lisa', 'Ema', 'Juana', 'Ester']
#varones = ['Eduardo', 'Pedro']
#inicial = 'E'
#Salida: Ema-Ester-Eduardo

nombresMujeres = ['Lisa', 'Ema', 'Juana', 'Ester']
nombresHombres = ['Eduardo', 'Pedro']
finalList = []
searcher = input("Ingrese termino a buscar:\n")
#me rio de las palabras en ingles que escribo 
for nombre in nombresMujeres:
    if nombre[0] == searcher:
        finalList.append(nombre)
for nombre in nombresHombres:
    if nombre[0] == searcher:
        finalList.append(nombre)

finalPrintOut = "-".join(finalList)
print(finalPrintOut)