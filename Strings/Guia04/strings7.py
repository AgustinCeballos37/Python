#7.	Buscar una palabra y reemplazarla por otra todas las veces que aparezca.
# Ej.: ‘peras’ en lugar de ‘manzanas’
# quedaría 'Quiero comer peras, solamente peras.' Sin usar replace.

frase = "Quiero comer manzanas, solamente manzanas."
fraseEnLista = frase.split()
palabraABuscar = "manzanas"
palabraAReemplazar = "peras"
nuevaFrase = ""

for palabra in fraseEnLista:
    palabraLimpia = palabra.strip(",.")
    if palabraLimpia == palabraABuscar:
        nuevaFrase += palabraAReemplazar + " "
    else:
        nuevaFrase += palabra + " "

print(nuevaFrase)