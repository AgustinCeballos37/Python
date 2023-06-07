
hayDatos = input("Hay datos para ingresar?\n")
while hayDatos != "no":
    numero = int(input("Ingrese un numero para ver si es positivo o negativo:\n"))
    if numero >= 0:
        print("El numero es positivo")
    else:
        print("El numero es negativo")
    hayDatos = input("Hay mas datos para ingresar?\n")