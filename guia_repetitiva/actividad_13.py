#Ingresar la lluvia caída en milímetros para cada día de la semana. 
#Mostrar al final el total de lluvia caída y la cantidad de días que no llovió.
totalLluvia = 0
diasNoLlovidos = 0
for x in range(1,8):
    print("Dia", x)
    lluviaMilimetros = int(input("Ingrese la cantidad de lluvia:\n"))
    if lluviaMilimetros == 0:
        diasNoLlovidos = diasNoLlovidos + 1
    totalLluvia = totalLluvia + lluviaMilimetros
print("Llovieron la cantidad de", totalLluvia,"milimetros", "No llovio en", diasNoLlovidos,"dias")