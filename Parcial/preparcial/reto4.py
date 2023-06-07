#4)	Extraer todas las fechas de una cadena de texto. El formato es AAAA-MM-DD

cadenaTexto = "nacio un 1999-01-01, un 2010-02-04 se anoto a un curso de ajedrez, 2023-01-23 encontro la improvisacion"

fechasEncontradas = []
fechaActual = ""
for caracter in cadenaTexto:
    if caracter >= "0" and caracter <= "9":
        fechaActual += caracter
    elif caracter == "-":
        fechaActual += caracter
    else:
        if len(fechaActual) == 10:
            fechasEncontradas.append(fechaActual)
        fechaActual = ""

for fecha in fechasEncontradas:
    print(fecha)