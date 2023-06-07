#5)	Ordena una lista de palabras por su longitud de mayor a menor.

listaPalabras = ["Salud", "Felicidad", "Amor", "Valentia", "Coordinacion"]

listaOrdenada = []  

for palabra in listaPalabras:
    for i in range(len(listaOrdenada)):
        if len(palabra) > len(listaOrdenada[i]):
            listaOrdenada.insert(i, palabra)
            break
    else:
        listaOrdenada.append(palabra)  

for palabra in listaOrdenada:
    print(palabra)