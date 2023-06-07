#Tomar una fecha en formato "DD-MM-AAAA" y convertirla en "D de [Mes] de AAAA".

fecha = "01-01-1999"

dia, mes, año = fecha.split("-")

if dia[0] == "0" :
    dia = dia[1:]

diccionarioMeses = {
    "01": "enero",
    "02": "febrero",
    "03": "marzo",
    "04": "abril",
    "05": "mayo",
    "06": "junio",
    "07": "julio",
    "08": "agosto",
    "09": "septiembre",
    "10": "octubre",
    "11": "noviembre",
    "12": "diciembre"
}

nombreMes = diccionarioMeses.get(mes)
print(dia,"de",nombreMes,"de",año)