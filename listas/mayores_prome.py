#dada una lista de numeros
#1) obtener el promedio.
#2) obtener los valores mayores al promedio.

numeros = [6,8,4,9,10]
totalPuntajeNotas = 0
for i in range(len(numeros)):
    totalPuntajeNotas = totalPuntajeNotas + numeros[i]
promedio = (totalPuntajeNotas / len(numeros))
print(promedio)

for i in range(len(numeros)):
    if numeros[i] >= promedio:
        print(numeros[i])

    