#Dada una lista de enteros ordenada ascendente y sin repetidos,
#hacer un programa que genere una nueva lista con todos los que faltan entre
#el menor y el mayor. Mostrar ambas listas.
#Comprobar primero que la lista cumpla con la condición inicial.

numeros = []
numerosNuevos = []
numeroAnterior = 0
checkerAscendente = 0
checkerDuplicado = 0
aprobacion = True

#Entrada de numeros por el usuario
while True:
    inputNumero = int(input("Ingrese un numero(666 para dejar de cargar)\n"))
    if inputNumero == 666:
        break
    numeros.append(inputNumero)

#Checker    
for x in range(len(numeros)):
    if numeros[x] in numeros:
        checkerDuplicado = 0
    else:
        checkerDuplicado = 1
    if numeros[x] > numeroAnterior:
        numeroAnterior = numeros[x]
    else:
        checkerAscendente = 1

if checkerDuplicado == 1 or checkerAscendente == 1:
    aprobacion = False
    print("El numero esta en la lista repetido o no esta de forma ascendente")
    print(numeros)

#Crear una lista con todos los numeros entre el menor y el mayor
#Luego remover los repetidos entre la lista original y la nueva.

if aprobacion == True:
    internalCounter = numeros[0]
    while internalCounter != numeros[-1]:
        internalCounter += 1
        numerosNuevos.append(internalCounter)

    for num in numerosNuevos:
        if num in numeros:
            numerosNuevos.remove(num)    

    print(numeros)
    print(numerosNuevos)

