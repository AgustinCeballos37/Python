#Pedir el ingreso de 10 números. 
#Contar los mayores de 23 y almacenar los que cumplen la condición.  
#Mostrar la cantidad y los números guardados.
numeros = []
contador = 0
for x in range(10):
    numeros.append(int(input("Ingrese un numero ")))

for numero in numeros:
    if numero > 23:
        contador = contador + 1
print("cantidad de items en la lista:", len(numeros),"Hay", contador, "numeros mayores a 23")