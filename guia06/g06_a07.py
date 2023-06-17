def inputChoice(opciones, mensaje='ingrese una opcion: '):
    validado = False
    
    while not validado:
        choice = input(mensaje+" ")
        opcionesExpliteao = opciones.split("/")

        if choice in opcionesExpliteao:
            validado = True
        else:
            print(f'opcion no soportada las opciones validas son: {opcionesExpliteao}')
    
    return choice

#q = inputChoice('si/no/a veces')
#print(q)

r = inputChoice("rojo/verde", "elija un color")
print(r)
