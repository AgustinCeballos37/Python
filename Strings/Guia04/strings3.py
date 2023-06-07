#Decir cuántas veces se repite una letra cualquiera, en un texto dado. 
#Por recorrido.

frase = "las mejores flores son rosas"
letraBuscada = input("Ingrese una letra a buscar:\n")
contador = 0
for letra in frase:
    if letraBuscada == letra:
        contador += 1

print("La palabra " + letra,"se repite", contador)
