#Cargar en dos listas paralelas nombres y sueldos. 
#Luego mostrar los nombres de las personas que ganan más de $185000.
nombres = []
sueldos = []

while True:
    nombre = input("Ingrese el nombre (o '.' para terminar): ")
    if nombre == ".":
        break
    sueldo = float(input("Ingrese el sueldo: "))
    nombres.append(nombre)
    sueldos.append(sueldo)

print("personas con sueldo mayor a $185000: ")
for i in range(len(nombres)):
    if sueldos[i] > 185000:
        print("[+]",nombres[i])
