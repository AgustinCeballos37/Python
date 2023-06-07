def cargadorEnLista(cadena):
    cadenaALista = cadena.split()
    fraseALista = []
    for frase in cadenaALista:
        fraseLimpia = frase.strip(",.")
        fraseALista.append(fraseLimpia)
    return fraseALista

def obtenedorPalabraMasLarga(cadena):
    listaDevolvida = cargadorEnLista(cadena)
    palabraMasGrande = ""
    tamañoPalabraMasGrande = 0
    for palabra in listaDevolvida:
        tamañoPalabra = len(palabra)
        if tamañoPalabra > tamañoPalabraMasGrande:
            tamañoPalabraMasGrande = tamañoPalabra
            palabraMasGrande = palabra
    return palabraMasGrande, tamañoPalabraMasGrande

print(obtenedorPalabraMasLarga("Quiero comer manzanas, solamente manzanas."))