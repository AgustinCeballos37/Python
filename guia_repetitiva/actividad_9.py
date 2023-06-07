
masNumeros = ""
recuerdo = 0
while masNumeros != "no":
    numero = int(input("Ingrese un numero\n"))
    if numero > recuerdo:
        recuerdo = numero
    masNumeros = input("Hay mas datos para ingresar?\n")
    print(recuerdo)


