#Primer for: Almacenar en dos listas paralelas, nombres y sexos de 8 personas. 
#Segundo for: Recorrerlas y guardar los nombres de las mujeres en una nueva lista. 
#Mostrar los elementos de la lista resultante.

nombres = []
mujeres = []
sexos = []

for x in range(8):
    nombre = input("Ingrese el nombre de la persona: ")
    sexo = input("Ingrese el sexo de la persona: ")
    nombres.append(nombre)
    sexos.append(sexo)

for y in range(len(nombres)):
    if sexos[y] == "f":
        mujeres.append(nombres[y])

print("los nombres de las mujeres son:")
for nombre in mujeres:
    print(nombre)