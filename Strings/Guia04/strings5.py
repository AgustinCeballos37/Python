#5.	Recibir por teclado una cadena de números e insertar 
# un punto cada 3 dígitos como divisorio de miles. 
#Ej.  1234567890 debería devolver 1.234.567.890

cadenaNumeros = input("Ingrese una cadena de numeros")

cadenaNueva = ""
for x in range(len(cadenaNumeros)):
    cadenaNueva += cadenaNumeros[x]
    if x % 3 == 0 and (x + 1) != len(cadenaNumeros):
        cadenaNueva += "."

print(cadenaNueva)

