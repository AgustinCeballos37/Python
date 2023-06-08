def promedio(numeros):
    sumador = 0
    cantidadNumeros = len(numeros)
    for num in range(len(numeros)):
        sumador += numeros[num]
    return sumador / cantidadNumeros

def mayorQue():
    numeros = [7, 9, 10, 6, 8, 9, 10, 7, 4, 10, 9]
    numeroPromedio = int(promedio(numeros))
    print("El promedio es", numeroPromedio)
    for num in range(len(numeros)):
        if numeroPromedio < numeros[num]:
            print(numeros[num])

mayorQue()