def contadorDeVocales(lista):
    ca = 0
    ce = 0
    ci = 0
    co = 0
    cu = 0
    for valor in lista:
            if valor == "a":
                ca += 1
            elif valor == "e":
                ce += 1
            elif valor == "i":
                ci += 1
            elif valor == "o":
                co += 1
            elif valor == "u":
                cu += 1
    return ca,ce,ci,co,cu
print(" a ","e"," i"," o"," u")
print(contadorDeVocales(['a', 'b', 'c', 'd', 'e', 'a', 'i', 'o', 'i', 'j']))