resultado = 0
for x in range(5):
    numero = int(input("Ingrese un numero:\n"))
    if numero > 23:
        resultado = resultado + numero
print(resultado)