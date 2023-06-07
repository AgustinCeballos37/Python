cantidadDePersonasACargar = int(input("Cuantas personas vas a cargar?\n"))
promedioEdad = 0
for x in range(cantidadDePersonasACargar):
    edad = int(input("Ingresa la edad:\n"))
    promedioEdad = promedioEdad + edad

print("la edad promedio es", round((promedioEdad / cantidadDePersonasACargar),2))

