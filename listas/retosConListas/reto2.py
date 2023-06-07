#Hacer un programa que cuente el número total de bumeranes de una lista de números enteros y muestre cada uno de ellos. 
#Un búmeran es una secuencia formada por 3 números seguidos, 
#en la cual el primero y el último son iguales, y el segundo es diferente. Por ejemplo [5, 2, 5]. 
#En la lista [7, 2, 1, 2, 3, 3, 3, 4, 2, 4, 1, 8]  hay 2 bumeranes ([2, 1, 2] y [4, 2, 4]).

contador = 0
listaNumeros = [7, 2, 1, 2, 3, 3, 3, 4, 2, 4, 1, 8]

for x in range(len(listaNumeros) -2):
# el -2 al rango total de elementos del array es debido a que no hace falta los ultimos 2 valores para checkear si hay un bumeran
# ademas de esta forma conseguimos no salirnos del index total del array
    if listaNumeros[x] == listaNumeros[x+2] and listaNumeros[x] != listaNumeros[x+1]:
        contador += 1
        print(listaNumeros[x], listaNumeros[x+1], listaNumeros[x+2])

print("Se encontraron", contador, "bumeranes")