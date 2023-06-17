def inputDate(formato, fechaStr):
    formatoSplit = formato.split("/")
    fechaSplit = fechaStr.split("/")
    
    if len(formatoSplit) == 3 and len(fechaSplit) == 3:
        diaFormato = formatoSplit[0]
        mesFormato = formatoSplit[1]
        añoFormato = formatoSplit[2]
        
        if diaFormato == "dd" and mesFormato == "mm" and añoFormato == "aaaa":
            dia = int(fechaSplit[0])
            mes = int(fechaSplit[1])
            año = int(fechaSplit[2])

            if len(str(año)) == 4 and 1 <= dia <= 31 and 1 <= mes <= 12:
                return f"dia: {dia}, mes: {mes}, año: {año}"
        
        elif diaFormato == "mm" and mesFormato == "dd" and añoFormato == "aaaa":
            dia = int(fechaSplit[1])
            mes = int(fechaSplit[0])
            año = int(fechaSplit[2])

            if len(str(año)) == 4 and 1 <= dia <= 31 and 1 <= mes <= 12:
                return f"mes: {mes}, dia: {dia}, año: {año}"

        elif diaFormato == "aaaa" and mesFormato == "mm" and añoFormato == "dd":
            dia = int(fechaSplit[2])
            mes = int(fechaSplit[1])
            año = int(fechaSplit[0])

            if len(str(año)) == 4 and 1 <= dia <= 31 and 1 <= mes <= 12:
                return f"año: {año}, mes: {mes}, dia: {dia}"
    
    return "fecha invalida"

fecha1 = inputDate("aaaa/mm/dd", "2012/12/10")
print(fecha1)

