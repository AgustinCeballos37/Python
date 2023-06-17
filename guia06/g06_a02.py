def cadenaCleaner(cadena):
    nuevaCadena = ""
    for caracter in cadena:
        if caracter.isalpha() or caracter.isspace():
            nuevaCadena += caracter
    return nuevaCadena

def contarSubCadena(cadena, fraseBuscada, ignorarMayus=True):
    cadena = cadenaCleaner(cadena)
    if ignorarMayus == True:
        cadena = cadena.lower()
        fraseBuscada = fraseBuscada.lower()
    
    contador = 0
    palabras = cadena.split()
    for palabra in palabras:
        if palabra == fraseBuscada:
            contador += 1

    return contador
frase = 'Desde niña me encanta mirar la luna, por eso es que le puse de nombre Luna a mi hija'
print(contarSubCadena(frase, "luna"))
print(contarSubCadena(frase, 'luna', ignorarMayus=False)) 