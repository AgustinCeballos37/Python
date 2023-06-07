def checkeadorDeLetra(letra, cadena):
    cantidad = 0
    for let in cadena:
        if let == letra:
            if letra == "." or letra == " " or letra == ",":
                cantidad += 0
            else:
                cantidad += 1
    return cantidad

print(checkeadorDeLetra("a", "Quiero comer manzanas, solamente manzanas."))