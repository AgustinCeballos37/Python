#9)	Verifique si para cada paréntesis abierto en una cadena de texto, hay un paréntesis cerrado correspondiente.

cadenaTexto = "(texto (con parentesis de ejemplo) sin errores)"
parenAbiertos = 0

for caracter in cadenaTexto:
    if caracter == "(":
        parenAbiertos += 1
    elif caracter == ")":
        if parenAbiertos > 0:
            parenAbiertos -= 1

if parenAbiertos == 0:
    print("la cadena de texto tiene los parentesis correctamente")
else:
    print("la cadena de texto no tiene los parentesis correctamente")