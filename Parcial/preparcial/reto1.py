#1)	Dados estos datos desordenados, encontrar los sueldos y obtener el total.
#‘Pedro$120.000, Ana(frontend)$512.700, el portero$175.120, el pibe del backend(capaz hay que actualizarle!)$371.459, revisar bien el total de erogaciones!’

datos = "Pedro$120.000, Ana(frontend)$512.700, el portero$175.120, el pibe del backend(capaz hay que actualizarle!)$371.459, revisar bien el total de erogaciones!, $1 peso le viene bien a ese man"

sueldos = []
totalSueldos = 0

splitComa = datos.split(",")
for string in splitComa:
    sueldo = ""
    for caracter in string:
        if caracter >= "0" and caracter <= "9":
            sueldo += caracter
    if sueldo != "":
        sueldos.append(int(sueldo))
        totalSueldos += int(sueldo)

print("Lista de sueldos:", sueldos)
print("El total de $ es", totalSueldos)
