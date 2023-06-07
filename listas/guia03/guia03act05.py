#Guardar en una lista los números pares mayores que 0 y menores que 31. 

numeros = []
numerosPares = []

while True:
    num = int(input("ingrese un numero:(666 para salir) \n"))
    if num == 666:
        break
    numeros.append(num)

for numero in numeros:
    if numero % 2 == 0:    
        if (numero > 0 and numero < 31):
            numerosPares.append(numero)
for numeropar in numerosPares:

    print("Los valores pares mayores que 0 y menos que 31 son: ",numeropar)    
