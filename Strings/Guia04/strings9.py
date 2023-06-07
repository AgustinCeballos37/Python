#9.	Contar la cantidad de palabras.

frase = "Quiero comer manzanas, solamente manzanas."
fraseEnLista = frase.split()
contador = 0
for palabra in fraseEnLista:
    contador += 1
print(contador)