#Eliminar el plural en esta frase: “Real Madrid gana las copas.” 
#Recorrer y quitar las eses. Sugerencia: Usar otra string.

frase = "Real Madrid gana las copas."
fraseNueva = ""
for x in range(len(frase)):
    if frase[x] != "s":
        fraseNueva = fraseNueva + frase[x]
print(fraseNueva)
