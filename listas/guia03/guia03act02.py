# Cargar letras en una lista (while). Contar las vocales (for). Mostrar el total.

letras = []
vocales = ["a","e","i","o","u"]
contador = 0

while True:
    letra = input("Ingrese una letra(ingrese . para terminar de cargar)\n ")
    if letra == ".":
        break
    letras.append(letra)

for letra in letras:
    for vocal in vocales:
        if letra == vocal:
            contador += 1  

print("El total de vocales es:", contador)