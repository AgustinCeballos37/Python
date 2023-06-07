#Dada una lista con números, crear otra con los cuadrados de esos valores. 
numeros = [1,3,6,8,9,11,23]
numerosx2 = []

for numero in numeros:
    numero *= numero
    numerosx2.append(numero)
print(numerosx2)
for numerox2 in numerosx2:
    print(numerox2)
