#8)	Encontrar todos los números en una cadena de texto y totalizarlos

cadenaTexto = "nacio un 1999-01-01, un 2010-02-04 se anoto a un curso de ajedrez, 2023-01-23 encontro la improvisacion"

numeros = {
    "0": 0,
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

for caracter in cadenaTexto:
    if caracter >= "0" and caracter <= "9":
        numeros[caracter] += 1

for numero, cantidad in numeros.items():
    finalMensaje = "Numero " + numero + ": " + str(cantidad) + " veces"
    print(finalMensaje)