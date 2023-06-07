#Averiguar qué cantidad de letras tiene la palabra más larga y cual es.

frase = "Quiero comer manzanas, solamente manzanas."
#tratamiento de la frase
fraseEnLista = frase.split()
fraseEnListaLimpia = []
for frase in fraseEnLista :
    fraseLimpia = frase.strip(",.")
    fraseEnListaLimpia.append(fraseLimpia)
#ver cual es mas larga
palabraMasGrande = ""
tamañoPalabraMasGrande = 0
for palabra in fraseEnListaLimpia:
    tamañoPalabra = len(palabra)
    if tamañoPalabra > tamañoPalabraMasGrande:
        tamañoPalabraMasGrande = tamañoPalabra
        palabraMasGrande = palabra
        
print("la palabra mas grande es", palabraMasGrande)
print("su tamaño es", tamañoPalabraMasGrande)