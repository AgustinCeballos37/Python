#Eliminar todos los valores iguales de una lista. 
#Previamente, solicitar el valor y si no está, 
#mostrar un cartel diciendo que no lo ha encontrado.

lista = ["arroz","pato","leon","comida","test"]
nuevaLista = []
print("array original: ", lista)
termino = input("Ingresar el valor a buscar en el array:\n")
checker = False

for valor in lista:
    if termino == valor:
        checker = True
        break
if checker == True:
    for valor in lista:
        if valor != termino:
            nuevaLista.append(valor)
    print(nuevaLista)
else:
    print("No se a encontrado el termino en el array.")