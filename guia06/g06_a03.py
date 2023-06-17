def promedio(*args, sinNegativos=False):
    listaRefinada = []

    if sinNegativos == True:
        for arg in args:
            if arg >= 0:
                listaRefinada.append(arg)
    else:
        for arg in args:
            listaRefinada.append(arg)

    numeroFinal = 0
    for numero in listaRefinada:
        numeroFinal += numero

    if numeroFinal % len(listaRefinada) == 0:
        return numeroFinal // len(listaRefinada)
    else:
        return numeroFinal / len(listaRefinada)
 
print(promedio(121,65,-88,34,-9,27)) # 150/6=25
print(promedio(121,65,-88,34,-9,27, sinNegativos=True)) # 247/4=61.75
print(promedio(2,4)) # 3