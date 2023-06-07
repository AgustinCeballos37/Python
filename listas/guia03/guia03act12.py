# Pedir nombres y sexo de personas y 
# mostrar al final el total de mujeres y el nombre de cada una.

nombres = []
sexo = []
totalMujeres = []

while True:
    nombre = input("Ingrese un nombre(presione '.' para salir): ")
    if nombre == '.':
        break
    nombres.append(nombre)
    sex = input("Ingrese el sexo de la persona: ")
    sexo.append(sex)

for i in range(len(nombres)):
    if sexo[i] == 'f':
        totalMujeres.append(nombres[i])

print("Total mujeres: ", len(totalMujeres))
for mujeres in totalMujeres:
    print(mujeres)