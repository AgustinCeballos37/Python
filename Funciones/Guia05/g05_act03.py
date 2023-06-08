def cleanerDeCadena(cadena):
    cadenaPointsOff = cadena.replace(".","")
    cadenaCommasOff = cadenaPointsOff.replace(",","")
    cadenaSpaceOff = cadenaCommasOff.replace(" ", "")
    return cadenaSpaceOff

def contadorDeLetra(cadena):
    cadenaLimpia = cleanerDeCadena(cadena)
    contadorLetra = 0
    for letra in cadenaLimpia:
        contadorLetra += 1
    return contadorLetra

print(contadorDeLetra("Quiero comer manzanas, solamente manzanas."))