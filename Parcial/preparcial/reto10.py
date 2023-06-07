#10)Buscar todas las palabras palíndromas en una cadena de texto y almacenarlas en una lista.

cadenaTexto = "La palabra radar es un ejemplo de palabra palindroma, asi como reconocer y level"

palindromas = []
palabras = cadenaTexto.split()

for palabra in palabras:
    invertida = ""
    if len(palabra) > 1:
        for i in range(len(palabra) - 1, -1, -1):
            invertida += palabra[i]

        if palabra == invertida:
            palindromas.append(palabra)

print(palindromas)