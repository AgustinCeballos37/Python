ingresador = ""
nombres = ""
contadorMujeres = 0
while ingresador != "no":
    nombre = input("Ingresar el nombre:\n")
    sexo = input("Ingresar sexo:\n (M/F)")
    if sexo == "F":
        contadorMujeres = contadorMujeres + 1
        nombres = nombres + "," + nombre
    ingresador = input("Seguir agregando personas?:\n (si/no)")
print("Hay",contadorMujeres, "Mujeres","sus nombres son:", nombres)
