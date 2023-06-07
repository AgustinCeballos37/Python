#8.	Contar la cantidad de letras (no incluir los separadores).

frase = "Quiero comer manzanas, solamente manzanas."
contador = 0
for letra in frase:
    if letra == "." or letra == " " or letra == ",":
        contador += 0
    else:
        contador += 1
print(contador) 