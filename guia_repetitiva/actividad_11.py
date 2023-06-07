#Ingresar 7 números enteros y en el caso de que 
#sean naturales de una sola cifra mostrar un cartel por cada uno.


for x in range(7):
    numero = int(input("Ingresar numero entero:\n"))
    if numero < 10 or numero < -10:
        print("numero natural de una sola cifra")