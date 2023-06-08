def cantidadDePalabra(cadena):
    cadenaSplit = cadena.split()
    contador = 0
    for palabra in cadenaSplit:
        contador += 1
    return contador
print(cantidadDePalabra("Quiero comer manzanas, solamente manzanas."))