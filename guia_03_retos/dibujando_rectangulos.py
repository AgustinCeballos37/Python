alto = int(input("Ingrese la altura del rectangulo:\n"))
ancho = int(input("Ingrese el ancho del rectangulo:\n"))
caracter = input("Ingrese el caracter a utilizar:\n")

for x in range(alto):
    for y in range(ancho):
        print(caracter, end="")
    print()