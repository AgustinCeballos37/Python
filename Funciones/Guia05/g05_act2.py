def reemplazadorPalabra(palabraAReemplazar,palabraABuscar,cadena):
    cadenaSeparadaParaLista = cadena.split()
    nuevaFrase = ""
    palabraLimpia = ""
    for palabra in cadenaSeparadaParaLista:
        palabraLimpia = palabra.strip(",.")
        if palabraLimpia == palabraABuscar:
            nuevaFrase += palabraAReemplazar + " "
        else:
            nuevaFrase += palabra + " "
    return nuevaFrase

print(reemplazadorPalabra("peras","manzanas","Quiero comer manzanas, solamente manzanas."))
